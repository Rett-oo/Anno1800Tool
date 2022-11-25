import sys
import requests
from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QVBoxLayout, \
    QLabel, QHBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QPixmap, QImage
from PyQt5.QtCore import *  # noqa
from painter import *  # noqa


class Widget_settings(QWidget):
    """Doc."""

    def __init__(self, parent=QMainWindow):
        """Doc."""
        super().__init__()

        self.initSubWindow()

    def paintEvent(self, event):
        """PAINT EVENT."""
        QWidget.paintEvent(self, event)
        url = "https://6kcmxu3d7l.a.trbcdn.net/upload/files-new/f5/1c/3d/562610_1000x1000.jpg"
        pix = QPixmap()
        pix.loadFromData(requests.get(url).content)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), pix)


    def initSubWindow(self):
        """Doc."""
        self.setMinimumSize(700, 500)
        self.setMaximumSize(1100, 800)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        settings_layout = QGridLayout()
        settings_layout.setContentsMargins(90, 50, 50, 50)
        self.setLayout(settings_layout)

        header_hbox = QHBoxLayout()
        header_hbox.setContentsMargins(50, 0, 0, 0)
        settings_layout.addLayout(header_hbox, 1, 1, Qt.AlignHCenter, Qt.AlignTop)

        settings_label = QLabel("Settings")
        settings_label.setFont(QFont("Heuristica", 12))
        settings_label.setAlignment(Qt.AlignHCenter)
        header_hbox.addWidget(settings_label, alignment=Qt.AlignHCenter)

        hide_btn = QPushButton("Hide")
        hide_btn.setMinimumSize(30, 30)
        hide_btn.setMaximumSize(30, 30)
        close_btn = QPushButton("Exit")
        close_btn.setMinimumSize(30, 30)
        close_btn.setMaximumSize(30, 30)

        close_btn.setMaximumSize(30, 30)
        header_hbox.addWidget(hide_btn, alignment=Qt.AlignTop)
        header_hbox.addWidget(close_btn, alignment=Qt.AlignTop)

        mainBtn_vbox = QVBoxLayout()
        mainBtn_vbox.setAlignment(Qt.AlignTop)
        settings_layout.addLayout(mainBtn_vbox, 2, 1, Qt.AlignLeft)

        settings1 = QPushButton("Settings_1")
        settings1.setMinimumSize(100, 35)
        settings1.setMaximumSize(135, 55)
        settings2 = QPushButton("Settings_2")
        settings2.setMinimumSize(100, 35)
        settings2.setMaximumSize(135, 55)
        settings3 = QPushButton("Settings_3")
        settings3.setMinimumSize(100, 35)
        settings3.setMaximumSize(135, 55)
        quit_btn = QPushButton("Exit")
        quit_btn.setMinimumSize(100, 35)
        quit_btn.setMaximumSize(135, 55)
        quit_btn.clicked.connect(self.closeEvent)

        mainBtn_vbox.addWidget(settings1, alignment=Qt.AlignTop)
        mainBtn_vbox.addWidget(settings2, alignment=Qt.AlignTop)
        mainBtn_vbox.addWidget(settings3, alignment=Qt.AlignTop)
        mainBtn_vbox.addWidget(quit_btn, alignment=Qt.AlignTop)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def closeEvent(self, event):
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget_settings()
    w.show()
    sys.exit(app.exec_())