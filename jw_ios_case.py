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
             #c(name="取消").click()#
        c.session('com.co.Yoosee')
        sleep(5)
        a = c.app_current()
        print (a)
