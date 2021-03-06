#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/26 11:21
# @Author  : Nana Xing
# @File    : qrcode_demo.py
# @ProjectName: PythonDemo
# @Software : PyCharm
# @Description :
"""
qrcode支持中文数据，而myqr不支持中文等字符。
qrcode不能设置背景图，但是能将图片放在二维码中间。
myqr可以将背景设置为图片，并且允许为动态图。
"""
import os
import qrcode
import zxing
from MyQR import myqr
from PIL import Image


def first_demo():
    qr = qrcode.make('hello world')
    qr.get_image().show()


def second_demo():
    text = '啊，sa子'
    img = qrcode.make(text)
    img.save('qr.png')
    img.show()


def create_icon_qrcode():
    # version:二维码尺寸大小，box_size:二维码图片的大小，border:二维码白色边框的大小
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=2)
    qr.add_data('爱你哟，sa猪')
    qr.make(fit=True)
    img = qr.make_image(fill_color='grey', back_color='white')
    img_w, img_h = img.size

    # 设置icon的大小,为二维码图片大小的6分之一
    factor = 3
    size_w = img_w // factor
    size_h = img_h // factor

    icon = Image.open('hh.jpg')
    icon_w, icon_h = icon.size

    if icon_w>size_w:
        icon_w=size_w
    if icon_h>size_h:
        icon_h=size_h

    icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)

    w=(img_w-icon_w)//2
    h=(img_h-icon_h)//2

    img.paste(icon,(w,h),mask=None)
    img.save('ju.png')

def myqr_demo():
    words='sa zhu'
    version,level,qr_name=myqr.run(words=words,version=10,picture='hh.jpg',colorized=True,save_name='ju1.png',save_dir=os.getcwd())
    print(version,level,qr_name)


def parse_qrcode(filename):
    # 解析二维码
    reader=zxing.BarCodeReader()
    barcode=reader.decode(filename)
    print(barcode)


if __name__ == '__main__':
    myqr_demo()
