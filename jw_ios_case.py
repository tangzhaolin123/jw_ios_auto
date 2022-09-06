#-*- coding:utf-8 -*-
from time import sleep
import os
import re
from PIL import Image,ImageStat
import math
import operator
from functools import reduce
import threading
import configparser
import cv2

#cfgpath = "ios_dbconf.ini"
#config = configparser.ConfigParser()
#config.read(cfgpath, encoding="gb2312")
#phone_num = config.get('sec1', '手机登录的号码')
#phone_pwd = config.get('sec1', '手机登录的密码')
class JiWei:
    @classmethod
    def jwt_01(cls, c, video_camera_name):  # 登录
        #with c.alert.watch_and_click(['提示', '取消']):
             #c(name="取消").click()
        c.session('com.co.Yoosee')
        sleep(5)
        a = c.app_current()
        #print (a)
        #print(c.alert.exists)
        if c.alert.watch_and_click(['提示', '取消']):
        #with c.alert.watch_and_click(['提示', '取消']):
             c(name="取消").click()
        #c.screenshot('screen.png')
        #c(name="取").click()
        # u.app_clear('com.yoosee')  # 清除应用数据
        # # u.watcher.stop()
        # SameOperation().app_go(u)
        # if u(text='用户服务协议和隐私政策概要').exists:
        #     u(resourceId='com.yoosee:id/tv_no').click(timeout=5)
        #     sleep(3)
        #     assert not u(text='登录').exists, '未进入登录界面'
        # else:
        #     assert u(text='用户服务协议和隐私政策概要').exists, '用户服务协议弹窗不存在'