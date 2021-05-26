
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPainter, QPixmap
from PyQt5.QtWidgets import QGridLayout, QLabel
import qrcode


class QrCodeContainer(QGridLayout):
    '''Display container for the generated QR code and link.'''

    def __init__(self, host: str, port: int, protocol: str = 'http'):
        QGridLayout.__init__(self)
        address = f'{protocol}://{host}:{port}'
        qr_image: QPixmap = qrcode.make(address, image_factory=QrCodeImage).pixmap()

        self.image = QLabel()
        self.image.setPixmap(qr_image)

        self.link = QLabel(text=f'<font color=#0000ee>{address}</font>')

        self.addWidget(self.image, 0, 0, Qt.AlignCenter)
        self.addWidget(self.link, 1, 0, Qt.AlignCenter)


class QrCodeImage(qrcode.image.base.BaseImage):
    '''Image class for QR code'''

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
        painter.fillRect((col + self.border) * self.box_size,
                         (row + self.border) * self.box_size,
                         self.box_size,
                         self.box_size,
                         Qt.black)
