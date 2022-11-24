"""Doc."""
import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QAction, QMainWindow, QMenu, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLayout, \
    QFormLayout, QFrame, QAbstractItemView, QSpacerItem, QSizePolicy, \
    QTabWidget, QScrollArea  # noqa
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
sys.path.append(os.path.abspath('resourсes/'))
import gui_icons  # noqa
from table import _createtable  # noqa


with open("resourсes\\consumption_data_h.json") as f:
    json_table = json.load(f)
with open("resourсes\\consumption_data_p.json") as g:
    json_table2 = json.load(g)


def _consumptiontab(self):

    type_polutation_box = QHBoxLayout()  # макет кнопок слева сверху
    type_polutation_box.setSizeConstraint(QLayout.SetDefaultConstraint)
    type_polutation_box.setContentsMargins(0, 0, 0, 0)
    type_polutation_box.setSpacing(0)
    type_polutation_box.setObjectName("Type Population Button")
    la_le_box = QFormLayout()  # форма для лейблов и едитов
    la_le_box.setSizeConstraint(QLayout.SetDefaultConstraint)
    la_le_box.setFieldGrowthPolicy(la_le_box.FieldsStayAtSizeHint)
    la_le_box.setRowWrapPolicy(la_le_box.DontWrapRows)
    la_le_box.setLabelAlignment(Qt. AlignRight | Qt. AlignTrailing
                                | Qt. AlignVCenter)
    la_le_box.setFormAlignment(Qt.AlignLeading
                               | Qt.AlignLeft | Qt.AlignVCenter)
    la_le_box.setContentsMargins(50, 70, 50, 80)
    la_le_box.setVerticalSpacing(3)
    la_le_box.setObjectName("type population form")
    pop_label_box = QVBoxLayout()  # макет лейблов слева снизу
    pop_label_box.setContentsMargins(0, 0, 0, 0)
    pop_label_box.setObjectName("Labels with type population")
    pop_le_box = QVBoxLayout()  # макет окон редактирования слева снизу
    pop_le_box.setContentsMargins(0, 5, 0, -1)
    pop_le_box.setSpacing(10)
    pop_le_box.setObjectName("Population type edit line")
    buttons_form = QVBoxLayout()  # макет слева снизу(хбох5,хбох6)
    buttons_form.setSizeConstraint(QLayout.SetDefaultConstraint)
    buttons_form.setContentsMargins(-1, -1, 0, -1)
    buttons_form.setSpacing(5)
    buttons_form.setObjectName("Buttons and form type population")
    search_box = QHBoxLayout()  # поиск и кпопка поиска
    search_table_box = QVBoxLayout()  # таблица и поиск
    search_table_box.setSizeConstraint(QLayout.SetMaximumSize)
    search_table_box.setContentsMargins(0, -1, -1, -1)
    search_table_box.setSpacing(5)
    search_table_box.setObjectName("Search and table")
    region_box = QHBoxLayout()  # макет кнопок справа сверху
    region_box.setSizeConstraint(QLayout.SetDefaultConstraint)
    region_box.setContentsMargins(0, 0, 0, 0)
    region_box.setSpacing(0)
    region_box.setObjectName("Region")

    region_city_box = QVBoxLayout()  # макет справа (хбох7,вбох4)
    region_city_box.setSizeConstraint(QLayout.SetFixedSize)
    region_city_box.setAlignment(Qt.AlignTop)
    region_city_box.setContentsMargins(0, 0, 0, 0)
    region_city_box.setSpacing(5)
    region_city_box.setObjectName("Region and City")
    tp_table_rc = QHBoxLayout()  # основные макеты (вбох5, таблица, вбох6)
    tp_table_rc.setObjectName("TypePopulation, Table, AddCity")
    pop_label = QLabel("Population")
    sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,  QtWidgets.QSizePolicy.Fixed)
    pop_label.setSizePolicy(sizePolicy)
    pop_label.setAlignment(Qt.AlignCenter)
    pop_label.setObjectName("Type_of_population")
    req_label = QLabel("Requirements")
    req_label.setAlignment(Qt.AlignCenter)
    req_label.setObjectName("Requirements")

    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalPolicy(0)
    sizePolicy.setHeightForWidth(
               req_label.sizePolicy().hasHeightForWidth())
    sizePolicy = QtWidgets.QSizePolicy(
                 QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    req_label.setSizePolicy(sizePolicy)
    city_label = QLabel("City")
    city_label.setAlignment(Qt.AlignCenter)
    city_label.setObjectName("City")
    buttons_form.addWidget(pop_label)
    search_table_box.addWidget(req_label)
    region_city_box.addWidget(city_label)
    people_btn = QPushButton(QIcon(':Population.webp'), '')
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalPolicy(0)
    sizePolicy.setHeightForWidth(
        people_btn.sizePolicy().hasHeightForWidth())
    people_btn.setSizePolicy(sizePolicy)
    people_btn.setMaximumSize(50, 25)
    people_btn.setObjectName("people_btn")
    # people_btn.setStyleSheet("background-color: #ced2bc;
    # font: 12px;border-radius: 3px;font-style: Roboto")
    house_btn = QPushButton(QIcon(':3d_storage.png'), '')
    sizePolicy2 = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Fixed)
    sizePolicy2.setHorizontalStretch(1)
    sizePolicy2.setVerticalPolicy(0)
    sizePolicy2.setHeightForWidth(
        house_btn.sizePolicy().hasHeightForWidth())
    house_btn.setSizePolicy(sizePolicy2)
    house_btn.setMaximumSize(50, 25)
    house_btn.setObjectName("house_btn")
    # house_btn.setStyleSheet("background-color: #ced2bc;
    # font: 12px;border-radius: 3px;font-style: Roboto")
    type_polutation_box.addWidget(people_btn)
    type_polutation_box.addWidget(house_btn)
    type_polutation_box.setStretch(1, 1)
    buttons_form.addLayout(type_polutation_box)

    def _setPopulation():
        valid = QtCore.QRegExp("[0-9 .,]{15}")
        val = QtGui.QRegExpValidator(valid)
        farmer_lab = QPixmap(":1_Farmers.webp")
        lbl = QLabel()
        lbl.setPixmap(farmer_lab)
        worker_lab = QPixmap(":2_Workers.webp")
        lbl2 = QLabel()
        lbl2.setPixmap(worker_lab)
        artisan_lab = QPixmap(":3_Artisans.webp")
        lbl3 = QLabel()
        lbl3.setPixmap(artisan_lab)
        engineer_lab = QPixmap(":4_Engineers.webp")
        lbl4 = QLabel()
        lbl4.setPixmap(engineer_lab)
        investor_lab = QPixmap(":5_Investors.webp")
        lbl5 = QLabel()
        lbl5.setPixmap(investor_lab)
        scholar_lab = QPixmap(":6_Icon_resident_scholars_0.webp")
        lbl6 = QLabel()
        lbl6.setPixmap(scholar_lab)
        tourist_lab = QPixmap(":7_Tourists.webp")
        lbl7 = QLabel()
        lbl7.setPixmap(tourist_lab)
        lbls = [lbl, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7]
        for lay in lbls:
            lay.setMinimumSize(30, 30)
            lay.setMaximumSize(40, 40)
            lay.setScaledContents(True)
            pop_label_box.addWidget(lay)

        pop_label_box.setStretch(1, 1)
        farmer_edit = QLineEdit()
        worker_edit = QLineEdit()
        artisan_edit = QLineEdit()
        engineer_edit = QLineEdit()
        investor_edit = QLineEdit()
        tourist_edit = QLineEdit()
        scholar_edit = QLineEdit()
        edit_list = [farmer_edit, worker_edit, artisan_edit, engineer_edit,
                     investor_edit, scholar_edit, tourist_edit]

        for m in edit_list:
            m.setMinimumSize(30, 30)
            m.setMaximumSize(45, 30)
            m.setValidator(val)
            m.setMaxLength(4)
            pop_le_box.addWidget(m)
            m.textChanged.connect(self.onTextChanged)

        la_le_box.setLayout(0, QFormLayout.LabelRole, pop_label_box)
        la_le_box.setLayout(0, QFormLayout.FieldRole, pop_le_box)
        buttons_form.addLayout(la_le_box)
        tp_table_rc.addLayout(buttons_form)

        house_btn.clicked.connect(self.onClicked)
        people_btn.clicked.connect(
                lambda pb=people_btn,
                laybels=lbls: self.action_people_btn(pb, laybels))
        house_btn.clicked.connect(
                lambda pb=house_btn, edem=edit_list,
                laybels=lbls, plb=pop_le_box: self.action_house_btn(
                                             pb, edem, laybels, plb))


    spisok_edit = _setPopulation()
    searchbutton = QPushButton('Filters')
    searchbutton.setStyleSheet("background-color: #ced2bc; \
                  font: 12px;border-radius: 3px;font-style: Roboto")
    searchbutton.setMinimumSize(100, 20)
    searchedit = QLineEdit()
    searchedit.setMinimumSize(290, 20)
    search_box.addWidget(searchbutton)
    search_box.addWidget(searchedit)
    search_box.addSpacerItem(QSpacerItem(100, 0,
                             QSizePolicy.Maximum, QSizePolicy.Fixed))
    search_table_box.addLayout(search_box)
    create_table = _createtable(self)

    search_table_box.addWidget(create_table)
    search_table_box.setStretch(2, 1)
    tp_table_rc.addLayout(search_table_box)

    region1 = QPushButton(QIcon(':oldworld_.webp'), '')
    region2 = QPushButton(QIcon(':newworld_.webp'), '')
    region3 = QPushButton(QIcon(':capetrelawney_.webp'), '')
    region4 = QPushButton(QIcon(':arctic_.webp'), '')
    region5 = QPushButton(QIcon(':enbesa_.webp'), '')

    region_box.addWidget(region1)
    region_box.addWidget(region2)
    region_box.addWidget(region3)
    region_box.addWidget(region4)
    region_box.addWidget(region5)
    region_city_box.addLayout(region_box)

    def _createCity(self):
        self.city_box = QVBoxLayout()  # макет кнопок справа снизу
        self.city_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.city_box.setContentsMargins(0, 0, 0, 0)
        self.city_box.setSpacing(0)
        self.city_box.setObjectName("City")

        self.city_scrollArea = QScrollArea(self)
        self.city_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.city_widget = QWidget()
        self.city_box_2 = QVBoxLayout(self.city_widget)
        self.city_scrollArea.setWidget(self.city_widget)
        self.city_scrollArea.setWidgetResizable(True)
        self.city_box_2.addWidget(self.city_scrollArea)

        city1 = QPushButton('Main city \n Population:')
        self.button = 1
        self.anothercity = QPushButton('+', self)



        self.anothercity.clicked.connect(
            lambda x, pb = self.anothercity,layout=self.city_box: self.add_city(pb, layout))


        # anothercity.clicked.connect(anothercity.deleteLater)

        self.city_box.addWidget(city1)
        self.city_box.addWidget(self.anothercity)
        region_city_box.addLayout(self.city_box)
        tp_table_rc.addLayout(region_city_box)
        tp_table_rc.setStretch(1, 1)
    _createCity(self)
    return tp_table_rc, create_table, spisok_edit