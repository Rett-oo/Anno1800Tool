"""Doc."""
import json  # noqa
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets  # noqa
from PyQt5.QtCore import Qt  # noqa
from PyQt5.QtGui import QIcon, QPixmap  # noqa
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,  # noqa
                             QDesktopWidget, QFormLayout, QFrame, QGridLayout,
                             QHBoxLayout, QLabel, QLayout, QLineEdit,
                             QMainWindow, QMenu, QPushButton, QScrollArea,
                             QSizePolicy, QSpacerItem, QStackedLayout,
                             QStackedWidget, QTableWidget, QTableWidgetItem,
                             QTabWidget, QVBoxLayout, QWidget)

sys.path.append(os.path.abspath('resources/'))
import gui_icons  # noqa


def goods(self):
    """Doc."""
    goods_frame = QFrame()
    goods_box = QVBoxLayout()
    goods_frame.setLayout(goods_box)

    goods_btn_box = QHBoxLayout()
    exp_supplies_btn = QPushButton("Expedition\nSupplies")
    trade_price_btn = QPushButton("Trade Prices")
    fdv_btn = QPushButton("Food, Drink\nVenue")
    shopping_arcade_btn = QPushButton("Shopping\nArcades")
    # goods buttons
    goods_btn_box.addWidget(exp_supplies_btn)
    goods_btn_box.addWidget(trade_price_btn)
    goods_btn_box.addWidget(fdv_btn)
    goods_btn_box.addWidget(shopping_arcade_btn)
    goods_box.addLayout(goods_btn_box)

    cards_label = QLabel("GOODS LABEL")
    cards_label.setAlignment(Qt.AlignCenter)
    goods_box.addWidget(cards_label)

    goods_stacked_w = QStackedWidget()
    goods_box.addWidget(goods_stacked_w)

    def expedition_supplies(self):

        exp_supplies_frame = QFrame()
        exp_supplies_mainv_box = QVBoxLayout()
        exp_supplies_frame.setLayout(exp_supplies_mainv_box)

        exp_supplies_g_box = QGridLayout()

        rations_btn = QPushButton("Rations")
        crafting_btn = QPushButton("Crafting")
        diplomacy_btn = QPushButton("Diplomacy")
        faith_btn = QPushButton("Faith")
        force_btn = QPushButton("Force")
        hunting_btn = QPushButton("Hunting")
        medicine_btn = QPushButton("Medicine")
        naval_power_btn = QPushButton("Naval Power")
        navigation_btn = QPushButton("Navigation")

        exp_supplies_g_box.addWidget(rations_btn, 0, 0, 1, 1)
        exp_supplies_g_box.addWidget(crafting_btn, 0, 1, 1, 1)
        exp_supplies_g_box.addWidget(diplomacy_btn, 0, 2, 1, 1)
        exp_supplies_g_box.addWidget(faith_btn, 1, 0, 1, 1)
        exp_supplies_g_box.addWidget(force_btn, 1, 1, 1, 1)
        exp_supplies_g_box.addWidget(hunting_btn, 1, 2, 1, 1)
        exp_supplies_g_box.addWidget(medicine_btn, 2, 0, 1, 1)
        exp_supplies_g_box.addWidget(naval_power_btn, 2, 1, 1, 1)
        exp_supplies_g_box.addWidget(navigation_btn, 2, 2, 1, 1)

        goods_table_stacked_w = QStackedWidget()
        goods_table = QTableWidget(5, 40)
        goods_table_stacked_w.addWidget(goods_table)

        exp_supplies_mainv_box.addLayout(exp_supplies_g_box)
        exp_supplies_mainv_box.addWidget(goods_table_stacked_w)

        return exp_supplies_frame

    goods_stacked_w.addWidget(expedition_supplies(self))

    return goods_frame
