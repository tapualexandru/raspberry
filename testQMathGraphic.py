from PyQt5 import QtWidgets ,QtCore
from QMathGraphic import QMathGraphic
import sys, os, psutil, threading, time


class runC(QtCore.QObject):
    updateGraphicEvent = QtCore.pyqtSignal(float)
    
    def __init__(self):
        super(runC, self).__init__()
        app = QtWidgets.QApplication(sys.argv)
        wid=QtWidgets.QWidget()
        wi = QMathGraphic(wid)
        
        l=QtWidgets.QHBoxLayout()
        self.updateGraphicEvent.connect(wi.addYValue)
        
        #wi.numberOfPoints=100
        wi.setAxisLimit(0,100,0,100)
        wi.setNumberOfDivisions(10,10)
        wi.setNumberOfPoint(200)
        t = threading.Thread(target=self.worker)
        t.start()
        l.addWidget(wi)
        wid.setLayout(l)
        wid.resize(500,500)
        wid.show()
        #print(psutil.cpu_percent())
        sys.exit(app.exec_())

    def worker(self):
        while True:
            x=psutil.cpu_percent()
            print(x)
            self.updateGraphicEvent.emit(float(x))
            time.sleep(0.5)



    
   

x=runC()
