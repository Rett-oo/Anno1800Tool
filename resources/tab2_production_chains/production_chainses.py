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


def production_chains(self):
    """Doc."""
    pc_frame = QFrame()
    pc_box = QVBoxLayout()
    pc_frame.setLayout(pc_box)

    cards_label = QLabel("PRODUCTION CHAINS LABEL")
    pc_box.addWidget(cards_label)

    return pc_frame
