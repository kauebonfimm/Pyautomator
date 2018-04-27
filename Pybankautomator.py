import MySQLdb
import cx_Oracle


class PyDatas():
    
    def __init__(self,Servidor,user=None,senha=None,banco=None,endereco=None,porta=None):
        if (Servidor=="MySQL"):
            self.__bank=MySQLdb.connect(user=user,passwd=senha,db=banco,host=endereco,port=porta,autocommit=True)
            self.cursor=self.__bank.cursor()
        elif (Servidor=="Oracle"):
            self.__bank=cx_Oracle.connect('{}/{}@{}{}'.format(user,senha,endereco,porta))
            self.cursor=self.__bank.cursor()
        
        
    def buscar(self,query:str):
        self.cursor.execute(query)
        return self.cursor.fetchall()