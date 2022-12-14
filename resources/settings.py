"""CREATE SETTINGS WINDOW."""
from PyQt5.QtWidgets import QGridLayout, QWidget, QVBoxLayout, \
    QLabel, QHBoxLayout
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import *  # noqa
from PyQt5 import QtCore
from painter import *  # noqa


class Widget_settings(QWidget):
    """Doc."""

    def __init__(self, parent):
        """INIT CLASS."""
        super(Widget_settings, self).__init__(parent)

        self.parent = parent
        self.setWindowFlags(QtCore.Qt.Window)
        self.pressing = False
        self.initSubWindow()

    def initSubWindow(self):
        """CLASS M OBJECT."""
        self.setMinimumSize(700, 500)
        self.setMaximumSize(1100, 800)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # main layout
        settings_layout = QGridLayout()
        settings_layout.setContentsMargins(90, 50, 50, 50)
        self.setLayout(settings_layout)

        def createheader() -> QHBoxLayout:  # header
            header_hbox = QHBoxLayout()
            header_hbox.setContentsMargins(50, 0, 0, 0)

            settings_label = QLabel("Settings")
            settings_label.setFont(QFont("Heuristica", 12))
            settings_label.setAlignment(Qt.AlignHCenter)
            header_hbox.addWidget(settings_label, alignment=Qt.AlignHCenter)

            def createheader_btn(action: str) -> QAbstractButton:
                btn = PushButton_HC(action)
                btn.setMinimumSize(30, 30)
                btn.setMaximumSize(30, 30)
                header_hbox.addWidget(btn, alignment=Qt.AlignTop)
                if action == "Hide":
                    btn.clicked.connect(self.showMinimized)
                elif action == "Exit":
                    btn.clicked.connect(self.close)
                return btn

            createheader_btn("Hide")
            createheader_btn("Exit")
            return header_hbox

        settings_layout.addLayout(createheader(),
                                  1, 1, Qt.AlignHCenter, Qt.AlignTop)

        def createsettings_area() -> QVBoxLayout:  # settings button
            mainBtn_vbox = QVBoxLayout()
            mainBtn_vbox.setAlignment(Qt.AlignTop)

            def createsettings_btn(section: str) -> QAbstractButton:
                btn = PushButton_Settings(section)
                btn.setMinimumSize(100, 35)
                btn.setMaximumSize(135, 55)
                mainBtn_vbox.addWidget(btn, alignment=Qt.AlignTop)
                if section == "Settings_1":
                    pass
                elif section == "Settings_2":
                    pass
                elif section == "Settings_3":
                    pass
                else:
                    btn.clicked.connect(self.exitApp)
                return btn

            createsettings_btn("Settings_1")
            createsettings_btn("Settings_2")
            createsettings_btn("Settings_3")
            createsettings_btn("Exit")
            return mainBtn_vbox

        settings_layout.addLayout(createsettings_area(), 2, 1, Qt.AlignLeft)

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

    def paintEvent(self, event):
        """PAINT EVENT."""
        QWidget.paintEvent(self, event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), QPixmap(
            "resources/images/assets/bg/bg_subwindow_postcard_gonesister_01_0.png"))  # noqa

    def exitApp(self):
        """Doc."""
        self.parent.close()
