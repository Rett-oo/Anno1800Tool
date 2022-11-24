"""Doc."""
import sys
import os
import sqlite3
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QAction, QMainWindow, QMenu, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLayout, \
    QFormLayout, QFrame, QAbstractItemView, QSizePolicy  # noqa
from PyQt5 import QtWidgets, QtCore, QtGui  # noqa
from PyQt5.QtGui import QIcon, QPixmap  # noqa
from PyQt5.QtCore import Qt  # noqa
sys.path.append(os.path.abspath('resourсes/'))
import gui_icons  # noqa
from table import _createtable  # noqa
from consumption import _consumptiontab  # noqa


base = sqlite3.connect('information.db')
cur = base.cursor()
with open("resourсes\\consumption_data_h.json") as f:
    json_table = json.load(f)
with open("resourсes\\consumption_data_p.json") as g:
    json_table2 = json.load(g)


class HighlightDelegate(QtWidgets.QStyledItemDelegate):
    """Doc."""

    def initStyleOption(self, option, index):
        """Doc."""
        super(HighlightDelegate, self).initStyleOption(option, index)
        option.backgroundBrush = QtGui.QBrush(QtGui.QColor("#805130"))
        if index.column() == 4:
            option.backgroundBrush = QtGui.QBrush(QtGui.QColor("#302522"))
        if index.column() == 0:
            option.backgroundBrush = QtGui.QBrush(QtGui.QColor("#72583f"))

    def paint(self, painter, option, index):
        """Doc."""
        super(HighlightDelegate, self).paint(painter, option, index)
        line = QtCore.QLine(option.rect.topRight(), option.rect.bottomRight())
        line2 = QtCore.QLine(option.rect.topLeft(), option.rect.bottomLeft())
        painter.save()
        painter.setPen(QtGui.QPen(QtGui.QColor("#dbe48b"), 3))
        painter.drawLine(line)
        painter.drawLine(line2)
        painter.restore()


class MainWindow(QMainWindow):
    """Doc."""

    def __init__(self):
        """Doc."""
        super().__init__()
        self.initUI()
# 		self._createActions()
# 		self._createMenuBar()

    def initUI(self):		# set window's geometry
        """Doc."""
        self.setMinimumSize(800, 600)
        self.setWindowTitle('Anno 1800 tools')
        self.setWindowIcon(QIcon(':Site-logo.webp'))
# 		self.setWindowFlag(Qt.FramelessWindowHint)  #убирает границы окна
# 		self.setAttribute(Qt.WA_TranslucentBackground) ! делает фон евидимым
        self.setAutoFillBackground(True)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        centralwidget = QWidget(self)
        self.setCentralWidget(centralwidget)
        main_box = QGridLayout(centralwidget)
        top_bar_box = QHBoxLayout()
        top_bar_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        top_bar_box.setContentsMargins(40, 0, 0, 0)
        top_bar_box.setSpacing(0)
        top_bar_box.setObjectName("TopBar")
        settings_info_box = QVBoxLayout()
        settings_info_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        settings_info_box.setSpacing(5)
        settings_info_box.setContentsMargins(50, 0, 0, 0)
        settings_info_box.setObjectName("Settings and Info")

        def create_top_bar():
            consumption_btn = QPushButton('Consumption \n calculator', self)
            consumption_btn.setObjectName("consumption_btn")
            production_chains_btn = QPushButton('Production\n chains', self)
            products_btn = QPushButton('Goods', self)
            NateWorkshop_btn = QPushButton("Old Nate's\n Workshop", self)
            MZG_btn = QPushButton("Museum,Zoo \nand Garden", self)
            logistics_btn = QPushButton("Logistics\n chains", self)
            cards_btn = QPushButton("Cards", self)
            settings_btn = QPushButton(QIcon(
                        ":Workforce_-_technicians.webp"), "")
            settings_btn.setFixedSize(30, 30)
            settings_btn.setStyleSheet("background-color: #ced2bc")
            info_btn = QPushButton(QIcon(
                                   ":Workforce_-_explorers.webp"), "")
            info_btn.setFixedSize(30, 30)
            info_btn.setStyleSheet("background-color: #ced2bc")
            settings_info_box.addWidget(settings_btn)
            settings_info_box.addWidget(info_btn)
            tabs_list = (consumption_btn, production_chains_btn, products_btn,
                         NateWorkshop_btn, MZG_btn, logistics_btn, cards_btn)
            for tabs in tabs_list:
                tabs.setMinimumSize(90, 40)
                tabs.setStyleSheet("background-color: #ced2bc; \
                                   font: 12px;font-style: Roboto")
                top_bar_box.addWidget(tabs)
            top_bar_box.addLayout(settings_info_box)
            main_box.addLayout(top_bar_box, 0, 0, 1, 3)
            return consumption_btn, production_chains_btn, products_btn, \
                NateWorkshop_btn, MZG_btn, logistics_btn, cards_btn

        create_top_bar()
        self.cons_tab = _consumptiontab(self)

        main_box.addLayout(self.cons_tab[0], 1, 0, 1, 3)

        delegate = HighlightDelegate(self.cons_tab[1])
        self.cons_tab[1].setItemDelegate(delegate)

    def action1(self, text, col5, col2, x):
        """Doc.

        Расчет необходимого.
        type_population*base_consumption/(productivity/100)*base_output
        """
        _value = int(text)
        _value2 = float(col2)
        col5.setText(f'{round(_value/100*_value2,2)}')
        # добавить значения 3 колонки

    def action2(self, text2, col5):
        """Doc."""
        pass

    def action_house_btn(self, pb, edem, laybels, plb):
        """Doc.

        Смена типа популяции - house
        Замена type_population_label, type_population_edit,
        table_column3(иконки, значения).
        edem = строки редактирования, laybels = макет для иконок,
        pls = слой для слоёв-иконок
        """
        house = []
        for list_dict in json_table.values():
            for key_value in list_dict:
                keys = key_value.keys()
                value = key_value.values()
                for key_item in keys:
                    if key_item == "House_id":
                        for i in value:
                            for u in i:
                                house.append(u)
        for i in laybels:
            i.setPixmap(QPixmap(":"+house.pop(0)))

    def action_people_btn(self, bp, laybels):
        """Doc.

        Смена типа популяции - people
        Замена type_population_label, type_population_edit,
        table_column3(иконки, значения)
        laybels = макет для иконок
        """
        people = []
        for list_dict in json_table2.values():
            for key_value in list_dict:
                keys = key_value.keys()
                value = key_value.values()
                for key_item in keys:
                    if key_item == "People_id":
                        for i in value:
                            for u in i:
                                people.append(u)
        for i in laybels:
            i.setPixmap(QPixmap(":"+people.pop(0)))

    def _createActions(self):       # button click actions
        self.newfileAction = QAction('&New', self)
        self.newfileAction.setStatusTip('Create new file')

        self.openfileAction = QAction('&Open', self)
        self.openfileAction.setStatusTip(' Open the existing settings ')

        self.saveAction = QAction('&Save', self)
        self.saveAction.setStatusTip('Save current settings')
        self.saveasAction = QAction('&Save as', self)
        self.saveasAction.setStatusTip('Save current settings \
                                        in new file or another directory')
        self.exitAction = QAction(QIcon(':logout_.png'), 'Quit', self)
        self.exitAction.triggered.connect(self.close)
        self.exitAction.setShortcut('Ctrl+Q')             # create shortcut
        self.settings = QAction('& App Settings', self)
        self.settings.setStatusTip('All settings')
        self.gvsettings = QAction(QIcon(':conversion.svg'),
                                  'Game version', self)
        self.gvsettings.setStatusTip('Change your game version')
        self.wikiAction = QAction(QIcon(':info_.png'), '&Anno 1800 Wiki', self)
        self.wikiAction.setStatusTip('Databases of Anno 1800')
        self.adviceAction = QAction('&Useful advices', self)
        self.adviceAction.setStatusTip('Give some advice')
        self.aboutAction = QAction('&About', self)
        self.aboutAction.setStatusTip('About App')

    def _createMenuBar(self):     # create buttons in Menu Bar
        menuBar = self.menuBar()
        fileMenu = QMenu('&File', self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newfileAction)
        fileMenu.addAction(self.openfileAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.saveasAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        settings = menuBar.addMenu('&Settings')
        settings.addAction(self.settings)
        settings.addAction(self.gvsettings)
        helpMenu = menuBar.addMenu('&Help')
        adviceMenu = helpMenu.addMenu('Help content')
        adviceMenu.addAction(self.adviceAction)
        adviceMenu.addAction(self.wikiAction)
        helpMenu.addAction(self.aboutAction)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("resourсes\\style.css", "r") as f:
        app.setStyleSheet(f.read())
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
