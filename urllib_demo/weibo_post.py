#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/24 18:59
# @Author  : Nana Xing
# @Site    : 
# @File    : weibo_post.py
# @Software: PyCharm
from urllib import request,parse

print('登录 weibo.cn。。。。')
user = 1082
passwd = 'xnn123456'

login_data = parse.urlencode(
    [
        ('username', user),
        ('password', passwd),
         ('entry', 'mweibo'),
         ('client_id',''),
         ('savestate','1'),
         ('ec',''),
         ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ]
)

req = request.Request('https://login-daily.tuya-inc.cn:7799/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', f.read().decode('utf-8'))