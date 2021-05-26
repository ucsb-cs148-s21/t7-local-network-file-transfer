# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import qrcode
import sys
  
# Image class for QR code
class Image(qrcode.image.base.BaseImage):
  
    # constructor
    def __init__(self, border, width, box_size):
  
        self.border = border
        self.width = width
        self.box_size = box_size
        size = (width + border * 2) * box_size
        self._image = QImage(size, size, QImage.Format_RGB16)
        self._image.fill(Qt.white)
  
    def pixmap(self):
        return QPixmap.fromImage(self._image)

    def drawrect(self, row, col):
        painter = QPainter(self._image)
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            QtCore.Qt.black)
  
  
# # Main Window class
# class Window(QMainWindow):
  
#     # constructor
#     def __init__(self):
#         QMainWindow.__init__(self)
  
#         # setting window title
#         self.setWindowTitle("QR Code")
  
#         # setting geometry
#         self.setGeometry(100, 100, 300, 300)
  
#         # creating a label to show the qr code
#         self.label = QLabel(self)
  
#         # creating a line edit to receive text
#         self.edit = QLineEdit(self)
  
#         # adding action when entered is pressed
#         self.edit.returnPressed.connect(self.handleTextEntered)
  
#         # setting font to the line edit
#         self.edit.setFont(QFont('Times', 9))
  
#         # setting alignment
#         self.edit.setAlignment(Qt.AlignCenter)
  
#         # creating a vertical layout
#         layout = QVBoxLayout(self)
  
#         # adding label to the layput
#         layout.addWidget(self.label)
  
#         # adding line edit to the layout
#         layout.addWidget(self.edit)
  
#         # creating a QWidget object
#         widget = QWidget()
  
#         # setting layout to the widget
#         widget.setLayout(layout)
  
#         # setting widget as central widget to the main window
#         self.setCentralWidget(widget)
  
  
#     # method called by the line edit
#     def handleTextEntered(self):
  
#         # get the text
#         text = self.edit.text()
  
#         # creating a pix map of qr code
#         qr_image = qrcode.make(text, image_factory = Image).pixmap()
  
#         # set image to the label
#         self.label.setPixmap(qr_image)