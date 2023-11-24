import io
import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>789</width>
    <height>671</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="add_circle">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>520</y>
     <width>341</width>
     <height>141</height>
    </rect>
   </property>
   <property name="text">
    <string>Создать круг</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.add_circle.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_circles(painter)

    def draw_circles(self, painter):
        brush = QBrush(Qt.SolidPatten)
        painter.setBrush(brush)
        num_1 = random.randint(0, 255)
        num_2 = random.randint(0, 255)
        num_3 = random.randint(0, 255)
        painter.setPen(QColor(num_1, num_2, num_3))
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
