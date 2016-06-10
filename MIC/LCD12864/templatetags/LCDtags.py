# -*- coding:utf-8 -*-
from django import template

import re

register=template.Library()

'''生成行内好多列
'''
@register.filter(name='generate_rows')
def generate_rows(text):
    Datas = text.split()
    ReturnData = ''
    for data in Datas:
        ReturnData = ReturnData + '<td>' + data + '</td>'
    return ReturnData
