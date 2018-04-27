'''

@author: KaueBonfim
'''
import os 
from appium import webdriver as mob
from Pyelementautomator import Pyelement
import time
import pyautogui
import PykeyMouseautomator

class Mobile(Pyelement,PykeyMouseautomator):
    def __init__(self,caminho_driver,dicionario_caps):
        self.driver
        
        os.chdir(caminho_driver+"Appium.lnk")
        while True:
            if pyautogui.locateOnScreen(image=caminho_driver+"/Appium.png"):
                pyautogui.press('enter')
                break
        time.sleep(2)
        desired_caps = {}
        desired_caps=dicionario_caps
        self.driver= mob.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)       