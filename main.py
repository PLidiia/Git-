import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle.ui', self)
        self.add_circle.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_circles(painter)

    def draw_circles(self, painter):
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.setPen(QColor(255, 255, 0))
        size = self.size()
        for i in range(1, 6):
            diameter = random.randint(10, 50)
            x = random.randint(0, size.width() - diameter)
            y = random.randint(0, size.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec_())
