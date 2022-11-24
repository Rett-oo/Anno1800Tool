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


def logistics_chains(self):
    """Doc."""
    lc_frame = QFrame()
    lc_box = QVBoxLayout()
    lc_frame.setLayout(lc_box)

    cards_label = QLabel("LOGISTIC CHAINS LABEL")
    lc_box.addWidget(cards_label)

    return lc_frame
