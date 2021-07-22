import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import  Qt 
#from PyQt5.QtGui import QPen

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=2):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize+1, windowSize+1)
        self.pen = QtGui.QPen(QtGui.QColor("red"))                
        self.pen.setWidth(penWidth)                                            
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1))


    def paintEvent(self, event):
        ws = self.ws
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        #Set Pen to color Red with solid line
        #painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        #Draw Circle in middle of screen with width and height 2
        #painter.drawEllipse(int(ws/2),int(ws/2),2,2)
        painter.drawPoint(int(ws/2),int(ws/2))

app = QtWidgets.QApplication(sys.argv) 

widget = Crosshair(windowSize=24, penWidth=4)
widget.show()

sys.exit(app.exec_())
