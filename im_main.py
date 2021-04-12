import sys
import os
import time
from PyQt5 import QtGui, QtWidgets
from main import Ui_MainWindow
from logs import Logs
from crupier1 import crupier1
import pathlib

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Jugar Dados")

        #elementos
        self.logs = Logs()
        self.c1 = crupier1(5000,2000)

        #init
        self.saldoJ.setText("Su saldo:"+str(self.c1.getSaldoJ()))
        self.saldoC.setText("Saldo Crupier:"+str(self.c1.getSaldoC()))
        self.input_num.setRange(1,6)
        #conexion
        self.play.clicked.connect(self.tirar)
        self.reset.clicked.connect(self.reiniciar)
    def tirar(self):
        try:
            if str.isnumeric(self.input_apuesta.text()):
                self.logs.writeLog("Se inicio el juego")
                apuesta = self.input_apuesta.text()
                num = self.input_num.value()
                self.logs.writeLog("El jugador aposto:"+apuesta)
                self.logs.writeLog("El jugador selecciono:"+str(num))
                if int(apuesta) <= self.c1.getSaldoJ() and int(apuesta)>0 :
                    numR = self.c1.getRandom()
                    self.logs.writeLog("El numero salio:"+str(numR))
                    self.num.setText(str(numR))
                    if num == numR:
                        self.info("XD ¡Ganastes!:"+apuesta,".\icons\happy.png")
                        self.logs.writeLog("El jugador gano:"+apuesta)
                        self.c1.setSaldoJ(apuesta,"+")
                        self.c1.setSaldoC(apuesta,"-")
                        self.actualizar()
                    elif  self.c1.isPar(num) and self.c1.isPar(numR):
                        self.info("¡Empate!",".\icons\poker.png")
                        self.logs.writeLog("Empate:")
                        self.actualizar()
                    else:
                        self.info(" :,( ¡Perdiste!:"+apuesta,".\icons\sad.png")
                        self.logs.writeLog("El jugador perdio:"+apuesta)
                        self.c1.setSaldoJ(apuesta,"-")
                        self.c1.setSaldoC(apuesta,"+")
                        self.actualizar()
                else:
                    self.info("Su saldo es insuficiente","icons\sad.png")
                    if self.c1.getSaldoJ() > 0:
                        pass
                    else:
                        self.bloquear(True)
            else:
                self.info("No a ingresado una apuesta valida","icons\poker.png")

        except Exception as e:
            self.logs.writeLog("Error al iniciar juego:"+str(e)+str(localtime)+"\t")            
    def reiniciar(self):
        c1 = crupier1(5000,2000)
        self.c1 = c1
        self.info("",".\icons\happy.png")
        self.saldoJ.setText("Su saldo:"+str(self.c1.getSaldoJ()))
        self.saldoC.setText("Saldo Crupier:"+str(self.c1.getSaldoC()))
        self.bloquear(False)
    def bloquear(self,bool):
        self.input_apuesta.setDisabled(bool)
        self.input_num.setDisabled(bool)
        self.play.setDisabled(bool)
    def info(self,text,path):
        self.msg.setText(text)
        self.pixmap=QtGui.QPixmap(path)
        self.icon.setPixmap(self.pixmap)
    
    def actualizar(self):
        self.saldoJ.setText("Su saldo:"+str(self.c1.getSaldoJ()))
        self.saldoC.setText("Saldo Crupier:"+str(self.c1.getSaldoC()))
    
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self,
                                     "Cerrando",
                                     "¿Desea cerrar la aplicacion?",
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            localtime = time.asctime( time.localtime(time.time()) )
            self.logs.writeLog("\tEl programa se cerro a las:"+str(localtime)+"\t")
            event.accept()

        else:
            event.ignore()

if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        logs = Logs()
        localtime = time.asctime( time.localtime(time.time()) )
        logs.writeLog("\tPrograma iniciado:"+str(localtime))
        window = MyApp()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)