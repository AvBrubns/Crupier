from os import error
import traceback
import re
import time
import sys

class Logs:
    def __init__(self):
        self.logPath='.\logs\logs.txt'
        self.errorpath = '.\logs\error.txt'
    def writeLog(self,text):
        try:
            f=open(self.logPath,'a',encoding='utf-8')
            f.write(text+'\n')
            print(text)
            f.close()
        except Exception as e:
            print("Error al escribir en el archivo de LOGS "+ str(e))
    def erroLogs(self,error):
        try:
            f=open(self.errorpath,'a',encoding='utf-8')
            f.write(error+'\n')
            print(error)
            f.close()
        except Exception as e:
            print("Error al escribir en el archivo de errores "+ str(e))
