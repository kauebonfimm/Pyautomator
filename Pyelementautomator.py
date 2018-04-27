'''

@author: KaueBonfim
'''
import os


class Pyelement():
    
    def fechar_programa(self):
        self.driver.close()
        try:
            os.system("TASKKILL /IM Winium.Desktop.Driver.exe")
        except:
            try:
                os.system("TASKKILL /IM Appium.exe")
            except: 
                pass
            
 
    def escreve(self,elemento,conteudo,tipo=None):
        if(tipo == 'id'):           
            element=self.driver.find_element_by_id(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo == 'name'):
            element=self.driver.find_element_by_name(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo == 'class'):            
            element=self.driver.find_element_by_class_name(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo == 'xpath'):            
            element=self.driver.find_element_by_xpath(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo == 'link'):            
            element=self.driver.find_element_by_link_text(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo == 'tag'):            
            element=self.driver.find_element_by_tag_name(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo == 'text'):            
            element=self.driver.find_element_by_partial_link_text(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo == 'css'):            
            element=self.driver.find_element_by_css_selector(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo=='binding'):
            element=self.driver.find_element_by_binding(elemento)
            element.send_keys(conteudo)
            return element
        elif(tipo=='model'):
            element=self.driver.find_element_by_model(elemento)
            element.send_keys(conteudo)
            return element
        else:
            print('nenhum elemento foi especificado')

    def clica(self,elemento,tipo=None):
        
        if(tipo == 'id'):
            self.driver.find_element_by_id(elemento).click()
        elif(tipo == 'name'):
            self.driver.find_element_by_name(elemento).click()
        elif(tipo == 'class'):            
            self.driver.find_element_by_class_name(elemento).click()
        elif(tipo == 'xpath'):            
            self.driver.find_element_by_xpath(elemento).click()
        elif(tipo == 'link'):            
            self.driver.find_element_by_link_text(elemento).click()
        elif(tipo == 'tag'):            
            self.driver.find_element_by_tag_name(elemento).click()
        elif(tipo == 'css'):            
            self.driver.find_element_by_css_selector(elemento).click()
        elif(tipo == 'text'):            
            self.driver.find_element_by_partial_link_text(elemento).click()
        elif(tipo=='binding'):
            self.driver.find_element_by_binding(elemento).click()
        elif(tipo=='model'):
            self.driver.find_element_by_model(elemento).click()
        else:
            print('nenhum elemento foi especificado')
             
    
    def pegar_texto(self,elemento,tipo):
        if(tipo == 'id'):
            return self.driver.find_element_by_id(elemento).text
        elif(tipo == 'name'):
            return self.driver.find_element_by_name(elemento).text
        elif(tipo == 'class'):            
            return self.driver.find_element_by_class_name(elemento).text
        elif(tipo == 'xpath'):            
            return self.driver.find_element_by_xpath(elemento).text
        elif(tipo == 'link'):            
            return self.driver.find_element_by_link_text(elemento).text
        elif(tipo == 'tag'):            
            return self.driver.find_element_by_tag_name(elemento).text
        elif(tipo == 'css'):            
            return self.driver.find_element_by_css_selector(elemento).text
        elif(tipo == 'text'):            
            return self.driver.find_element_by_partial_link_text(elemento).text
        elif(tipo=='binding'):
            return self.driver.find_element_by_binding(elemento).text
        elif(tipo=='model'):
            return self.driver.find_element_by_model(elemento).text
        else:
            print('nenhum elemento foi especificado')
            
    def confirmar(self):
        try:
            self.submit()
        except:
            print('Nenhum elemento foi encontrado')        