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
import cv2
#213313213331
class SameOperation:
    def quit_app(self,c):
        sleep(1)
        c.home()
        sleep(1)
        c.session().app_terminate('com.co.Yoosee')
class JiWei:
    class JiWei:
        @classmethod
        def jwt_01(cls, c, video_camera_name):  # 周手机成功登录
            c.session('com.co.Yoosee')  # 打开app
            sleep(5)
            c(name="登录").wait(timeout=5.0)
            if c(name="登录").exists:  # 判断是否是登录状态，如果登录存在的话就进行登录操作
                c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
                c(type='XCUIElementTypeTextField').set_text("13016129715")  # 输入手机号
                c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
                c(name="登录").click()  # 点击登录按钮
                c(name="同意并继续").click()  # 同意隐私协议
                c(name="以后").click()
            else:  # 没有登录元素就是为登录状态，先进行退出操作
                c(name="我的").click()
                c(name="我的头像").click()
                c(name="退出登录").click()
                c.session('com.co.Yoosee')
                c(name="登录").wait(timeout=5.0)
                c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
                c(type='XCUIElementTypeTextField').set_text("13016129715")  # 输入手机号
                c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
                c(name="登录").click()  # 点击登录按钮
                c(name="同意并继续").click()  # 同意隐私协议
                c(name="以后").click()
            assert c(name="首页导航添加按钮").wait(timeout=5.0)  # 如果有该元素则登录成功
            c.session().app_terminate('com.co.Yoosee')  # 关闭app

        @classmethod
        def jwt_02(cls, c, video_camera_name):  # 查看yooseeID
            c.session('com.co.Yoosee')  # 打开app
            sleep(5)
            c(name="登录").wait(timeout=5.0)
            if c(name="登录").exists:
                c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
                c(type='XCUIElementTypeTextField').set_text("13016129715")  # 输入手机号
                c(type='XCUIElementTypeTextField').set_text("karinzl@163.com")  # 输入手机号
                c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
                c(name="登录").click()  # 点击登录按钮
                c(name="同意并继续").click()  # 同意隐私协议
                c(name="登录").click()
                c(name="同意并继续").click()
                c(name="以后").click()
                assert c(enabled="true").wait(timeout=5.0)
            else:
                assert c(enabled="true").wait(timeout=5.0)
            c(name="我的").click()
            c(name="我的头像").click()
            c(name="退出登录").click()
            sleep(3)
            c.session().app_terminate('com.co.Yoosee')  # 关闭app

        @classmethod
        def jwt_03(cls, c, video_camera_name):  # 登录判断是否有设备
            c.session('com.co.Yoosee')  # 打开app
            sleep(5)
            c(name="登录").wait(timeout=5.0)
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
        def jwt_07(cls, c, video_camera_name):  # 微信登录判断无设备（已登录微信号）
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
    def jwt_08(cls, c, video_camera_name):  # 微信登录查看yooseeID（前提是微信登录的状态）
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

    @classmethod
    def jwt_13(cls, c, video_camera_name):  # 手机成功登录
        c.session('com.co.Yoosee')  # 打开app
        sleep(5)
        if c(name="登录").exists:
            c(name="登录").wait(timeout=5.0)
            c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
            c(type='XCUIElementTypeTextField').set_text("13016129715")  # 输入手机号
            c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
            c(name="登录").click()  # 点击登录按钮
            c(name="同意并继续").click()  # 同意隐私协议
            c(name="以后").click()
        else:
            assert c(name="添加设备入口").wait(timeout=5.0)

    def jwt_08(cls, c, video_camera_name):  # 微信登录查看yooseeID
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

    @classmethod
    def jwt_14(cls, c, video_camera_name):  # 邮箱登录
        c.session('com.co.Yoosee')  # 打开app
        sleep(5)
        if c(name="登录").exists:
            c(name="登录").wait(timeout=5.0)
            c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
            c(type='XCUIElementTypeTextField').set_text("karinzl@163.com")  # 输入邮箱号
            c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
            c(name="登录").click()  # 点击登录按钮
            c(name="同意并继续").click()  # 同意隐私协议
            c(name="以后").click()
        else:
            assert c(name="添加设备入口").wait(timeout=5.0)
            c.session().app_terminate('com.co.Yoosee')  # 关闭app

    @classmethod
    def jwt_15(cls, c, video_camera_name):  # 退出
        c.session('com.co.Yoosee')  # 打开app
        sleep(5)
        if c(name="登录").exists:
            c(name="登录").wait(timeout=5.0)
            c(type='XCUIElementTypeTextField').clear_text()  # 清除当前账号
            c(type='XCUIElementTypeTextField').set_text("karinzl@163.com")  # 输入邮箱
            c(type='XCUIElementTypeSecureTextField').set_text("qwe12345")  # 输入正确密码
            c(name="登录").click()  # 点击登录按钮
            c(name="同意并继续").click()  # 同意隐私协议
            c(name="以后").click()
        else:  # 不是登录状态的话就退出
            c(name="我的").click()
            c(name="我的头像").click()
            c(name="退出登录").click()
            assert c(name="登录").wait(timeout=5.0)  # 检查是否是退出状态
            c.session().app_terminate('com.co.Yoosee')  # 关闭app

    @classmethod
    def jwt_16(cls, c, video_camera_name):
        c.session('com.co.Yoosee')  # 打开app
        sleep(5)
        assert c(type="XCUIElementTypeImage").wait(timeout=5.0)  # 检查是否有广告页
        c.session().app_terminate('com.co.Yoosee')  # 关闭app

    @classmethod
    def jwt_18(cls, c, video_camera_name):
        c.session('com.co.Yoosee')  # 打开app
        if c(type="XCUIElementTypeImage").exists:
            sleep(10)
        assert c(name="设备").wait(timeout=5.0)  # 检查广告是否跳过进入列表页面
        c.session().app_terminate('com.co.Yoosee')  # 关闭app

    @classmethod
    def jwt_20(cls, c, video_camera_name):
        c.session().app_terminate('com.co.Yoosee')
        c.session('com.co.Yoosee')  # 打开app
        sleep(2)
        if c(name="跳过").exists:
            c(name="跳过").click()
            c(type="XCUIElementTypeCell").click()
            sleep(20)
        else:
            c(name="点击跳过 | 4s").click()
            sleep(2)
            c(type="XCUIElementTypeCell").click()
            sleep(20)
        assert c(type="XCUIElementTypeStaticText").wait(timeout=5.0)  # 查看监控页面是否有错误状态码
        c.session().app_terminate('com.co.Yoosee')

    @classmethod
    def jwt_22(cls, c, video_camera_name):
        c.session('com.co.Yoosee')
        sleep(5)
        c(name="跳过").wait(timeout=5.0)
        assert c(type="XCUIElementTypeImage").wait(timeout=5.0)  # 查看是否有banner广告
        c.session().app_terminate('com.co.Yoosee')
