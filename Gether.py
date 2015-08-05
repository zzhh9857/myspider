__author__ = 'dw'

import requests;


class Gather:
    def getContent(self, url):
        r = None;
        try:
            r = requests.get(url);
        except:
            r = None;
        r.encoding = self.setEncoding(r.text);
        return r.text;

    # 获取文字的编码
    def setEncoding(self, text):
        encodings = requests.utils.get_encodings_from_content(text);
        if encodings:
            encoding = encodings[0];
        else:
            encoding = 'utf-8';

        return encoding;
