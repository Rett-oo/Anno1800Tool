"""Doc."""

from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout, \
    QLabel, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy  # noqa
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import *  # noqa
from PyQt5 import QtCore
from painter import *  # noqa


class Widget_settings(QWidget):
    """Doc."""

    def __init__(self, parent):
        """Doc."""
        super(Widget_settings, self).__init__(parent)

        self.parent = parent
        self.setWindowFlags(QtCore.Qt.Window)
        self.pressing = False
        self.initSubWindow()

    def paintEvent(self, event):
        """PAINT EVENT."""
        QWidget.paintEvent(self, event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), QPixmap(
            "E:/Python/Anno1800Tool/resources/images/assets/bg/bg_subwindow_postcard_gonesister_01_0.png"))  # noqa

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
        settings_layout.addLayout(header_hbox, 1, 1,
                                  Qt.AlignHCenter, Qt.AlignTop)

        settings_label = QLabel("Settings")
        settings_label.setFont(QFont("Heuristica", 12))
        settings_label.setAlignment(Qt.AlignHCenter)
        header_hbox.addWidget(settings_label, alignment=Qt.AlignHCenter)

        spacer = QSpacerItem(10, 1, QSizePolicy.Expanding, QSizePolicy.Fixed)  # noqa
        # header_hbox.addSpacerItem(spacer)

        hide_btn = PushButton_HC("Hide")
        hide_btn.setMinimumSize(30, 30)
        hide_btn.setMaximumSize(30, 30)
        hide_btn.clicked.connect(self.showMinimized)
        close_btn = PushButton_HC("Exit")
        close_btn.setMinimumSize(30, 30)
        close_btn.setMaximumSize(30, 30)
        close_btn.setMaximumSize(30, 30)
        close_btn.clicked.connect(self.close)

        header_hbox.addWidget(hide_btn, alignment=Qt.AlignTop)
        header_hbox.addWidget(close_btn, alignment=Qt.AlignTop)

        mainBtn_vbox = QVBoxLayout()
        mainBtn_vbox.setAlignment(Qt.AlignTop)
        settings_layout.addLayout(mainBtn_vbox, 2, 1, Qt.AlignLeft)

        settings1 = PushButton_Settings("Settings_1")
        settings1.setMinimumSize(100, 35)
        settings1.setMaximumSize(135, 55)
        settings2 = PushButton_Settings("Settings_2")
        settings2.setMinimumSize(100, 35)
        settings2.setMaximumSize(135, 55)
        settings3 = PushButton_Settings("Settings_3")
        settings3.setMinimumSize(100, 35)
        settings3.setMaximumSize(135, 55)
        self.quit_btn = PushButton_Settings("Exit")
        self.quit_btn.setMinimumSize(100, 35)
        self.quit_btn.setMaximumSize(135, 55)
        self.quit_btn.clicked.connect(self.exitApp)

        mainBtn_vbox.addWidget(settings1, alignment=Qt.AlignTop)
        mainBtn_vbox.addWidget(settings2, alignment=Qt.AlignTop)
        mainBtn_vbox.addWidget(settings3, alignment=Qt.AlignTop)
        mainBtn_vbox.addWidget(self.quit_btn, alignment=Qt.AlignTop)

    def mousePressEvent(self, event):
        """MOUSE PRESS EVENT."""
        self.oldPosition = event.globalPos()
        self.pressing = True

    def mouseMoveEvent(self, event):
        """MOUSE MOVE EVENT."""
        if self.pressing:
            delta = QPoint(event.globalPos() - self.oldPosition)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPosition = event.globalPos()

    def mouseReleaseEvent(self, event):
        """MOUSE RELEASE EVENT."""
        self.pressing = False

    def exitApp(self):
        self.parent.close()

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         self.close()
