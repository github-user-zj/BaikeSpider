#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'HTML下载器'
__author__ = 'zhangjun'
__mtime__ = '2017/3/19'
   
"""
# import urllib2
# import requests
from ..download.html_request import request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        # response = urllib2.urlopen(url)
        response = request.get(url=url, timeout=2)
        if response.status_code !=200:
            return None
        return response.content
