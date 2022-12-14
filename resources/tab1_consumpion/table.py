"""Doc."""
import json
from PyQt5.QtWidgets import QLineEdit, QLabel, QHBoxLayout, \
    QTableWidget, QFrame, QAbstractItemView, \
    QStackedWidget, QTableWidgetItem, QFormLayout
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt  # noqa
from resources import gui_icons  # noqa
from painter import PushButton_G


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


def _createtable(self, region: str) -> QTableWidget:

    valid = QtCore.QRegExp("[0-9 .,]{15}")
    val = QtGui.QRegExpValidator(valid)

    # self.column1 - products list
    # self.column2 - products base output list
    # self.column3_people/column3_home - consumer: consumtion dict list list
    self.column1 = []
    self.column2 = []
    self.column3_people = []
    self.column3_home = []

    def createtable_info(region):
        """Retrieve data from json."""
        for list_dict in json_table[region]:
            self.column1.append(list(list_dict)[0])
            self.column2.append(list(list_dict.values())[0][0])
            self.column3_people.append(list(list_dict.values())[0][1:])

        for list_dict in json_table2[region]:
            self.column3_home.append(list(list_dict.values())[0][1:])
    createtable_info(region)

    if region == "Old_World":
        table = QTableWidget(len(self.column1) - 1, 5)
        self.table_row_column = {}
    elif region == "New_World":
        table = QTableWidget(len(self.column1) - 1, 5)
        self.table_row_column = {}
    elif region == "Cape_Trelawney":
        table = QTableWidget(len(self.column1) - 1, 5)
        self.table_row_column = {}
    elif region == "The_Arctic":
        table = QTableWidget(len(self.column1) - 1, 5)
        self.table_row_column = {}
    elif region == "Enbesa":
        table = QTableWidget(len(self.column1) - 1, 5)
        self.table_row_column = {}

    def completetable():

        for row in range(table.rowCount()):
            # 1 column
            column1_frame = QFrame()
            column1_h_box = QHBoxLayout()
            column1_frame.setLayout(column1_h_box)

            column1_pb = PushButton_G(self.column1[row])
            column1_pb.setMinimumSize(35, 35)
            column1_pb.setMaximumSize(55, 45)
            column1_h_box.addWidget(column1_pb)
            table.setCellWidget(row, 0, column1_frame)

            # 2 column
            self.column2_text = QTableWidgetItem(self.column2[row])
            self.column2_text.setTextAlignment(Qt.AlignCenter)
            table.setItem(row, 1, self.column2_text)

            # 3 column
            def complete_3column() -> QStackedWidget:
                column3_stacked_w = QStackedWidget()
                frame = QFrame()
                frame.setStyleSheet("border: 2px solid red;")
                fbox1 = QFormLayout(frame)
                fbox1.setVerticalSpacing(15)
                fbox1.setFieldGrowthPolicy(fbox1.FieldsStayAtSizeHint)
                fbox1.setRowWrapPolicy(fbox1.DontWrapRows)
                #########
                fbox1.setFormAlignment(Qt.AlignCenter)
                fbox1.setLabelAlignment(Qt.AlignVCenter)
                ##########
                frame2 = QFrame()
                fbox2 = QFormLayout(frame2)
                column3_stacked_w.addWidget(frame)
                column3_stacked_w.addWidget(frame2)
                fbox2.setFieldGrowthPolicy(fbox2.FieldsStayAtSizeHint)
                fbox2.setRowWrapPolicy(fbox2.DontWrapRows)

                # creating a dictionary for indexing
                # Toggle widget inside region's st.widget -> city st.widget
                self.table_row_column[row, 2] = column3_stacked_w

                def distribute_population(tp_list):
                    # column3_people[row] - consumers count
                    for i in tp_list[row]:
                        icon_label = QLabel()
                        icon_label.setObjectName(f"{i}")
                        icon_label.setMinimumSize(25, 30)
                        icon_label.setStyleSheet("border: 2px solid black")
                        icon_pixmap = QPixmap(
                            ":" + list(tp_list[row]
                                       [tp_list[row].index(i)].keys())
                            [0]).scaled(25, 25,
                                        transformMode=Qt.SmoothTransformation)
                        icon_label.setPixmap(icon_pixmap)
                        text_label = QLabel(list(
                            tp_list[row][tp_list[row].index(i)].values())[0])
                        #####################
                        text_label.setMinimumSize(55, 30)
                        #####################
                        if tp_list == self.column3_people:
                            fbox1.addRow(icon_label, text_label)  # noqa
                        else:
                            fbox2.addRow(icon_label, text_label)  # noqa

                distribute_population(self.column3_people)
                distribute_population(self.column3_home)

                return column3_stacked_w

            table.setCellWidget(row, 2, complete_3column())

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

            column4_la = QLabel()
            column4_la.setAlignment(Qt.AlignCenter)
            column4_la.setMaximumSize(30, 25)
            column4_la.setPixmap(
                QPixmap(":free-icon-percent-4688859.png").scaled(
                    15, 15, transformMode=Qt.SmoothTransformation))
            column4_h_box.addWidget(self.column4_le)
            column4_h_box.addWidget(column4_la)

            # 5 column
            column5_frame = QFrame()
            column5_h_box = QHBoxLayout()
            column5_frame.setLayout(column5_h_box)

            self.column5_la = QLabel("0")
            self.column5_la.setAlignment(Qt.AlignCenter)
            column5_h_box.addWidget(self.column5_la)
            table.setCellWidget(row, 4, column5_frame)
            ##############
            self.column4_le.textChanged.connect(self.onTextChanged)
            self.column4_le.textChanged.connect(
                lambda text=self.column4_le.text(),
                col5=self.column5_la,
                col2=self.column2_text.text():
                    self.action1(text, col5, col2))

    completetable()

    # Table style
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
    table.setFrameShadow(QtWidgets.QFrame.Raised)
    table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    table.setShowGrid(False)
    table.verticalHeader().setVisible(False)
    table.setSelectionMode(QAbstractItemView.NoSelection)
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    table.setFocusPolicy(Qt.NoFocus)
    table.setHorizontalHeaderLabels([
        'Product', 'Base\noutput',
        'Base\nconsumption',
        'Productivity',
        'Buildings\nRequired'
    ])
    table.horizontalHeader().setSectionResizeMode(
        QtWidgets.QHeaderView.Stretch)
    if region == "The_Arctic" or "Enbesa":
        table.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        table.verticalHeader().setMinimumSectionSize(75)
    else:
        table.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)

    table.setStyleSheet("""font-size: 16px; font-family: Heuristica""")
    return table
