#coding:utf-8
from tidevice import Device
d = Device("f79f89bb4bf781b7230138e45f1744718981dbea")
d.xctest("com.jiwei.WebDriverAgentRunner.xctrunner", target_bundle_id="f79f89bb4bf781b7230138e45f1744718981dbea")