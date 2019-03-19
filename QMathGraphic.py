from PyQt5 import QtWidgets ,QtCore, QtGui
import sys



class QMathGraphic(QtWidgets.QWidget):
  
    def __init__(self,w):      
        super().__init__(w)
        self.xDiv=10
        self.yDiv=10
        self.numberOfPoints=20
        self.xMinValue=0
        self.yMinValue=-1
        self.xMaxValue=100
        self.yMaxValue=1
        
        self.Cy=(self.yMaxValue-self.yMinValue)/self.yDiv
        self.Cx=(self.xMaxValue-self.xMinValue)/self.xDiv
        
        self.leftOfset = 25
        self.bottomOfset = 20

        self.xValues=[]
        self.yValues=[]
        self.setList()

    def addPoint(self,x,y):
        self.xValues.append(x)
        self.xValues=self.xValues[1:]
        self.yValues.append(y)
        self.yValues = self.yValues[1:]
        self.repaint()

    def addYValue(self, y):
        print("y este: ",y)
        self.yValues.append(y)
        self.yValues = self.yValues[1:]
        self.repaint()
        print(self.yValues)
        
    def setList(self):
        self.xValues=[]
        self.yValues=[]
        self.xValues.append(0)
        self.yValues.append(0)
        for i in range(1,self.numberOfPoints):
            self.xValues.append(self.xValues[i-1]+(self.xMaxValue-self.xMinValue)/self.numberOfPoints)
            self.yValues.append(0)
        print(self.xValues)
        print(self.yValues)

    def setNumberOfDivisions(self, x,y):
        self.xDiv=x
        self.yDiv=y
        self.Cy=(self.yMaxValue-self.yMinValue)/self.yDiv
        self.Cx=(self.xMaxValue-self.xMinValue)/self.xDiv
        self.repaint()

    def setNumberOfPoint(self ,n):
        self.numberOfPoints=n
        self.setList()

    def setAxisLimit(self,xMin,xMax,yMin,yMax):
        self.xMinValue=xMin
        self.yMinValue=-yMin
        self.xMaxValue=xMax
        self.yMaxValue=yMax
        self.Cy=(self.yMaxValue-self.yMinValue)/self.yDiv
        self.Cx=(self.xMaxValue-self.xMinValue)/self.xDiv
        self.repaint()

    def paintEvent(self, e):
      
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
      
    def drawWidget(self, qp):
        height = self.frameGeometry().height()-self.bottomOfset-1
        width = self.frameGeometry().width()-self.leftOfset
        xkp=width/(self.xMaxValue-self.xMinValue)
        ykp=height/(self.yMaxValue-self.yMinValue)
        #print(width, " ", height)
            
        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(self.leftOfset ,0 , width-1 , height)
        for i in range(1,self.xDiv):
            qp.drawLine(self.leftOfset+i*width/self.xDiv ,0 ,self.leftOfset+i*width/self.xDiv ,height )
            text = str(self.xMinValue+(i*self.Cx))
            if(len(text)>4):
                text=text[:4]
            qp.drawText(self.leftOfset+i*width/self.xDiv,height+(self.bottomOfset/2), text)
        for i in range(1, self.yDiv):
            qp.drawLine(self.leftOfset,i*height/self.yDiv ,width+self.leftOfset-1,i*height/self.yDiv )
            text=str(self.yMaxValue-(i*self.Cy))
            if(len(text)>4):
                text=text[:4]
            qp.drawText(0, i*height/self.yDiv, text)

    
        pen2 = QtGui.QPen(QtGui.QColor(50, 50, 175), 2, QtCore.Qt.SolidLine)
        qp.setPen(pen2)
        qp.setBrush(QtGui.QColor(255, 175, 175))

        for i in range(1,self.numberOfPoints):
            qp.drawLine(self.xValues[i-1]*xkp+self.leftOfset,(self.yMaxValue-self.yValues[i-1])*ykp,self.xValues[i]*xkp+self.leftOfset,(self.yMaxValue-self.yValues[i])*ykp)
        print("Number of point is:",self.numberOfPoints)

                    
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    wid=QtWidgets.QWidget()
    l=QtWidgets.QHBoxLayout()
    wi = QMathGraphic(wid)
    
    l.addWidget(wi)
    wid.setLayout(l)
    wid.show()
    wi.addYValue(0.5)
    wi.addYValue(0.25)
    sys.exit(app.exec_())
