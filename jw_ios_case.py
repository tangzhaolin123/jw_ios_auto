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

class SameOperation:
    def quit_app(self,c):
        sleep(1)
        c.home()
        sleep(1)
        c.session().app_terminate('com.co.Yoosee')


class JiWei:
    # 登录 判断是否有设备
    @classmethod
    def jwt_01(cls, c, video_camera_name):  # 登录
        c.session('com.co.Yoosee')  # 打开app   ！打开APP后，有等待一段时间，可以用强制等待sleep或显性等待wait
        c(type='XCUIElementTypeTextField').clear_text()  # 清除账号
        c(type='XCUIElementTypeTextField').set_text("1755354468@qq.com")  # 填写账号
        c(type='XCUIElementTypeSecureTextField').set_text("zx123456")  # 填写密码
        c(name="登录").click()  # 点击登录按钮
        c(name="同意并继续").click()  # 同意隐私协议
        c(name="以后").click()
        sleep(4)
        assert c(name="添加设备") # 判断设备列表是否有设备  ！不要用if,用assert 断言判断，若c(name="添加新设备")不存在即报错就行了，框架自会恢复执行
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


    @classmethod
    def jwt_02(cls, c, video_camera_name):  # 登录
        sleep(3)
        print ('第2条用例')

    @classmethod
    def jwt_03(cls, c, video_camera_name):  # 登录
        sleep(3)
        print('第3条用例')



    @classmethod
    def jwt_01(cls, c, video_camera_name):  # 周手机成功登录
            c.session('com.co.Yoosee')  # 打开app
            c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
            c(type='XCUIElementTypeTextField').set_text("13016129715")  # 输入手机号
            c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
            c(name="登录").click()  # 点击登录按钮
            c(name="同意并继续").click()  # 同意隐私协议
            c(name="以后").click()
            sleep(2)
            c.screenshot().save("screen.png")  # 截图登录进来的界面
            c(name="我的").click()
            c(name="我的头像").click()
            c(name="退出登录").click()
            sleep(3)
            c.session().app_terminate('com.co.Yoosee')  # 关闭app

    @classmethod
    def jwt_02(cls, c, video_camera_name):  # 周查看yooseeID
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
                assert c.screenshot().save("error.png")  # 没有yooseeID的话就截图报错
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
