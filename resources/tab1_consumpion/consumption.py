"""Doc."""
import sys
import os
import json
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, \
     QHBoxLayout, QVBoxLayout, QLayout, QFormLayout, QFrame,  QSizePolicy, \
     QScrollArea,  QStackedWidget, QSpacerItem   # noqa
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
sys.path.append(os.path.abspath('resources/tab1_consumpion'))
from resources import gui_icons  # noqa
from table import _createtable  # noqa
from painter import *  # noqa
from resources.tab1_consumpion.tpForm import _setPopulation

with open("resources\\tab1_consumpion\\consumption_data_p.json") as p:
    json_table = json.load(p)
with open("resources\\tab1_consumpion\\consumption_data_h.json") as h:
    json_table2 = json.load(h)


def _consumptiontab(self) -> QFrame:

    # макет с "Buttons and form type population" ,
    # "Search and table","Region and City"
    tp_table_rc_f = QFrame()
    tp_table_rc_hbox = QHBoxLayout()
    tp_table_rc_hbox.setContentsMargins(0, 0, 0, 0)
    tp_table_rc_f.setLayout(tp_table_rc_hbox)

    ##############################################################
    # TYPE POPULATION BUTTONS AND FORM
    tpBtnForm_f = Frame_tp()
    tpBtnForm_f.setMinimumSize(100, 170)
    tpBtnForm_vbox = QVBoxLayout()
    tpBtnForm_vbox.setContentsMargins(0, 0, 0, 0)
    tpBtnForm_vbox.setSpacing(5)
    tpBtnForm_f.setLayout(tpBtnForm_vbox)

    popBtnLabel_f = Frame_label("Population")
    tpBtn_hbox = QHBoxLayout()
    tpBtn_hbox.setContentsMargins(10, 50, 10, 43)
    tpBtn_hbox.setSpacing(25)
    tpBtn_hbox.setAlignment(Qt.AlignCenter)
    popBtnLabel_f.setLayout(tpBtn_hbox)

    tpBtnForm_vbox.addWidget(popBtnLabel_f)

    self.people_btn = PushButton_TP("Population")
    self.people_btn.setMinimumSize(50, 25)
    self.people_btn.clicked.connect(
        lambda: self.column3_stacked_w("People"))
    self.people_btn.clicked.connect(
        lambda: self.forms_stackedW("type_1"))

    self.house_btn = PushButton_TP("Buildings")
    self.house_btn.setMinimumSize(50, 25)
    self.house_btn.clicked.connect(
        lambda: self.column3_stacked_w("Home"))
    self.house_btn.clicked.connect(
        lambda: self.forms_stackedW("type_2"))

    tpBtn_hbox.addWidget(self.people_btn)
    tpBtn_hbox.addWidget(self.house_btn)

    self.stacked_form_count = {}
    # Form_StackedW

    form_1 = _setPopulation(self, "Old_World", 0, 0)
    self.cityForm_stackedW0 = QStackedWidget()
    self.cityForm_stackedW0.addWidget(form_1)

    form_2 = _setPopulation(self, "New_World", 1, 0)
    self.cityForm_stackedW1 = QStackedWidget()
    self.cityForm_stackedW1.addWidget(form_2)

    form_3 = _setPopulation(self, "Cape_Trelawney", 2, 0)
    self.cityForm_stackedW2 = QStackedWidget()
    self.cityForm_stackedW2.addWidget(form_3)

    form_4 = _setPopulation(self, "The_Arctic", 3, 0)
    self.cityForm_stackedW3 = QStackedWidget()
    self.cityForm_stackedW3.addWidget(form_4)

    form_5 = _setPopulation(self, "Enbesa", 4, 0)
    self.cityForm_stackedW4 = QStackedWidget()
    self.cityForm_stackedW4.addWidget(form_5)

    self.cityForm_stackedW = QStackedWidget()

    self.cityForm_stackedW.addWidget(self.cityForm_stackedW0)
    self.cityForm_stackedW.addWidget(self.cityForm_stackedW1)
    self.cityForm_stackedW.addWidget(self.cityForm_stackedW2)
    self.cityForm_stackedW.addWidget(self.cityForm_stackedW3)
    self.cityForm_stackedW.addWidget(self.cityForm_stackedW4)

    self.regionForm_stackedW = QStackedWidget()
    self.regionForm_stackedW.addWidget(self.cityForm_stackedW)  # Main city
    # self.regionForm_stackedW.addWidget(form_1)
    # self.regionForm_stackedW.addWidget(form_2)
    # self.regionForm_stackedW.addWidget(form_3)
    # self.regionForm_stackedW.addWidget(form_4)
    # self.regionForm_stackedW.addWidget(form_5)

    tpBtnForm_vbox.addWidget(self.regionForm_stackedW)

    tp_table_rc_hbox.addWidget(tpBtnForm_f)
    ############################################################
    # поиск и кпопка поиска
    self.search_box = QHBoxLayout()
    self.searchTable_vbox = QVBoxLayout()  # таблица и поиск
    self.searchTable_vbox.setSizeConstraint(QLayout.SetMaximumSize)
    self.searchTable_vbox.setContentsMargins(0, -1, -1, -1)
    self.searchTable_vbox.setSpacing(5)

    req_label_frame = Frame_label("Requirements")
    reqLabel_hbox = QHBoxLayout()
    reqLabel_hbox.setSpacing(0)
    reqLabel_hbox.setContentsMargins(0, 10, 0, 21)
    req_label_frame.setLayout(reqLabel_hbox)

    self.searchTable_vbox.addWidget(req_label_frame)

    searchbutton = PushButton_F('Filters')
    searchbutton.setMinimumSize(100, 20)

    searchedit = QLineEdit()
    searchedit.setObjectName("search_e")

    word_list = ["fish", "schnapps", "work clothes", "sausages"]

    completer = QCompleter(word_list, self)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    searchedit.setCompleter(completer)

    searchedit.setMinimumSize(290, 20)
    self.search_box.addWidget(searchbutton)
    self.search_box.addWidget(searchedit)
    self.search_box.addSpacerItem(QSpacerItem(100, 0,
                                  QSizePolicy.Maximum, QSizePolicy.Fixed))
    self.searchTable_vbox.addLayout(self.search_box)

    self.table_count = []
    table_1 = _createtable(self, "Old_World")
    self.table_count.append(self.table_row_column)
    table_2 = _createtable(self, "New_World")
    self.table_count.append(self.table_row_column)
    table_3 = _createtable(self, "Cape_Trelawney")
    self.table_count.append(self.table_row_column)
    table_4 = _createtable(self, "The_Arctic")
    self.table_count.append(self.table_row_column)
    table_5 = _createtable(self, "Enbesa")
    self.table_count.append(self.table_row_column)

    self.regionTable_stackedW = QStackedWidget()
    self.regionTable_stackedW.setContentsMargins(0, 0, 0, 0)

    self.regionTable_stackedW.addWidget(table_1)
    self.regionTable_stackedW.addWidget(table_2)
    self.regionTable_stackedW.addWidget(table_3)
    self.regionTable_stackedW.addWidget(table_4)
    self.regionTable_stackedW.addWidget(table_5)

    self.searchTable_vbox.addWidget(self.regionTable_stackedW)

    # self.city_select_stacked_w_t = QStackedWidget()
    # self.city_select_stacked_w_t.addWidget(self.regionTable_stackedW)
    # self.searchTable_vbox.addWidget(self.city_select_stacked_w_t)

    tp_table_rc_hbox.addLayout(self.searchTable_vbox)
    #######################################################################
    # макет кнопок выбора региона
    region_box = QHBoxLayout()
    region_box.setSizeConstraint(QLayout.SetDefaultConstraint)
    region_box.setContentsMargins(0, 0, 0, 0)
    region_box.setSpacing(0)
    # макет выбора региона и добавление города
    regionCity_vbox = QVBoxLayout()
    regionCity_vbox.setSizeConstraint(QLayout.SetDefaultConstraint)
    regionCity_vbox.setAlignment(Qt.AlignTop)
    regionCity_vbox.setContentsMargins(0, 0, 0, 0)
    regionCity_vbox.setSpacing(5)

    city_label_frame = Frame_label("City")
    city_label_frame.setMinimumSize(170, 0)
    city_label_box = QVBoxLayout()
    city_label_box.setSpacing(0)
    city_label_box.setContentsMargins(7, 50, 7, 43)
    city_label_box.setAlignment(Qt.AlignCenter)
    city_label_frame.setLayout(city_label_box)

    regionCity_vbox.addWidget(city_label_frame)

    def create_region_btn(self, region: str, index: int) -> QAbstractButton:

        btn = PushButton_R(region)
        btn.setMinimumSize(32, 23)
        btn.clicked.connect(
            lambda: self.regionTable_stackedW.setCurrentIndex(index))
        btn.clicked.connect(
            lambda: self.cityForm_stackedW.setCurrentIndex(index))
        btn.clicked.connect(
            lambda: self.city_stacked_w.setCurrentIndex(index))
        btn.setObjectName(region)
        return btn

    region1 = create_region_btn(self, "Old_World", 0)
    region2 = create_region_btn(self, "New_World", 1)
    region3 = create_region_btn(self, "Cape_Trelawney", 2)
    region4 = create_region_btn(self, "The_Arctic", 3)
    region5 = create_region_btn(self, "Enbesa", 4)

    region_box.addWidget(region1)
    region_box.addWidget(region2)
    region_box.addWidget(region3)
    region_box.addWidget(region4)
    region_box.addWidget(region5)

    city_label_box.addLayout(region_box)

    self.city_count = {}

    def _createCity(self, region, index_stacked_wi):
        """Doc."""
        # макет кнопок добавления города
        self.city_box = QVBoxLayout()
        self.city_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.city_box.setContentsMargins(0, 0, 0, 0)
        self.city_box.setSpacing(0)
        self.city_box.setObjectName("City")
        self.city_box.setAlignment(Qt.AlignTop)

        self.city_scrollArea = QScrollArea(self)
        self.city_scrollArea.setObjectName("Scroll_Area")

        self.city_widget = QWidget()
        self.city_widget.setObjectName("City_widget")

        self.city_box_2 = QVBoxLayout(self.city_widget)
        self.city_box_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.city_box_2.setContentsMargins(0, 0, 0, 0)
        self.city_box_2.setSpacing(0)
        self.city_box_2.setAlignment(Qt.AlignTop)

        self.city_count[index_stacked_wi] = self.city_box_2
        self.reg = region

        if region == "Old_World":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = PushButton_C('Main city \n Population:')
            city1.setMinimumSize(100, 40)
            city1.setObjectName("Main_city")
            city1.clicked.connect(
                lambda: self.cityForm_stackedW0.setCurrentIndex(0))
            city1.clicked.connect(
                lambda: print(self.cityForm_stackedW0.currentIndex()))
            # city1.clicked.connect(
            #     lambda: self.city_select_stacked_w_t.setCurrentIndex(0))
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = PushButton_AC('+', self)
            self.anothercity.setMinimumSize(100, 25)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2,
                reg=self.reg: self.add_city(pb, layout, reg))

        elif region == "New_World":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = PushButton_C('Main city \n Population:')
            city1.setMinimumSize(100, 40)
            # city1.clicked.connect(
            #     lambda: self.citySelectForm_stackedW.setCurrentIndex(0))
            # city1.clicked.connect(
            #     lambda: self.city_select_stacked_w_t.setCurrentIndex(0))
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = PushButton_AC('+', self)
            self.anothercity.setMinimumSize(100, 25)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        elif region == "Cape_Trelawney":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = PushButton_C('Main city \n Population:')
            city1.setMinimumSize(100, 40)
            # city1.clicked.connect(
            #     lambda: self.citySelectForm_stackedW.setCurrentIndex(0))
            # city1.clicked.connect(
            #     lambda: self.city_select_stacked_w_t.setCurrentIndex(0))
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = PushButton_AC('+', self)
            self.anothercity.setMinimumSize(100, 25)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        elif region == "The_Arctic":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = PushButton_C('Main city \n Population:')
            city1.setMinimumSize(100, 40)
            # city1.clicked.connect(
            #     lambda: self.citySelectForm_stackedW.setCurrentIndex(0))
            # city1.clicked.connect(
            #     lambda: self.city_select_stacked_w_t.setCurrentIndex(0))
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = PushButton_AC('+', self)
            self.anothercity.setMinimumSize(100, 25)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        elif region == "Enbesa":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = PushButton_C('Main city \n Population:')
            city1.setMinimumSize(100, 40)
            # city1.clicked.connect(
            #     lambda: self.citySelectForm_stackedW.setCurrentIndex(0))
            # city1.clicked.connect(
            #     lambda: self.city_select_stacked_w_t.setCurrentIndex(0))
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = PushButton_AC('+', self)
            self.anothercity.setMinimumSize(100, 25)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        return self.city_box

    create_city = _createCity(self, "Old_World", 0)
    create_city2 = _createCity(self, "New_World", 1)
    create_city3 = _createCity(self, "Old_World", 2)
    create_city4 = _createCity(self, "The_Arctic", 3)
    create_city5 = _createCity(self, "Enbesa", 4)

    cc = [create_city, create_city2, create_city3, create_city4, create_city5]
    self.city_stacked_w = QStackedWidget()

    for i in cc:
        self.city_frame = QFrame()
        self.city_frame.setLayout(i)
        self.city_stacked_w.addWidget(self.city_frame)

    regionCity_vbox.addWidget(self.city_stacked_w)
    regionCity_vbox.setAlignment(Qt.AlignTop)

    tp_table_rc_hbox.addLayout(regionCity_vbox)
    tp_table_rc_hbox.setStretch(1, 1)

    return tp_table_rc_f
