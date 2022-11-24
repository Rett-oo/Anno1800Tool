"""Doc."""
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QAction, QMainWindow, QMenu, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLayout, \
    QFormLayout, QFrame, QAbstractItemView   # noqa
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt, QModelIndex  # noqa
from shiboken6 import isValid  # noqa
import gui_icons  # noqa


with open("resourсes\\consumption_data_p.json") as f:
    json_table = json.load(f)


def _createtable(self):

    valid = QtCore.QRegExp("[0-9 .,]{15}")
    val = QtGui.QRegExpValidator(valid)

    table = QTableWidget(43, 5)
    sizePolicy = QtWidgets.QSizePolicy(
                 QtWidgets.QSizePolicy.Expanding,
                 QtWidgets.QSizePolicy.Expanding
                                      )
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalPolicy(0)
    sizePolicy.setHeightForWidth(
        table.sizePolicy().hasHeightForWidth()
                                )
    table.setSizePolicy(sizePolicy)
    table.setMinimumSize(QSize(400, 300))
    table.setMaximumSize(QSize(2000, 1000))
    table.setSizeIncrement(QSize(0, 0))
    table.setLayoutDirection(Qt.LeftToRight)
    table.setFrameShadow(QtWidgets.QFrame.Raised)
    table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    table.setShowGrid(False)
    table.setGridStyle(Qt.SolidLine)
    table.verticalHeader().setVisible(False)
    table.setSelectionMode(QAbstractItemView.NoSelection)
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    table.setFocusPolicy(Qt.NoFocus)
    table.setCurrentIndex(QModelIndex())
    table.setObjectName("Table")
    table.setHorizontalHeaderLabels([
        'Product', 'Base output',
        'Base\nconsumption',
        'Productivity',
        'Buildings\nRequired'
    ])
    table.horizontalHeader().setSectionResizeMode(
        QtWidgets.QHeaderView.Stretch)
    table.verticalHeader().setSectionResizeMode(
        QtWidgets.QHeaderView.ResizeToContents)

    column1 = []
    column2 = []
    column3 = []

    for list_dict in json_table.values():
        for key_value in list_dict:
            keys = key_value.keys()
            value = key_value.values()
            for key_item in keys:
                column1.append(key_item)		# значения для 1 столбца
            for value_item in value:
                column2.append(value_item[0])  # значения 2 столбца
                column3.append(value_item[1:])
                # списки со значениями для 3 столбца

    for row in range(table.rowCount()):
        gbox = QGridLayout()
        framebox = QFrame()
        framebox.setLayout(gbox)
        table.setCellWidget(row, 2, framebox)
        le4_box = QHBoxLayout()
        framebox2 = QFrame()
        framebox2.setLayout(le4_box)
        table.setCellWidget(row, 3, framebox2)
        hbox9 = QHBoxLayout()
        framebox3 = QFrame()
        framebox3.setLayout(hbox9)
        hbox9.setContentsMargins(0, 0, 0, 0)
        table.setCellWidget(row, 0, framebox3)
        required_la_box = QHBoxLayout()
        framebox4 = QFrame()
        framebox4.setLayout(required_la_box)
        table.setCellWidget(row, 4, framebox4)
        farmer = QLabel()
        farmer.setAlignment(Qt.AlignRight)
        farmer.setPixmap(
            QPixmap(':1_Farmers.webp').scaled(25, 25))
        worker = QLabel()
        worker.setAlignment(Qt.AlignRight)
        worker.setPixmap(
            QPixmap(':2_Workers.webp').scaled(25, 25))
        artisan = QLabel()
        artisan.setAlignment(Qt.AlignRight)
        artisan.setPixmap(
            QPixmap(':3_Artisans.webp').scaled(25, 25))
        engineer = QLabel()
        engineer.setAlignment(Qt.AlignRight)
        engineer.setPixmap(
            QPixmap(':4_Engineers.webp').scaled(25, 25))
        investor = QLabel()
        investor.setAlignment(Qt.AlignRight)
        investor.setPixmap(
            QPixmap(':5_Investors.webp').scaled(25, 25))
        scholar = QLabel()
        scholar.setAlignment(Qt.AlignRight)
        scholar.setPixmap(
            QPixmap(':6_Icon_resident_scholars_0.webp').scaled(25, 25))
        tourist = QLabel()
        tourist.setAlignment(Qt.AlignRight)
        tourist.setPixmap(
            QPixmap(':7_Tourists.webp').scaled(25, 25))
        for pics in (farmer, worker, artisan, engineer,
                     investor, scholar, tourist):
            pics.setStyleSheet("background-color: ")

        column_pop = column1.pop(0)
        column1_pb = QPushButton(QIcon(":" + column_pop), '')
        column1_pb.setMinimumSize(35, 35)
        column1_pb.setMaximumSize(35, 35)
        column1_pb.setStyleSheet("background-color: brown")
        hbox9.addWidget(column1_pb)
        widget = QTableWidgetItem(column2.pop(0))
        widget.setTextAlignment(Qt.AlignCenter)
        table.setItem(row % 60, 1, widget)  # заполнение 2 столбца
        widget.setFlags(Qt.ItemIsDragEnabled
                        | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
        list_values = column3.pop(0)
        if len(list_values) == 2:
            if column_pop in ("Fish.webp",
                              "Schnapps.webp",
                              "Work_clothes.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                gbox.addWidget(farmer, 0, 0, 1, 1)
                gbox.addWidget(worker, 1, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
            elif column_pop in ("Sausages.webp", "Bread.webp",
                                "Soap.webp", "Beer.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                gbox.addWidget(worker, 0, 0, 1, 1)
                gbox.addWidget(artisan, 1, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
            elif column_pop in ("Canned_food.webp",
                                "Sewing_machines.webp",
                                "Fur_Coats.webp", "Rum.webp",
                                "Advanced_rum_roaster.png"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                gbox.addWidget(artisan, 0, 0, 1, 1)
                gbox.addWidget(engineer, 1, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
            elif column_pop in ("Glasses.webp",
                                "High_wheeler.webp",
                                "Pocket_watch.webp",
                                "Light_bulb.webp", "Coffee.webp",
                                "Advanced_coffee_roaster.png",
                                "Chewing_Gum.webp",
                                "Typewriters.webp",
                                "Violins.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                gbox.addWidget(engineer, 0, 0, 1, 1)
                gbox.addWidget(investor, 1, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
            elif column_pop in ("Champagne.webp", "Jewelry.webp",
                                "Gramophone.webp",
                                "Steam_carriages.webp",
                                "Cigars.webp", "Chocolate.webp",
                                "Biscuits.webp", "Cognac.webp",
                                "Billiard_Tables.webp",
                                "Toys.webp"):
                if column_pop == "Jewelry.webp":
                    labe = QLabel(list_values[0])
                    labe2 = QLabel(list_values[1])
                    gbox.addWidget(investor, 0, 0, 1, 1)
                    gbox.addWidget(tourist, 1, 0, 1, 1)
                    gbox.addWidget(labe, 0, 1, 1, 1)
                    gbox.addWidget(labe2, 1, 1, 1, 1)
                else:
                    labe = QLabel(list_values[0])
                    labe2 = QLabel(list_values[1])
                    gbox.addWidget(investor, 0, 0, 1, 1)
                    gbox.addWidget(scholar, 1, 0, 1, 1)
                    gbox.addWidget(labe, 0, 1, 1, 1)
                    gbox.addWidget(labe2, 1, 1, 1, 1)
            elif column_pop in ("Bowler_hats.webp",
                                "Icon_hibiscus_tea_0.webp",
                                "Icon_tapestries_0.webp",
                                "Icon_wat_stew_0.webp",
                                "Icon_tobacco_pipes_0.webp",
                                "Icon_leather_shoes_0.webp",
                                "Icon_suits_0.webp",
                                "Icon_telephones_0.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                gbox.addWidget(scholar, 0, 0, 1, 1)
                gbox.addWidget(investor, 1, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
            else:
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                gbox.addWidget(tourist, 0, 0, 1, 1)
                gbox.addWidget(tourist, 1, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
        elif len(list_values) == 3:
            if column_pop in ("Fish.webp", "Schnapps.webp",
                              "Work_clothes.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                labe3 = QLabel(list_values[2])
                labe3.setStyleSheet("font-family: Roboto; \
                                    font-size: 14px;")
                gbox.addWidget(farmer, 0, 0, 1, 1)
                gbox.addWidget(worker, 1, 0, 1, 1)
                gbox.addWidget(artisan, 2, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
                gbox.addWidget(labe3, 2, 1, 1, 1)
            elif column_pop in ("Sausages.webp", "Bread.webp",
                                "Soap.webp", "Beer.webp"):
                if column_pop == "Bread.webp":
                    labe = QLabel(list_values[0])
                    labe2 = QLabel(list_values[1])
                    labe3 = QLabel(list_values[2])
                    labe3.setStyleSheet("font-family: Roboto; \
                                        font-size: 14px;")
                    gbox.addWidget(worker, 0, 0, 1, 1)
                    gbox.addWidget(artisan, 1, 0, 1, 1)
                    gbox.addWidget(tourist, 2, 0, 1, 1)
                    gbox.addWidget(labe, 0, 1, 1, 1)
                    gbox.addWidget(labe2, 1, 1, 1, 1)
                    gbox.addWidget(labe3, 2, 1, 1, 1)
                else:
                    labe = QLabel(list_values[0])
                    labe2 = QLabel(list_values[1])
                    labe3 = QLabel(list_values[2])
                    labe3.setStyleSheet("font-family: Roboto; \
                                        font-size: 14px;")
                    gbox.addWidget(worker, 0, 0, 1, 1)
                    gbox.addWidget(artisan, 1, 0, 1, 1)
                    gbox.addWidget(engineer, 2, 0, 1, 1)
                    gbox.addWidget(labe, 0, 1, 1, 1)
                    gbox.addWidget(labe2, 1, 1, 1, 1)
                    gbox.addWidget(labe3, 2, 1, 1, 1)
            elif column_pop in ("Canned_food.webp",
                                "Sewing_machines.webp",
                                "Fur_Coats.webp", "Rum.webp",
                                "Advanced_rum_roaster.png"):
                if column_pop == "Canned_food.webp":
                    labe = QLabel(list_values[0])
                    labe2 = QLabel(list_values[1])
                    labe3 = QLabel(list_values[2])
                    labe3.setStyleSheet("font-family: Roboto; \
                                        font-size: 14px;")
                    gbox.addWidget(artisan, 0, 0, 1, 1)
                    gbox.addWidget(engineer, 1, 0, 1, 1)
                    gbox.addWidget(scholar, 2, 0, 1, 1)
                    gbox.addWidget(labe, 0, 1, 1, 1)
                    gbox.addWidget(labe2, 1, 1, 1, 1)
                    gbox.addWidget(labe3, 2, 1, 1, 1)
                if column_pop == "Fur_Coats.webp":
                    labe = QLabel(list_values[0])
                    labe2 = QLabel(list_values[1])
                    labe3 = QLabel(list_values[2])
                    labe3.setStyleSheet("font-family: Roboto; \
                                        font-size: 14px;")
                    gbox.addWidget(artisan, 0, 0, 1, 1)
                    gbox.addWidget(engineer, 1, 0, 1, 1)
                    gbox.addWidget(tourist, 2, 0, 1, 1)
                    gbox.addWidget(labe, 0, 1, 1, 1)
                    gbox.addWidget(labe2, 1,  1, 1, 1)
                    gbox.addWidget(labe3, 2, 1, 1, 1)
                if column_pop in ("Rum.webp",
                                  "Advanced_rum_roaster.png"):
                    labe = QLabel(list_values[0])
                    labe2 = QLabel(list_values[1])
                    labe3 = QLabel(list_values[2])
                    labe3.setStyleSheet("font-family: Roboto; \
                                        font-size: 14px;")
                    gbox.addWidget(artisan, 0, 0, 1, 1)
                    gbox.addWidget(engineer, 1, 0, 1, 1)
                    gbox.addWidget(scholar, 2, 0, 1, 1)
                    gbox.addWidget(labe, 0, 1, 1, 1)
                    gbox.addWidget(labe2, 1, 1, 1, 1)
                    gbox.addWidget(labe3, 2, 1, 1, 1)
            elif column_pop in ("Glasses.webp",
                                "High_wheeler.webp",
                                "Pocket_watch.webp",
                                "Light_bulb.webp", "Coffee.webp",
                                "Advanced_coffee_roaster.png",
                                "Chewing_Gum.webp",
                                "Typewriters.webp",
                                "Violins.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                labe3 = QLabel(list_values[2])
                labe3.setStyleSheet("font-family: Roboto; \
                                    font-size: 14px;")
                gbox.addWidget(engineer, 1, 0, 1, 1)
                gbox.addWidget(investor, 1, 0, 1, 1)
                gbox.addWidget(scholar, 2, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
                gbox.addWidget(labe3, 2, 1, 1, 1)
            elif column_pop in ("Champagne.webp", "Jewelry.webp",
                                "Gramophone.webp",
                                "Steam_carriages.webp",
                                "Cigars.webp", "Chocolate.webp",
                                "Biscuits.webp", "Cognac.webp",
                                "Billiard_Tables.webp",
                                "Toys.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                labe3 = QLabel(list_values[2])
                labe3.setStyleSheet("font-family: Roboto; \
                                    font-size: 14px;")
                gbox.addWidget(investor, 0, 0, 1, 1)
                gbox.addWidget(scholar, 1, 0, 1, 1)
                gbox.addWidget(tourist, 2, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
                gbox.addWidget(labe3, 2, 1, 1, 1)
            elif column_pop in ("Bowler_hats.webp",
                                "Icon_hibiscus_tea_0.webp",
                                "Icon_tapestries_0.webp",
                                "Icon_wat_stew_0.webp",
                                "Icon_tobacco_pipes_0.webp",
                                "Icon_leather_shoes_0.webp",
                                "Icon_suits_0.webp",
                                "Icon_telephones_0.webp"):
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                labe3 = QLabel(list_values[2])
                labe3.setStyleSheet("font-family: Roboto; \
                                    font-size: 14px;")
                gbox.addWidget(scholar, 0, 0, 1, 1)
                gbox.addWidget(scholar, 1, 0, 1, 1)
                gbox.addWidget(scholar, 2, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
                gbox.addWidget(labe3, 2, 1, 1, 1)
            else:
                labe = QLabel(list_values[0])
                labe2 = QLabel(list_values[1])
                labe3 = QLabel(list_values[2])
                labe3.setStyleSheet("font-family: Roboto; \
                                    font-size: 14px;")
                gbox.addWidget(tourist, 0, 0, 1, 1)
                gbox.addWidget(tourist, 1, 0, 1, 1)
                gbox.addWidget(tourist, 2, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
                gbox.addWidget(labe2, 1, 1, 1, 1)
                gbox.addWidget(labe3, 2, 1, 1, 1)
        else:
            if column_pop in ("Fish.webp", "Schnapps.webp",
                              "Work_clothes.webp"):
                labe = QLabel(list_values[0])
                gbox.addWidget(farmer, 0, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
            elif column_pop in ("Sausages.webp", "Bread.webp",
                                "Soap.webp", "Beer.webp"):
                labe = QLabel(list_values[0])
                gbox.addWidget(worker, 0, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
            elif column_pop in ("Canned_food.webp",
                                "Sewing_machines.webp",
                                "Fur_Coats.webp", "Rum.webp",
                                "Advanced_rum_roaster.png"):
                labe = QLabel(list_values[0])
                gbox.addWidget(artisan, 0, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
            elif column_pop in ("Glasses.webp",
                                "High_wheeler.webp",
                                "Pocket_watch.webp",
                                "Light_bulb.webp", "Coffee.webp",
                                "Advanced_coffee_roaster.png",
                                "Chewing_Gum.webp",
                                "Typewriters.webp",
                                "Violins.webp"):
                labe = QLabel(list_values[0])
                gbox.addWidget(engineer, 0, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
            elif column_pop in ("Champagne.webp", "Jewelry.webp",
                                "Gramophone.webp",
                                "Steam_carriages.webp",
                                "Cigars.webp", "Chocolate.webp",
                                "Biscuits.webp", "Cognac.webp",
                                "Billiard_Tables.webp",
                                "Toys.webp"):
                labe = QLabel(list_values[0])
                gbox.addWidget(investor, 0, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
            elif column_pop in ("Bowler_hats.webp",
                                "Icon_hibiscus_tea_0.webp",
                                "Icon_tapestries_0.webp",
                                "Icon_wat_stew_0.webp",
                                "Icon_tobacco_pipes_0.webp",
                                "Icon_leather_shoes_0.webp",
                                "Icon_suits_0.webp",
                                "Icon_telephones_0.webp"):
                labe = QLabel(list_values[0])
                gbox.addWidget(scholar, 0, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
            else:
                labe = QLabel(list_values[0])
                gbox.addWidget(tourist, 0, 0, 1, 1)
                gbox.addWidget(labe, 0, 1, 1, 1)
        labe.setStyleSheet("font-family: Roboto; \
                            font-size: 14px;")
        labe2.setStyleSheet("font-family: Roboto; \
                            font-size: 14px;")
        column4_le = QLineEdit("100")
        column4_le.setValidator(val)
        column4_le.setMaxLength(4)
        column4_le.setAlignment(Qt.AlignCenter)
        column4_le.setMinimumSize(50, 20)
        column4_le.setMaximumSize(100, 25)
        column4_le.setStyleSheet("background-color: #ced2bc; \
                             font: 12px;border-radius: 3px; \
                             font-style: Roboto")
        column4_la = QLabel()
        column4_la.setAlignment(Qt.AlignCenter)
        column4_la.setMaximumSize(30, 25)
        column4_la.setPixmap(
            QPixmap(
                ":free-icon-percent-4688859.png"
            ).scaled(15, 15))
        le4_box.addWidget(column4_le)
        le4_box.addWidget(column4_la)
        column5_la = QLabel("0")
        column5_la.setAlignment(Qt.AlignCenter)
        column5_la.setStyleSheet("color: white; font-size: 12px")

        column4_le.textChanged.connect(
            lambda text=column4_le.text(), col5=column5_la, col2=widget.text():
                self.action1(text, col5, col2))

        required_la_box.addWidget(column5_la)

    return table
