"""Doc."""
import sys
import os
import json  # noqa
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QAction, QMainWindow, QMenu, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLayout, \
    QFormLayout, QFrame, QAbstractItemView,  QSizePolicy, \
    QTabWidget, QScrollArea,  QStackedWidget, QStackedLayout, QSpacerItem   # noqa
from PyQt5 import QtWidgets, QtCore, QtGui  # noqa
from PyQt5.QtGui import QIcon, QPixmap  # noqa
from PyQt5.QtCore import Qt  # noqa
sys.path.append(os.path.abspath('resources/'))
import gui_icons  # noqa


def old_Nate_workshop(self):
    """Doc."""
    on_workshop_frame = QFrame()
    on_workshop_box = QVBoxLayout()
    on_workshop_frame.setLayout(on_workshop_box)

    cards_label = QLabel("OLDS NATE WORKSHOP LABEL")
    on_workshop_box.addWidget(cards_label)

    return on_workshop_frame
