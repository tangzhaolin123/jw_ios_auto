# -*- coding: utf-8 -*-
import os
import threading
from time import sleep


def doTask_1(case):
    e_1 = os.system(case)
    if e_1 == 1:
        sleep(3)
        doTask_1(case)

def main_1():
    case = 'ios_xctest.py'
    while True:
        try:
            doTask_1(case)
        except:
            sleep(10)
            continue

if __name__ == '__main__':


    main_1()
    # while True:
    #     # 保活
    #     sleep(10)