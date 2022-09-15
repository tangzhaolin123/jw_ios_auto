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
class JiWei:
    @classmethod
    def jwt_01(cls, c, video_camera_name):  # 手机成功登录
        c.session('com.co.Yoosee')  # 打开app
        c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
        c(type='XCUIElementTypeTextField').set_text("13016129715")  # 输入手机号
        c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
        c(name="登录").click()  # 点击登录按钮
        c(name="同意并继续").click()  # 同意隐私协议
        c(name="以后").click()
        sleep(2)
        c.screenshot().save("screen.png")#截图登录进来的界面
        c(name="我的").click()
        c(name="我的头像").click()
        c(name="退出登录").click()
        sleep(3)
        c.session().app_terminate('com.co.Yoosee')  # 关闭app

    @classmethod
    def jwt_02(cls, c, video_camera_name):  # 查看yooseeID
        c.session('com.co.Yoosee')  # 打开app
        c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
        c(type='XCUIElementTypeTextField').set_text("karinzl@163.com")  # 输入手机号
        c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
        c(name="登录").click()
        c(name="同意并继续").click()
        c(name="以后").click()
        c(name="我的").click()
        c(type="XCUIElementTypeStaticText").click()
        if c(enabled="true").exists:
            c(name="退出登录").click()
        else:
            assert c.screenshot().save("error.png")#没有yooseeID的话就截图报错
        sleep(3)
        c.session().app_terminate('com.co.Yoosee')  # 关闭app
    @classmethod
    def jwt_03(cls, c, video_camera_name):  # 周云婷登录判断是否有设备
        c.session('com.co.Yoosee')  # 打开app
        c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
        c(type='XCUIElementTypeTextField').set_text("karinzl@163.com")  # 输入手机号
        c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
        c(name="登录").click()
        c(name="同意并继续").click()
        c(name="以后").click()
        # 如果有添加设备按钮则截图退出
        if c(name="添加设备入口").exists:
            sleep(2)
            c.screenshot().save("JiWEi.png")
            c(name="我的").click()
            c(name="我的头像").click()
            c(name="退出登录").click()
        # 有设备的话直接退出
        else:
            assert c(type="XCUIElementTypeStaticText").exists
            c(name="我的").click()
            c(name="我的头像").click()
            c(name="退出登录").click()
        sleep(3)
        c.session().app_terminate('com.co.Yoosee')  # 关闭app

    @classmethod
    def jwt_07(cls, c, video_camera_name):  # 周云婷微信登录判断无设备（已登录微信号）
        c.session('com.co.Yoosee')
        c(name="微信").click()
        c(name="同意并继续").click()
        # 没有设备的话退出账号
        if c(type="XCUIElementTypeButton").exists:
            sleep(2)
            c.screenshot().save("JiWEi1.png")
            c(name="我的").click()
            c(type="XCUIElementTypeStaticText").click()
            c(name="退出登录").click()
        # 有设备的话直接退出
        else:
            assert c(type="XCUIElementTypeStaticText").exists
            c(name="我的").click()
            c(name="我的头像").click()
            c(name="退出登录").click()
        sleep(3)
        c.session().app_terminate('com.co.Yoosee')  # 关闭app
    @classmethod
    def jwt_08(cls, c, video_camera_name):  # 周云婷微信登录查看yooseeID
        c.session('com.co.Yoosee')
        c(name="微信").click()
        c(name="同意并继续").click()
        c(name="我的").click()
        c(type="XCUIElementTypeStaticText").click()
        if c(type="XCUIElementTypeImage").exists:
            c.screenshot().save("image.png")
            c(name="退出登录").click()
        else:
            assert c.screenshot().save("error.png")  # 没有头像的话就报错截图
        sleep(3)
        c.session().app_terminate('com.co.Yoosee')  # 关闭app
