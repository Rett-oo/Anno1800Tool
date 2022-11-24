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


def mzg(self):
    """Doc."""
    mzg_frame = QFrame()
    mzg_box = QVBoxLayout()
    mzg_frame.setLayout(mzg_box)

    cards_label = QLabel("MUSEUM\nZOO\nGARDEN\nLABEL")
    mzg_box.addWidget(cards_label)

    return mzg_frame
