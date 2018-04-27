'''

@author: KaueBonfim
'''
import os
import sys
import threading
import socket
import time


def irDiretorio(diretorio):
    diretorio=str(diretorio).replace("\\", "/")
    os.chdir(diretorio)

def criarPasta(nomePasta):
    os.mkdir('./'+nomePasta)

def abrirPrograma(programa):
    programa=str(programa).replace("\\", "/")
    return os.startfile(programa)

def terminal_parametro():
    return sys.argv
    

def execute(command):
    os.system(command)
            
def transmissao_server(host:str,port:int,diretorio:str):
    diretorio=str(diretorio).replace("\\", "/")
    os.chdir(diretorio)
    s = socket.socket()
    s.bind((host,port))
    s.listen(4)
    c=None
    
    while True:
        if c is None:            
            c,addr =s.accept() 
            endereco=addr           
        else:
            try:
                menssagem=c.recv(1024).decode()
                print(menssagem)
                
                os.system(menssagem)
                
                q = "OK"
                c.send(q.encode())
                c=None
            except:
                continue
            
def transmissao_cliente(host:str,port:int, command:str):
    s=socket.socket()
    s.connect((host,port))
    s.send(str(command).encode())
    print(s.recv(1024))

def dia_mes_ano():
    line=time.localtime()
    line=list(line)
    lis=[]
    for h in line:
        lis.append(h)
        if(line.index(h) == 2):
            break
    return lis

def caminho_anterior():
    return str(os.path.dirname(os.getcwd())).replace("\\", "/")

def path_atual():
    return str(os.getcwd()).replace("\\", "/")