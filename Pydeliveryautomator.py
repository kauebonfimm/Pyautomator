#*- coding: utf-8 -*-
import os
from jenkins import Jenkins
import jenkins


def conectar_jenkins(self,url,senha_user,nome_user):
    self.jenkins_server= Jenkins(url,nome_user, senha_user)
    
def construir_no_jenkins(self,nome):
    self.jenkins_server.build_job(nome)
    
def iniciar_repo(self,diretorio,nome,email):
    try:
        os.chdir(diretorio)
        os.system("git init")
        os.system('git config --global user.name %s'% nome)
        os.system('git config --global user.email "%s"'% email)
    except:
        print("Repositorio j� foi iniciado, ou n�o existe")
    

def add_repo(self,pasta="*"):
    for list in pasta:
        os.system("git add %s" % list)
    
def commit(self,menssagem):
    os.system('git commit -m "%s"'% menssagem)

def enviar_github(self,url):
    os.system("git remote add origem %s"% url)
    os.system("git push -f origem master")

def proxy_git(self,url):
    os.system('git config --global %s'% url)
    
