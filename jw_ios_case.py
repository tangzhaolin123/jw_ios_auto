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
#wda.DEBUG = True


class JiWei:
    @classmethod
    def jwt_01(cls, c, video_camera_name):  # 登录
        c.session('com.co.Yoosee')  # 打开app   ！打开APP后，有等待一段时间，可以用强制等待sleep或显性等待wait
        c(type='XCUIElementTypeTextField').clear_text()  # 清除账号
        c(type='XCUIElementTypeTextField').set_text("1755354468@qq.com")  # 填写账号
        c(type='XCUIElementTypeSecureTextField').set_text("zx123456")  # 填写密码
        c(name="登录").click()  # 点击登录按钮
        c(name="同意并继续").click()  # 同意隐私协议
        c(name="以后").click()
        if c(name="添加新设备"):  # 判断设备列表是否有设备  ！不要用if,用assert 断言判断，若c(name="添加新设备")不存在即报错就行了，框架自会恢复执行
            c(name="我的").click()
            c(type="XCUIElementTypeImage").click()
            c(name="退出登录").click()
            sleep(5)
            c.close()
        else:
            c.close()
        '''
         #智慧生活登录
        # c.session('com.huawei.smarthome-ios')  # 打开app
        # c(name="登录").click()  # 点击登录按钮
        # c(name="密码登录").click() 
        # c(value="密码").click() #需点击输入框 不然输入法无法打开
        # c(value="密码").set_text("xz123456")  # 填写密码
        # c(name="登录").click() 

        '''
    @classmethod
    def jwt_02(cls, c, video_camera_name):  # 登录
        sleep(3)
        print ('第2条用例')

    @classmethod
    def jwt_03(cls, c, video_camera_name):  # 登录
        sleep(3)
        print('第3条用例')