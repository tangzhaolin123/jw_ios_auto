#coding:utf-8
'''from tidevice import Device
from tidevice._relay import relay
d = Device("f79f89bb4bf781b7230138e45f1744718981dbea")
relay(d, 8100, 8100, debug=True)'''
import os


os.system('tidevice relay 8100 8100')

