#coding:utf-8

import configparser

cfgpath = "ios_dbconf.ini"
config = configparser.ConfigParser()
config.read(cfgpath, encoding="gb2312")
video_camera_name = config.get('sec1', '摄像头设备ID')
print (video_camera_name)