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
    @classmethod
    def jwt_01(cls, c, video_camera_name):  # 登录
        c.session('com.co.Yoosee')  # 打开app
        c(type='XCUIElementTypeTextField').clear_text()  # 清除账号
        c(type='XCUIElementTypeTextField').set_text("1755354468@qq.com")  # 填写账号
        c(type='XCUIElementTypeSecureTextField').set_text("zx123456")  # 填写密码
        c(name="登录").click()  # 点击登录按钮
        c(name="同意并继续").click()  # 同意隐私协议
        c(name="以后").click()
        if c(name="添加新设备"):  # 判断设备列表是否有设备
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

        # a = c.app_current()
        # #print (a)
        # #print(c.alert.exists)
        # if c.alert.watch_and_click(['提示', '取消']):
        # #with c.alert.watch_and_click(['提示', '取消']):
        #      c(name="取消").click()
        # #c.screenshot('screen.png')
        # #c(name="取").click()
        # # u.app_clear('com.yoosee')  # 清除应用数据
        # # # u.watcher.stop()
        # # SameOperation().app_go(u)
        # # if u(text='用户服务协议和隐私政策概要').exists:
        # #     u(resourceId='com.yoosee:id/tv_no').click(timeout=5)
        # #     sleep(3)
        # #     assert not u(text='登录').exists, '未进入登录界面'
        # # else:
        # #     assert u(text='用户服务协议和隐私政策概要').exists, '用户服务协议弹窗不存在'