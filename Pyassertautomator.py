'''

@author: KaueBonfim
'''

import pyautogui
from  assertpy import assert_that


def verifica_tela(path_imagem:str)->bool:
    if(pyautogui.locateOnScreen(image=path_imagem)):
        return True
    else:
        return False
    
def verifica_valor(valor,comparado)->bool:
    try:
        assert_that(valor).is_equal_to(comparado)
        return True
    except:
        return False

