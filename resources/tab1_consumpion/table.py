"""Doc."""
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QAction, QMainWindow, QMenu, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLayout, \
    QFormLayout, QFrame, QAbstractItemView, QSpacerItem, QSizePolicy, QStackedWidget, QFrame  # noqa
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt, QModelIndex, QObject  # noqa
from shiboken6 import isValid  # noqa
from resources import gui_icons  # noqa


with open("resources\\tab1_consumpion\\consumption_data_p.json") as p:
    json_table = json.load(p)
with open("resources\\tab1_consumpion\\consumption_data_h.json") as h:
    json_table2 = json.load(h)


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


def _createtable(self, region):

    valid = QtCore.QRegExp("[0-9 .,]{15}")
    val = QtGui.QRegExpValidator(valid)

    if region == "Old_World":
        # создание списков для заполнения таблицы
        column1 = []
        column2 = []
        column3_people = []
        column3_home = []

        for list_dict in json_table[region]:
            column1.append(list(list_dict)[0])
            column2.append(list(list_dict.values())[0][0])
            column3_people.append(list(list_dict.values())[0][1:])

        for list_dict in json_table2[region]:
            column3_home.append(list(list_dict.values())[0][1:])

        table = QTableWidget(43, 5)
        self.table_row_column = {}

        # создание иконок для 3 колонки
        for iz in range(table.rowCount()):
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    pop_label_p = QLabel(self)
                    pop_label_p.move(0, -100)
                    pop_label_p.setAlignment(Qt.AlignRight)
                    pop_label_p.setPixmap(
                        QPixmap(":" + people_icon_id).scaled(25, 25))
                    pop_label_p.setObjectName(f"{people_icon_id}")

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    pop_label_h = QLabel(self)
                    pop_label_h.move(0, -100)
                    pop_label_h.setAlignment(Qt.AlignRight)
                    pop_label_h.setPixmap(
                        QPixmap(":" + home_icon_id).scaled(25, 25))
                    pop_label_h.setObjectName(f"{home_icon_id}")

        for row in range(table.rowCount()):
            # 1 column
            column1_h_box = QHBoxLayout()
            column1_frame = QFrame()
            column1_frame.setLayout(column1_h_box)
            column_pop = column1.pop(0)
            column1_pb = QPushButton(QIcon(":" + column_pop), '')
            column1_pb.setMinimumSize(35, 35)
            column1_pb.setMaximumSize(35, 35)
            column1_h_box.addWidget(column1_pb)
            column1_h_box.setContentsMargins(0, 0, 0, 0)
            table.setCellWidget(row, 0, column1_frame)
            # 2 column
            self.column2_text = QTableWidgetItem(column2.pop(0))
            self.column2_text.setTextAlignment(Qt.AlignCenter)
            table.setItem(row % 60, 1, self.column2_text)
            # 3 column
            column3_frame1 = QFrame()
            column3_g_box1 = QGridLayout(column3_frame1)
            column3_frame2 = QFrame()
            column3_g_box2 = QGridLayout(column3_frame2)

            column3_stacked_w = QStackedWidget()
            column3_stacked_w.addWidget(column3_frame1)
            column3_stacked_w.addWidget(column3_frame2)
            table.setCellWidget(row, 2, column3_stacked_w)

            self.table_row_column[row, 2] = column3_stacked_w

            column3_p_value = column3_people.pop(0)
            column3_h_value = column3_home.pop(0)
            if len(column3_p_value) == 2:
                if column_pop in ("Fish.webp",
                                  "Schnapps.webp",
                                  "Work_clothes.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "1_Farmers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "2_Workers.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "1_house_tier01.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "2_house_tier02.webp"), 1, 0, 1, 1)  # noqa
                elif column_pop in ("Sausages.webp", "Bread.webp",
                                    "Soap.webp", "Beer.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "2_Workers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "3_Artisans.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "2_house_tier02.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "3_house_tier03.webp"), 1, 0, 1, 1)  # noqa
                elif column_pop in ("Canned_food.webp",
                                    "Sewing_machines.webp",
                                    "Fur_Coats.webp", "Rum.webp",
                                    "Advanced_rum_roaster.png"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)  # noqa
                elif column_pop in ("Glasses.webp",
                                    "High_wheeler.webp",
                                    "Pocket_watch.webp",
                                    "Light_bulb.webp", "Coffee.webp",
                                    "Advanced_coffee_roaster.png",
                                    "Chewing_Gum.webp",
                                    "Typewriters.webp",
                                    "Violins.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "4_Engineers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "5_Investors.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "4_house_tier04.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "5_house_tier05.webp"), 1, 0, 1, 1)  # noqa
                elif column_pop in ("Champagne.webp", "Jewelry.webp",
                                    "Gramophone.webp",
                                    "Steam_carriages.webp",
                                    "Cigars.webp", "Chocolate.webp",
                                    "Biscuits.webp", "Cognac.webp",
                                    "Billiard_Tables.webp",
                                    "Toys.webp"):
                    if column_pop == "Jewelry.webp":
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "5_Investors.webp"), 0, 0, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "7_Tourists.webp"), 1, 0, 1, 1)
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "5_house_tier05.webp"), 0, 0, 1, 1)
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "7_house_tier7.png"), 1, 0, 1, 1)
                    else:
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "5_Investors.webp"), 0, 0, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "6_Icon_resident_scholars_0.webp"), 1, 0, 1, 1)  # noqa
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "5_house_tier05.webp"), 0, 0, 1, 1)
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "6_house_tier6.png"), 1, 0, 1, 1)
                elif column_pop in ("Bowler_hats.webp",
                                    "Icon_hibiscus_tea_0.webp",
                                    "Icon_tapestries_0.webp",
                                    "Icon_wat_stew_0.webp",
                                    "Icon_tobacco_pipes_0.webp",
                                    "Icon_leather_shoes_0.webp",
                                    "Icon_suits_0.webp",
                                    "Icon_telephones_0.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "5_Investors.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "6_house_tier6.png"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "5_house_tier05.webp"), 1, 0, 1, 1)
                else:
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "7_Tourists.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "7_Tourists.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "7_house_tier7.png"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "7_house_tier7.png"), 1, 0, 1, 1)  # noqa

            elif len(column3_p_value) == 3:
                if column_pop == "Bread.webp":
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "2_Workers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "7_Tourists.webp"), 2, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "2_house_tier02.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 2, 0, 1, 1)
                elif column_pop == "Canned_food.webp":
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 2, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "6_house_tier6.png"), 2, 0, 1, 1)
                elif column_pop == "Fur_Coats.webp":
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "7_Tourists.webp"), 2, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 2, 0, 1, 1)
                elif column_pop in ("Rum.webp", "Advanced_rum_roaster.png"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 2, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 2, 0, 1, 1)
            else:
                if column_pop in ("Champagne.webp", "Jewelry.webp",
                                  "Gramophone.webp",
                                  "Steam_carriages.webp",
                                  "Cigars.webp", "Chocolate.webp",
                                  "Biscuits.webp", "Cognac.webp",
                                  "Billiard_Tables.webp",
                                  "Toys.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "5_Investors.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "5_house_tier05.webp"), 0, 0, 1, 1)  # noqa

                elif column_pop in ("Bowler_hats.webp",
                                    "Icon_hibiscus_tea_0.webp",
                                    "Icon_tapestries_0.webp",
                                    "Icon_wat_stew_0.webp",
                                    "Icon_tobacco_pipes_0.webp",
                                    "Icon_leather_shoes_0.webp",
                                    "Icon_suits_0.webp",
                                    "Icon_telephones_0.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "6_house_tier6.png"), 0, 0, 1, 1)

                else:
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "7_Tourists.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "7_house_tier7.png"), 0, 0, 1, 1)  # noqa

            # 4 column
            column4_frame = QFrame()
            column4_h_box = QHBoxLayout()
            column4_frame.setLayout(column4_h_box)
            table.setCellWidget(row, 3, column4_frame)
            self.column4_le = QLineEdit("100")
            self.column4_le.setValidator(val)
            self.column4_le.setMaxLength(4)
            self.column4_le.setAlignment(Qt.AlignCenter)
            self.column4_le.setMinimumSize(50, 20)
            self.column4_le.setMaximumSize(100, 25)
            self.column4_le.setStyleSheet("background-color: #ced2bc; \
                                font: 12px;border-radius: 3px; \
                                font-style: Roboto")
            column4_la = QLabel()
            column4_la.setAlignment(Qt.AlignCenter)
            column4_la.setMaximumSize(30, 25)
            column4_la.setPixmap(
                QPixmap(":free-icon-percent-4688859.png").scaled(15, 15))
            column4_h_box.addWidget(self.column4_le)
            column4_h_box.addWidget(column4_la)

            # 5 column
            column5_frame = QFrame()
            column5_h_box = QHBoxLayout()
            column5_frame.setLayout(column5_h_box)
            self.column5_la = QLabel("0")
            self.column5_la.setAlignment(Qt.AlignCenter)
            self.column5_la.setStyleSheet("color: black; font-size: 12px")
            column5_h_box.addWidget(self.column5_la)
            table.setCellWidget(row, 4, column5_frame)

            self.column4_le.textChanged.connect(self.onTextChanged)

    elif region == "New_World":
        # создание списков для заполнения таблицы
        column1 = []
        column2 = []
        column3_people = []
        column3_home = []

        for list_dict in json_table[region]:
            column1.append(list(list_dict)[0])
            column2.append(list(list_dict.values())[0][0])
            column3_people.append(list(list_dict.values())[0][1:])

        for list_dict in json_table2[region]:
            column3_home.append(list(list_dict.values())[0][1:])

        table = QTableWidget(15, 5)
        self.table_row_column = {}

        # создание иконок для 3 колонки
        for iz in range(table.rowCount()):
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    pop_label_p = QLabel(self)
                    pop_label_p.move(0, -100)
                    pop_label_p.setAlignment(Qt.AlignRight)
                    pop_label_p.setPixmap(
                        QPixmap(":" + people_icon_id).scaled(25, 25))
                    pop_label_p.setObjectName(f"{people_icon_id}")

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    pop_label_h = QLabel(self)
                    pop_label_h.move(0, -100)
                    pop_label_h.setAlignment(Qt.AlignRight)
                    pop_label_h.setPixmap(
                        QPixmap(":" + home_icon_id).scaled(25, 25))
                    pop_label_h.setObjectName(f"{home_icon_id}")

        for row in range(table.rowCount()):
            # 1 column
            column1_h_box = QHBoxLayout()
            column1_frame = QFrame()
            column1_frame.setLayout(column1_h_box)
            column_pop = column1.pop(0)
            column1_pb = QPushButton(QIcon(":" + column_pop), '')
            column1_pb.setMinimumSize(35, 35)
            column1_pb.setMaximumSize(35, 35)
            column1_pb.setStyleSheet("background-color: brown")
            column1_h_box.addWidget(column1_pb)
            column1_h_box.setContentsMargins(0, 0, 0, 0)
            table.setCellWidget(row, 0, column1_frame)
            # 2 column
            column2_text = QTableWidgetItem(column2.pop(0))
            column2_text.setTextAlignment(Qt.AlignCenter)
            table.setItem(row % 60, 1, column2_text)
            # 3 column
            column3_frame1 = QFrame()
            column3_g_box1 = QGridLayout(column3_frame1)
            column3_frame2 = QFrame()
            column3_g_box2 = QGridLayout(column3_frame2)

            column3_stacked_w = QStackedWidget()
            column3_stacked_w.addWidget(column3_frame1)
            column3_stacked_w.addWidget(column3_frame2)
            table.setCellWidget(row, 2, column3_stacked_w)

            self.table_row_column[row, 2] = column3_stacked_w

            # self.column3_stacked_w.setStyleSheet("border: 3px solid black")
            column3_p_value = column3_people.pop(0)
            column3_h_value = column3_home.pop(0)
            if len(column3_p_value) == 2:
                if column_pop in ("Tortilla.webp",
                                  "Coffee.webp",
                                  "Advanced_coffee_roaster.png",
                                  "Beer.webp", "Beer_Hacienda.png",
                                  "Sewing_machines.webp", "Bowler_hats.webp",
                                  "Cigars.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "9_Obreros.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "9_Obreros.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "9_ObreroResidence.png"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "11_Hacienda_Obrera_Quarters.webp"), 1, 0, 1, 1)  # noqa
                else:
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "8_Jornaleros.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "9_Obreros.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "10_Hacienda_Jornalero_Quarters.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "11_Hacienda_Obrera_Quarters.webp"), 1, 0, 1, 1)  # noqa
            elif len(column3_p_value) == 4:
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 3, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 3, 1, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(
                        QLabel, "8_Jornaleros.webp"), 0, 0, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(
                        QLabel, "9_Obreros.webp"), 1, 0, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(
                        QLabel, "8_Jornaleros.webp"), 2, 0, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(
                        QLabel, "9_Obreros.webp"), 3, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(
                        QLabel, "8_JornaleroResidence.png"), 0, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(
                        QLabel, "9_ObreroResidence.png"), 1, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(
                        QLabel, "10_Hacienda_Jornalero_Quarters.webp"), 2, 0, 1, 1)  # noqa
                column3_g_box2.addWidget(
                    self.findChild(
                        QLabel, "11_Hacienda_Obrera_Quarters.webp"), 3, 0, 1, 1)  # noqa
            else:
                if column_pop == "Schnapps_Hacienda.png":
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "8_Jornaleros.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "10_Hacienda_Jornalero_Quarters.webp"), 0, 0, 1, 1)  # noqa
                else:
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "9_Obreros.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "11_Hacienda_Obrera_Quarters.webp"), 0, 0, 1, 1)  # noqa

            # 4 column
            column4_frame = QFrame()
            column4_h_box = QHBoxLayout()
            column4_frame.setLayout(column4_h_box)
            table.setCellWidget(row, 3, column4_frame)
            self.column4_le = QLineEdit("100")
            self.column4_le.setValidator(val)
            self.column4_le.setMaxLength(4)
            self.column4_le.setAlignment(Qt.AlignCenter)
            self.column4_le.setMinimumSize(50, 20)
            self.column4_le.setMaximumSize(100, 25)
            self.column4_le.setStyleSheet("background-color: #ced2bc; \
                                font: 12px;border-radius: 3px; \
                                font-style: Roboto")
            column4_la = QLabel()
            column4_la.setAlignment(Qt.AlignCenter)
            column4_la.setMaximumSize(30, 25)
            column4_la.setPixmap(
                QPixmap(":free-icon-percent-4688859.png").scaled(15, 15))
            column4_h_box.addWidget(self.column4_le)
            column4_h_box.addWidget(column4_la)
            # 5 column
            column5_frame = QFrame()
            column5_h_box = QHBoxLayout()
            column5_frame.setLayout(column5_h_box)
            self.column5_la = QLabel("0")
            self.column5_la.setAlignment(Qt.AlignCenter)
            self.column5_la.setStyleSheet("color: black; font-size: 12px")
            column5_h_box.addWidget(self.column5_la)
            table.setCellWidget(row, 4, column5_frame)

            self.column4_le.textChanged.connect(
                lambda text=self.column4_le.text(),
                col5=self.column5_la,
                col2=column2_text.text():
                    self.action1(text, col5, col2))

    elif region == "Cape_Trelawney":
        # создание списков для заполнения таблицы
        column1 = []
        column2 = []
        column3_people = []
        column3_home = []

        for list_dict in json_table[region]:
            column1.append(list(list_dict)[0])
            column2.append(list(list_dict.values())[0][0])
            column3_people.append(list(list_dict.values())[0][1:])

        for list_dict in json_table2[region]:
            column3_home.append(list(list_dict.values())[0][1:])

        table = QTableWidget(43, 5)
        self.table_row_column = {}

        # создание иконок для 3 колонки
        for iz in range(table.rowCount()):
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    pop_label_p = QLabel(self)
                    pop_label_p.move(0, -100)
                    pop_label_p.setAlignment(Qt.AlignRight)
                    pop_label_p.setPixmap(
                        QPixmap(":" + people_icon_id).scaled(25, 25))
                    pop_label_p.setObjectName(f"{people_icon_id}")

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    pop_label_h = QLabel(self)
                    pop_label_h.move(0, -100)
                    pop_label_h.setAlignment(Qt.AlignRight)
                    pop_label_h.setPixmap(
                        QPixmap(":" + home_icon_id).scaled(25, 25))
                    pop_label_h.setObjectName(f"{home_icon_id}")

        for row in range(table.rowCount()):
            # 1 column
            column1_h_box = QHBoxLayout()
            column1_frame = QFrame()
            column1_frame.setLayout(column1_h_box)
            column_pop = column1.pop(0)
            column1_pb = QPushButton(QIcon(":" + column_pop), '')
            column1_pb.setMinimumSize(35, 35)
            column1_pb.setMaximumSize(35, 35)
            column1_pb.setStyleSheet("background-color: brown")
            column1_h_box.addWidget(column1_pb)
            column1_h_box.setContentsMargins(0, 0, 0, 0)
            table.setCellWidget(row, 0, column1_frame)
            # 2 column
            column2_text = QTableWidgetItem(column2.pop(0))
            column2_text.setTextAlignment(Qt.AlignCenter)
            table.setItem(row % 60, 1, column2_text)
            # 3 column
            column3_frame1 = QFrame()
            column3_g_box1 = QGridLayout(column3_frame1)
            column3_frame2 = QFrame()
            column3_g_box2 = QGridLayout(column3_frame2)

            column3_stacked_w = QStackedWidget()
            column3_stacked_w.addWidget(column3_frame1)
            column3_stacked_w.addWidget(column3_frame2)
            table.setCellWidget(row, 2, column3_stacked_w)

            self.table_row_column[row, 2] = column3_stacked_w

            column3_p_value = column3_people.pop(0)
            column3_h_value = column3_home.pop(0)
            if len(column3_p_value) == 2:
                if column_pop in ("Fish.webp",
                                  "Schnapps.webp",
                                  "Work_clothes.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "1_Farmers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "2_Workers.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "1_house_tier01.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "2_house_tier02.webp"), 1, 0, 1, 1)
                elif column_pop in ("Sausages.webp", "Bread.webp",
                                    "Soap.webp", "Beer.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "2_Workers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "2_house_tier02.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 1, 0, 1, 1)
                elif column_pop in ("Canned_food.webp",
                                    "Sewing_machines.webp",
                                    "Fur_Coats.webp", "Rum.webp",
                                    "Advanced_rum_roaster.png"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)
                elif column_pop in ("Glasses.webp",
                                    "High_wheeler.webp",
                                    "Pocket_watch.webp",
                                    "Light_bulb.webp", "Coffee.webp",
                                    "Advanced_coffee_roaster.png",
                                    "Chewing_Gum.webp",
                                    "Typewriters.webp",
                                    "Violins.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "4_Engineers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "5_Investors.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "5_house_tier05.webp"), 1, 0, 1, 1)
                elif column_pop in ("Champagne.webp", "Jewelry.webp",
                                    "Gramophone.webp",
                                    "Steam_carriages.webp",
                                    "Cigars.webp", "Chocolate.webp",
                                    "Biscuits.webp", "Cognac.webp",
                                    "Billiard_Tables.webp",
                                    "Toys.webp"):
                    if column_pop == "Jewelry.webp":
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "5_Investors.webp"), 0, 0, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "7_Tourists.webp"), 1, 0, 1, 1)
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "5_house_tier05.webp"), 0, 0, 1, 1)
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "7_house_tier7.png"), 1, 0, 1, 1)
                    else:
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box1.addWidget(
                            QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                        column3_g_box2.addWidget(
                            QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "5_Investors.webp"), 0, 0, 1, 1)
                        column3_g_box1.addWidget(
                            self.findChild(
                                QLabel, "6_Icon_resident_scholars_0.webp"), 1, 0, 1, 1)  # noqa
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "5_house_tier05.webp"), 0, 0, 1, 1)
                        column3_g_box2.addWidget(
                            self.findChild(
                                QLabel, "6_house_tier6.png"), 1, 0, 1, 1)
                elif column_pop in ("Bowler_hats.webp",
                                    "Icon_hibiscus_tea_0.webp",
                                    "Icon_tapestries_0.webp",
                                    "Icon_wat_stew_0.webp",
                                    "Icon_tobacco_pipes_0.webp",
                                    "Icon_leather_shoes_0.webp",
                                    "Icon_suits_0.webp",
                                    "Icon_telephones_0.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "5_Investors.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "6_house_tier6.png"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "5_house_tier05.webp"), 1, 0, 1, 1)
                else:
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "7_Tourists.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "7_Tourists.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 1, 0, 1, 1)

            elif len(column3_p_value) == 3:
                if column_pop == "Bread.webp":
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "2_Workers.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "7_Tourists.webp"), 2, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "2_house_tier02.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 2, 0, 1, 1)
                elif column_pop == "Canned_food.webp":
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 2, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "6_house_tier6.png"), 2, 0, 1, 1)
                elif column_pop == "Fur_Coats.webp":
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "7_Tourists.webp"), 2, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 2, 0, 1, 1)
                elif column_pop in ("Rum.webp",
                                    "Advanced_rum_roaster.png"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 2, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "3_Artisans.webp"), 0, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "4_Engineers.webp"), 1, 0, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 2, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "3_house_tier03.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "4_house_tier04.webp"), 1, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "7_house_tier7.png"), 2, 0, 1, 1)
            else:

                if column_pop in ("Champagne.webp", "Jewelry.webp",
                                  "Gramophone.webp",
                                  "Steam_carriages.webp",
                                  "Cigars.webp", "Chocolate.webp",
                                  "Biscuits.webp", "Cognac.webp",
                                  "Billiard_Tables.webp",
                                  "Toys.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "5_Investors.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "5_house_tier05.webp"), 0, 0, 1, 1)  # noqa

                elif column_pop in ("Bowler_hats.webp",
                                    "Icon_hibiscus_tea_0.webp",
                                    "Icon_tapestries_0.webp",
                                    "Icon_wat_stew_0.webp",
                                    "Icon_tobacco_pipes_0.webp",
                                    "Icon_leather_shoes_0.webp",
                                    "Icon_suits_0.webp",
                                    "Icon_telephones_0.webp"):
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(
                            QLabel, "6_Icon_resident_scholars_0.webp"), 0, 0, 1, 1)  # noqa
                    column3_g_box2.addWidget(
                        self.findChild(
                            QLabel, "6_house_tier6.png"), 0, 0, 1, 1)

                else:
                    column3_g_box1.addWidget(
                        QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box2.addWidget(
                        QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                    column3_g_box1.addWidget(
                        self.findChild(QLabel, "7_Tourists.webp"), 0, 0, 1, 1)
                    column3_g_box2.addWidget(
                        self.findChild(QLabel, "7_house_tier7.png"), 0, 0, 1, 1)  # noqa

            # 4 column
            column4_frame = QFrame()
            column4_h_box = QHBoxLayout()
            column4_frame.setLayout(column4_h_box)
            table.setCellWidget(row, 3, column4_frame)
            self.column4_le = QLineEdit("100")
            self.column4_le.setValidator(val)
            self.column4_le.setMaxLength(4)
            self.column4_le.setAlignment(Qt.AlignCenter)
            self.column4_le.setMinimumSize(50, 20)
            self.column4_le.setMaximumSize(100, 25)
            self.column4_le.setStyleSheet("background-color: #ced2bc; \
                                font: 12px;border-radius: 3px; \
                                font-style: Roboto")
            column4_la = QLabel()
            column4_la.setAlignment(Qt.AlignCenter)
            column4_la.setMaximumSize(30, 25)
            column4_la.setPixmap(
                QPixmap(":free-icon-percent-4688859.png").scaled(15, 15))
            column4_h_box.addWidget(self.column4_le)
            column4_h_box.addWidget(column4_la)
            # 5 column
            column5_frame = QFrame()
            column5_h_box = QHBoxLayout()
            column5_frame.setLayout(column5_h_box)
            self.column5_la = QLabel("0")
            self.column5_la.setAlignment(Qt.AlignCenter)
            self.column5_la.setStyleSheet("color: black; font-size: 12px")
            column5_h_box.addWidget(self.column5_la)
            table.setCellWidget(row, 4, column5_frame)

            self.column4_le.textChanged.connect(
                lambda text=self.column4_le.text(),
                col5=self.column5_la,
                col2=column2_text.text():
                    self.action1(text, col5, col2))

    elif region == "The_Arctic":

        # создание списков для заполнения таблицы
        column1 = []
        column2 = []
        column3_people = []
        column3_home = []

        for list_dict in json_table[region]:
            column1.append(list(list_dict)[0])
            column2.append(list(list_dict.values())[0][0])
            column3_people.append(list(list_dict.values())[0][1:])

        for list_dict in json_table2[region]:
            column3_home.append(list(list_dict.values())[0][1:])

        table = QTableWidget(9, 5)
        self.table_row_column = {}

        # создание иконок для 3 колонки
        for iz in range(table.rowCount()):
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    pop_label_p = QLabel(self)
                    pop_label_p.move(0, -100)
                    pop_label_p.setAlignment(Qt.AlignRight)
                    pop_label_p.setPixmap(
                        QPixmap(":" + people_icon_id).scaled(25, 25))
                    pop_label_p.setObjectName(f"{people_icon_id}")

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    pop_label_h = QLabel(self)
                    pop_label_h.move(0, -100)
                    pop_label_h.setAlignment(Qt.AlignRight)
                    pop_label_h.setPixmap(
                        QPixmap(":" + home_icon_id).scaled(25, 25))
                    pop_label_h.setObjectName(f"{home_icon_id}")

        for row in range(table.rowCount()):
            # 1 column
            column1_h_box = QHBoxLayout()
            column1_frame = QFrame()
            column1_frame.setLayout(column1_h_box)
            column_pop = column1.pop(0)
            column1_pb = QPushButton(QIcon(":" + column_pop), '')
            column1_pb.setMinimumSize(35, 35)
            column1_pb.setMaximumSize(35, 35)
            column1_pb.setStyleSheet("background-color: brown")
            column1_h_box.addWidget(column1_pb)
            column1_h_box.setContentsMargins(0, 0, 0, 0)
            table.setCellWidget(row, 0, column1_frame)
            # 2 column
            column2_text = QTableWidgetItem(column2.pop(0))
            column2_text.setTextAlignment(Qt.AlignCenter)
            table.setItem(row % 60, 1, column2_text)
            # 3 column
            column3_frame1 = QFrame()
            column3_g_box1 = QGridLayout(column3_frame1)
            column3_frame2 = QFrame()
            column3_g_box2 = QGridLayout(column3_frame2)

            column3_stacked_w = QStackedWidget()
            column3_stacked_w.addWidget(column3_frame1)
            column3_stacked_w.addWidget(column3_frame2)
            table.setCellWidget(row, 2, column3_stacked_w)

            self.table_row_column[row, 2] = column3_stacked_w

            column3_p_value = column3_people.pop(0)
            column3_h_value = column3_home.pop(0)
            if len(column3_p_value) == 2:
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(
                        QLabel, "10_Explorers.webp"), 0, 0, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(
                        QLabel, "11_Technicians.webp"), 1, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(
                        QLabel, "Icon_research_resource_0.webp"), 0, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(
                        QLabel, "Icon_research_resource_0.webp"), 1, 0, 1, 1)
            else:
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(QLabel, "11_Technicians.webp"), 0, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(QLabel, "Icon_research_resource_0.webp"), 0, 0, 1, 1)  # noqa

            # 4 column
            column4_frame = QFrame()
            column4_h_box = QHBoxLayout()
            column4_frame.setLayout(column4_h_box)
            table.setCellWidget(row, 3, column4_frame)
            self.column4_le = QLineEdit("100")
            self.column4_le.setValidator(val)
            self.column4_le.setMaxLength(4)
            self.column4_le.setAlignment(Qt.AlignCenter)
            self.column4_le.setMinimumSize(50, 20)
            self.column4_le.setMaximumSize(100, 25)
            self.column4_le.setStyleSheet("background-color: #ced2bc; \
                                font: 12px;border-radius: 3px; \
                                font-style: Roboto")
            column4_la = QLabel()
            column4_la.setAlignment(Qt.AlignCenter)
            column4_la.setMaximumSize(30, 25)
            column4_la.setPixmap(
                QPixmap(":free-icon-percent-4688859.png").scaled(15, 15))
            column4_h_box.addWidget(self.column4_le)
            column4_h_box.addWidget(column4_la)
            # 5 column
            column5_frame = QFrame()
            column5_h_box = QHBoxLayout()
            column5_frame.setLayout(column5_h_box)
            self.column5_la = QLabel("0")
            self.column5_la.setAlignment(Qt.AlignCenter)
            self.column5_la.setStyleSheet("color: black; font-size: 12px")
            column5_h_box.addWidget(self.column5_la)
            table.setCellWidget(row, 4, column5_frame)

            self.column4_le.textChanged.connect(
                lambda text=self.column4_le.text(),
                col5=self.column5_la,
                col2=column2_text.text():
                    self.action1(text, col5, col2))

    elif region == "Enbesa":

        # создание списков для заполнения таблицы
        column1 = []
        column2 = []
        column3_people = []
        column3_home = []

        for list_dict in json_table[region]:
            column1.append(list(list_dict)[0])
            column2.append(list(list_dict.values())[0][0])
            column3_people.append(list(list_dict.values())[0][1:])

        for list_dict in json_table2[region]:
            column3_home.append(list(list_dict.values())[0][1:])

        table = QTableWidget(11, 5)
        self.table_row_column = {}

        # создание иконок для 3 колонки
        for iz in range(table.rowCount()):
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    pop_label_p = QLabel(self)
                    pop_label_p.move(0, -100)
                    pop_label_p.setAlignment(Qt.AlignRight)
                    pop_label_p.setPixmap(
                        QPixmap(":" + people_icon_id).scaled(25, 25))
                    pop_label_p.setObjectName(f"{people_icon_id}")

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    pop_label_h = QLabel(self)
                    pop_label_h.move(0, -100)
                    pop_label_h.setAlignment(Qt.AlignRight)
                    pop_label_h.setPixmap(
                        QPixmap(":" + home_icon_id).scaled(25, 25))
                    pop_label_h.setObjectName(f"{home_icon_id}")

        for row in range(table.rowCount()):
            # 1 column
            column1_h_box = QHBoxLayout()
            column1_frame = QFrame()
            column1_frame.setLayout(column1_h_box)
            column_pop = column1.pop(0)
            column1_pb = QPushButton(QIcon(":" + column_pop), '')
            column1_pb.setMinimumSize(35, 35)
            column1_pb.setMaximumSize(35, 35)
            column1_pb.setStyleSheet("background-color: brown")
            column1_h_box.addWidget(column1_pb)
            column1_h_box.setContentsMargins(0, 0, 0, 0)
            table.setCellWidget(row, 0, column1_frame)
            # 2 column
            column2_text = QTableWidgetItem(column2.pop(0))
            column2_text.setTextAlignment(Qt.AlignCenter)
            table.setItem(row % 60, 1, column2_text)
            # 3 column
            column3_frame1 = QFrame()
            column3_g_box1 = QGridLayout(column3_frame1)
            column3_frame2 = QFrame()
            column3_g_box2 = QGridLayout(column3_frame2)

            column3_stacked_w = QStackedWidget()
            column3_stacked_w.addWidget(column3_frame1)
            column3_stacked_w.addWidget(column3_frame2)
            table.setCellWidget(row, 2, column3_stacked_w)

            self.table_row_column[row, 2] = column3_stacked_w

            column3_p_value = column3_people.pop(0)
            column3_h_value = column3_home.pop(0)
            if len(column3_p_value) == 2:
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 1, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 1, 1, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(QLabel, "12_Icon_resident_sheperd_0.webp"),
                    0, 0, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(QLabel, "13_Icon_resident_elder_0.webp"),
                    1, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(QLabel, "Icon_research_resource_0.webp"),
                    0, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(QLabel, "Icon_research_resource_0.webp"),
                    1, 0, 1, 1)
            else:
                column3_g_box1.addWidget(
                    QLabel(column3_p_value.pop(0)), 0, 1, 1, 1)
                column3_g_box2.addWidget(
                    QLabel(column3_h_value.pop(0)), 0, 1, 1, 1)
                column3_g_box1.addWidget(
                    self.findChild(
                        QLabel, "13_Icon_resident_elder_0.webp"), 0, 0, 1, 1)
                column3_g_box2.addWidget(
                    self.findChild(
                        QLabel, "Icon_research_resource_0.webp"), 0, 0, 1, 1)

            # 4 column
            column4_frame = QFrame()
            column4_h_box = QHBoxLayout()
            column4_frame.setLayout(column4_h_box)
            table.setCellWidget(row, 3, column4_frame)
            self.column4_le = QLineEdit("100")
            self.column4_le.setValidator(val)
            self.column4_le.setMaxLength(4)
            self.column4_le.setAlignment(Qt.AlignCenter)
            self.column4_le.setMinimumSize(50, 20)
            self.column4_le.setMaximumSize(100, 25)
            self.column4_le.setStyleSheet("background-color: #ced2bc; \
                                font: 12px;border-radius: 3px; \
                                font-style: Roboto")
            column4_la = QLabel()
            column4_la.setAlignment(Qt.AlignCenter)
            column4_la.setMaximumSize(30, 25)
            column4_la.setPixmap(
                QPixmap(":free-icon-percent-4688859.png").scaled(15, 15))
            column4_h_box.addWidget(self.column4_le)
            column4_h_box.addWidget(column4_la)
            # 5 column
            column5_frame = QFrame()
            column5_h_box = QHBoxLayout()
            column5_frame.setLayout(column5_h_box)
            self.column5_la = QLabel("0")
            self.column5_la.setAlignment(Qt.AlignCenter)
            self.column5_la.setStyleSheet("color: black; font-size: 12px")
            column5_h_box.addWidget(self.column5_la)
            table.setCellWidget(row, 4, column5_frame)

            self.column4_le.textChanged.connect(
                lambda text=self.column4_le.text(),
                col5=self.column5_la,
                col2=column2_text.text():
                    self.action1(text, col5, col2))
    # Стиль таблицы
    delegate = HighlightDelegate(table)
    table.setItemDelegate(delegate)

    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalPolicy(0)
    sizePolicy.setHeightForWidth(table.sizePolicy().hasHeightForWidth())
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
    return table
