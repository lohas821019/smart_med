# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:46:34 2022

@author: Jason
"""

import serial
import time
import numpy as np 

COM_PORT = 'COM4'
baudRate = 115200
ser = serial.Serial(COM_PORT, baudRate, timeout=0.5)

try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        choice = input('請輸入模式 0 ~ 16\n').lower()
        
        if choice == 'q':
            break

        elif (int(choice) < 17):
            # print(int(choice))
            choice = np.array(choice).tobytes()
            ser.write(choice)            # 訊息必須是位元組類型
            ser.flush()
            time.sleep(0.5)

        while ser.in_waiting:
            mcu_feedback = ser.readline()
            mcu_feedback = mcu_feedback.decode("utf-8") # 接收回應訊息並解碼
            mcu_feedback = mcu_feedback.strip()
            print('控制板回應：', mcu_feedback)
            time.sleep(0.1)

        # while ser.in_waiting:
        #     sys.stdout.write(ser.readline())
        #     sys.stdout.flush()

finally:
    ser.close()
    print('再見！')