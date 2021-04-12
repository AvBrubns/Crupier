from math import trunc
import random
class crupier1:
    def __init__(self,saldoc,saldoj):
        self.saldoJ = saldoj
        self.saldoC = saldoc

    def getSaldoC(self):
        return self.saldoC

    def getSaldoJ(self):
        return self.saldoJ

    def setSaldoC(self,res,option):
        res = int(res)
        if option == "+":
            self.saldoC = self.saldoC + res 
        else:
            self.saldoC = self.saldoC - res 
        

    def setSaldoJ(self,res,option):
        res = int(res)
        if option == "+":
            self.saldoJ = self.saldoJ + res 
        else:
            self.saldoJ = self.saldoJ - res

    def getRandom(self):
        r = random.randint(1,6)
        return r

    def isPar(self, num):
        result = num/2
        r = str(result)
        if int(r[2])==0:
            return True
        else:
            return False
        