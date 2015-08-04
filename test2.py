# encoding=utf-8
__author__ = 'dw'
from pyquery import PyQuery as pq;
from collections import deque;
import threading;

d = pq(url='http://www.repian.com/', headers={});
# print(d('a').attr('href'));
links = d('.navBar a[target=_self]').make_links_absolute();

queue = deque();
visited = set();
cnt = 0;

for link in links:
    queue.append(link.attrib['href'])


def start():
    global cnt, visited;
    while queue:
        url = queue.popleft();
        try:
            d = pq(url=url);
        except:
            continue;
        finally:
            visited |= {url}

        print('已经抓取：' + str(cnt) + '   正在抓取<--- ' + url);
        print('title:' + d('title').text());
        cnt += 1;
        content = None;
        try:
            content = d('meta[http-equiv=Content-Type]').attr('content');
        except:
            continue;

        if content is not None and 'html' not in content:
            continue;

        links = d('a').make_links_absolute();
        for link in links:
            if 'repian.com' in link.attrib['href'] and link.attrib['href'] not in visited:
                queue.append(link.attrib['href']);
                # print('加入队列---> ' + link.attrib['href'])

threads = [];
t1 = threading.Thread(target=start)
t2 = threading.Thread(target=start)
t3 = threading.Thread(target=start)
t4 = threading.Thread(target=start)
t5 = threading.Thread(target=start)
# t6 = threading.Thread(target=start)
# t7 = threading.Thread(target=start)
# t8 = threading.Thread(target=start)
# t9 = threading.Thread(target=start)
# t10 = threading.Thread(target=start)
threads.append(t1);
threads.append(t2);
threads.append(t3);
threads.append(t4);
threads.append(t5);
# threads.append(t6);
# threads.append(t7);
# threads.append(t8);
# threads.append(t9);
# threads.append(t10);

for thread in threads:
    thread.start();