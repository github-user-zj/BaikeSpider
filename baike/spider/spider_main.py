#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '爬虫总调度'
__author__ = 'zhangjun'
__mtime__ = '2017/3/18'
   
"""

from baike.spider import html_downloader
from baike.spider import html_outputer
from baike.spider import url_manager
from baike.spider import html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            print '成功'
            try:
                new_url = self.urls.get_new_url()
                print 'crawl %d : %s ' %(count,new_url)
                html_count = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_count)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count >= 100:
                    break
                count = count + 1

            except Exception,e:
                print 'crawl failed！！',e

        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
