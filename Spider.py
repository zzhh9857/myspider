# coding:utf-8
__author__ = 'dw'

import requests
from bs4 import BeautifulSoup as bs
import queue
from threading import Thread;


class Spider:
    urlQueue = queue.Queue()
    visited = set()
    cnt = 0

    r = None
    url = ''
    soup = None;

    def getContent(self, url):
        print('正在采集第' + str(self.cnt) + '个网址:' + url)
        try:
            self.r = requests.get(url)
        except:
            return False;

        self.setEncode()
        self.soup = bs(self.r.text, 'html.parser')
        self.visited |= {url}

    def setEncode(self):
        encodings = requests.utils.get_encodings_from_content(self.r.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = 'utf-8'
        self.r.encoding = encoding

    def getLinks(self):
        links = self.soup.find_all('a')
        return links;

    def addLinkToQueue(self):
        print('正在获取连接地址...')
        links = self.getLinks();

        for link in links:
            href = link.get('href');
            if href is None or href in self.visited:
                continue;

            if 'repian.com' in href:
                self.urlQueue.put(href)

    def getLinkFromQueue(self):
        print('正在从队列获取网址...')
        self.cnt += 1
        return self.urlQueue.get();

    def start(self, tNum):
        print('线程:' + str(tNum) + '启动')
        while True:

            getUrl = self.getLinkFromQueue();
            self.getContent(getUrl)
            self.addLinkToQueue()

    def main(self, url):
        self.getContent(url);
        self.addLinkToQueue();

        for i in range(30):
            Thread(target=self.start, args={i, }).start()

s = Spider()
url = 'http://www.repian.com'
s.main(url)
