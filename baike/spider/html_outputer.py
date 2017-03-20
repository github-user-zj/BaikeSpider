#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '输出器'
__author__ = 'zhangjun'
__mtime__ = '2017/3/19'
   
"""

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)


    def output_html(self):
        fout = open('output.html','w')

        fout.write('<html><head><meta charset="UTF-8"></head><body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s<td>' % data['url'])
            fout.write('<td>%s<td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s<td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body></html>')
        fout.close()