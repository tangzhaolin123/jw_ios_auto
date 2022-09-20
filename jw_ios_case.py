# -*- coding:utf-8 -*-
from time import sleep
import wda
import os
import re
from PIL import Image, ImageStat
import math
import operator
from functools import reduce
import threading
import configparser

# import cv2

# cfgpath = "ios_dbconf.ini"
# config = configparser.ConfigParser()
# config.read(cfgpath, encoding="gb2312")
# phone_num = config.get('sec1', '手机登录的号码')
# phone_pwd = config.get('sec1', '手机登录的密码')
wda.DEBUG = True


class JiWei:
    # 登录 判断是否有设备
    @classmethod
    def jwt_01(cls, c, video_camera_name):
        c.session('com.co.Yoosee')  # 打开app
        c(type='XCUIElementTypeTextField').clear_text()  # 清除账号
        c(type='XCUIElementTypeTextField').set_text("1755354468@qq.com")  # 填写账号
        c(type='XCUIElementTypeSecureTextField').set_text("zx123456")  # 填写密码
        c(name="登录").click()  # 点击登录按钮
        c(name="同意并继续").click()  # 同意隐私协议
        c(name="以后").click()
        sleep(4)
        assert c(name="添加设备")#判断是否有添加设备按钮
        sleep(2)
        assert c(name="添加设备")
        c(xpath='//XCUIElementTypeButton[@name="我的"]').click()
        c(xpath='//XCUIElementTypeImage[@name="我的头像"]').click()
        c(name="退出登录").click()
    # 循环登录10次
    @classmethod
    def jwt_02(cls, c, video_camera_name):  # 登录
        for i in range(10):
            c.session('com.co.Yoosee')  # 打开app
            c(type='XCUIElementTypeTextField').clear_text()  # 清除账号
            c(type='XCUIElementTypeTextField').set_text("1755354468@qq.com")  # 填写账号
            c(type='XCUIElementTypeSecureTextField').set_text("zx123456")  # 填写密码
            c(name="登录").click()  # 点击登录按钮
            c(name="同意并继续").click()  # 同意隐私协议
            c(name="以后").click()
            sleep(2)
            assert c(name="添加设备")
            c(xpath='//XCUIElementTypeButton[@name="我的"]').click()
            c(xpath='//XCUIElementTypeImage[@name="我的头像"]').click()
            c(name="退出登录").click()
            sleep(2)
            c.close()
    #循环点击监控10次
    @classmethod
    def jwt_03(cls,c,video_camera_name):
        c.session('com.co.Yoosee')  # 打开app
        c(type='XCUIElementTypeTextField').clear_text()  # 清除账号
        c(type='XCUIElementTypeTextField').set_text("17633853458")  # 填写账号
        c(type='XCUIElementTypeSecureTextField').set_text("xz123456")  # 填写密码
        c(name="登录").click()  # 点击登录按钮
        c(name="同意并继续").click()  # 同意隐私协议
        c(name="以后").click()
        sleep(2)
        for i in range(10):# 循环执行10次
            c(type='XCUIElementTypeCell',index=2).click() # 通过index定位需要点击的设备窗口
            sleep(10)#
            c(type='XCUIElementTypeButton',name="iot back").click()# 通过name属性定位返回按钮 需要注意报警消息弹窗
            sleep(5)
        else:
            c.close()
