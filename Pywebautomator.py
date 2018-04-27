'''

@author: KaueBonfim
'''
import os 
from pytractor import webdriver as web
from selenium import webdriver
from Pyelementautomator import Pyelement
from PykeyMouseautomator import Pykeymouseautomator


class Web(Pyelement,Pykeymouseautomator):
    def __init__(self,driver,path_driver):
        if(driver == 'Chrome'):
            self.driver=webdriver.Chrome(path_driver+"chromedriver.exe")
            
            
        elif(driver == 'Firefox'):            
            self.driver=webdriver.Firefox(path_driver+"geckodriver.exe")
            
            
        elif(driver == 'Ie'):             
            self.driver=webdriver.Ie(path_driver+"IEDriverServer.exe")
                    
         
    def url_atual(self):
        return self.driver.current_url
    
    def pagina(self,url):
        self.driver.get(url)
        
    def maximiza(self):
        self.driver.maximize_window()
        
    def atualizar(self):
        self.driver.refresh()
        
    def voltar(self):
        self.driver.back()
    
    def limpar(self):
        self.driver.clear()
        
    def pegar_atributo(self,info):
        self.driver.get_attribute(info)
        
    def titulo(self):
        return self.driver.title
    
    def navegador(self):
        return self.driver.name