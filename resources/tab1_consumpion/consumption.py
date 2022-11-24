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

with open("resources\\tab1_consumpion\\consumption_data_p.json") as p:
    json_table = json.load(p)
with open("resources\\tab1_consumpion\\consumption_data_h.json") as h:
    json_table2 = json.load(h)


def _consumptiontab(self):

    # макет с "Buttons and form type population" ,
    # "Search and table","Region and City"
    tp_table_rc_hbox = QHBoxLayout()
    tp_table_rc_hbox.setContentsMargins(0, 0, 0, 0)
    tp_table_rc_f = QFrame()
    tp_table_rc_f.setLayout(tp_table_rc_hbox)

    ##############################################################
    # TYPE POPULATION BUTTONS AND FORM
    tpBtnForm_f = Frame_tp()
    tpBtnForm_f.setMinimumSize(100, 170)
    tpBtnForm_vbox = QVBoxLayout()
    tpBtnForm_vbox.setContentsMargins(0, 0, 0, 0)
    tpBtnForm_vbox.setSpacing(5)
    tpBtnForm_f.setLayout(tpBtnForm_vbox)

    tpBtn_hbox = QHBoxLayout()
    tpBtn_hbox.setContentsMargins(10, 50, 10, 43)
    tpBtn_hbox.setSpacing(25)
    tpBtn_hbox.setAlignment(Qt.AlignCenter)
    popBtnLabel_f = Frame_label("Population")
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
    # stacked_form_box - это функция

    tpBtn_hbox.addWidget(self.people_btn)
    tpBtn_hbox.addWidget(self.house_btn)

    self.stacked_form_count = {}

    def _setPopulation(self, region, index_stacked_w):
        """Doc.

        Добавление виджетов популяции. Кнопки для переключения.
        StackedLayout для отображения
        """
        # 2 формы для лейблов и едитов
        la_le_fbox = QFormLayout()    # 1 форма
        la_le_fbox.setSizeConstraint(QLayout.SetDefaultConstraint)
        la_le_fbox.setFieldGrowthPolicy(la_le_fbox.FieldsStayAtSizeHint)
        la_le_fbox.setRowWrapPolicy(la_le_fbox.DontWrapRows)
        la_le_fbox.setLabelAlignment(Qt. AlignRight | Qt. AlignTrailing |  # noqa
                                     Qt. AlignVCenter)
        la_le_fbox.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft |  # noqa
                                    Qt.AlignVCenter)
        la_le_fbox.setContentsMargins(50, 70, 50, 80)
        la_le_fbox.setVerticalSpacing(3)
        la_le_fbox.setObjectName("type_population_form")
        la_le_fbox2 = QFormLayout()   # 2 форма
        la_le_fbox2.setSizeConstraint(QLayout.SetDefaultConstraint)
        la_le_fbox2.setFieldGrowthPolicy(la_le_fbox2.FieldsStayAtSizeHint)
        la_le_fbox2.setRowWrapPolicy(la_le_fbox2.DontWrapRows)
        la_le_fbox2.setLabelAlignment(Qt. AlignRight | Qt. AlignTrailing |  # noqa
                                      Qt. AlignVCenter)
        la_le_fbox2.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft |  # noqa
                                     Qt.AlignVCenter)
        la_le_fbox2.setContentsMargins(50, 70, 50, 80)
        la_le_fbox2.setVerticalSpacing(3)
        la_le_fbox2.setObjectName("type_population_form2")
        # макет для форм
        form1_box = QFrame()
        form2_box = QFrame()
        forms_stackedW = QStackedWidget()
        forms_stackedW.addWidget(form1_box)
        forms_stackedW.addWidget(form2_box)
        form1_box.setLayout(la_le_fbox)
        form2_box.setLayout(la_le_fbox2)

        valid = QtCore.QRegExp("[0-9 .,]{15}")
        val = QtGui.QRegExpValidator(valid)

        people_list = []
        home_list = []

        for ki in range(2):
            self.stacked_form_count[index_stacked_w,
                                    f"type_{ki+1}"] = forms_stackedW

        if region == "Old_World":
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    people_list.append(people_icon_id)

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    home_list.append(home_icon_id)
            for i in people_list:      # заполнение лейблами 1 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox2.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)

        elif region == "New_World":
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    people_list.append(people_icon_id)

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    home_list.append(home_icon_id)
            for i in people_list:      # заполнение лейблами 1 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox2.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)

        elif region == "Cape_Trelawney":
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    people_list.append(people_icon_id)

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    home_list.append(home_icon_id)
            for i in people_list:      # заполнение лейблами 1 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox2.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)

        elif region == "The_Arctic":
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    people_list.append(people_icon_id)

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    home_list.append(home_icon_id)
            for i in people_list:      # заполнение лейблами 1 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox2.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)

        elif region == "Enbesa":
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    people_list.append(people_icon_id)

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    home_list.append(home_icon_id)
            for i in people_list:      # заполнение лейблами 1 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":" + i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit()
                self.edit_.setPlaceholderText("0")
                self.edit_.setAlignment(Qt.AlignCenter)
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_fbox2.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
        return forms_stackedW

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

    self.regionForm_stackedW = QStackedWidget()
    form_1 = _setPopulation(self, "Old_World", 0)
    form_2 = _setPopulation(self, "New_World", 1)
    form_3 = _setPopulation(self, "Cape_Trelawney", 2)
    form_4 = _setPopulation(self, "The_Arctic", 3)
    form_5 = _setPopulation(self, "Enbesa", 4)

    self.regionForm_stackedW.addWidget(form_1)
    self.regionForm_stackedW.addWidget(form_2)
    self.regionForm_stackedW.addWidget(form_3)
    self.regionForm_stackedW.addWidget(form_4)
    self.regionForm_stackedW.addWidget(form_5)

    # buttons_form.addWidget(self.regionForm_stackedW)
    # self.citySelectForm_stackedW = QStackedWidget()
    # self.citySelectForm_stackedW.addWidget(self.regionForm_stackedW)
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

    self.table_stackedW = QStackedWidget()
    self.table_stackedW.setContentsMargins(0, 0, 0, 0)

    self.table_stackedW.addWidget(table_1)
    self.table_stackedW.addWidget(table_2)
    self.table_stackedW.addWidget(table_3)
    self.table_stackedW.addWidget(table_4)
    self.table_stackedW.addWidget(table_5)

    self.searchTable_vbox.addWidget(self.table_stackedW)
    # self.city_select_stacked_w_t = QStackedWidget()
    # self.city_select_stacked_w_t.addWidget(self.table_stackedW)
    # self.searchTable_vbox.addWidget(self.city_select_stacked_w_t)

    tp_table_rc_hbox.addLayout(self.searchTable_vbox)
    #######################################################################
    city_label_frame = Frame_label("City")
    city_label_frame.setMinimumSize(170, 0)
    city_label_box = QVBoxLayout()
    city_label_box.setSpacing(0)
    city_label_box.setContentsMargins(7, 50, 7, 43)
    city_label_box.setAlignment(Qt.AlignCenter)
    city_label_frame.setLayout(city_label_box)

    regionCity_vbox.addWidget(city_label_frame)

    region1 = PushButton_R("Old_World")
    region1.setMinimumSize(32, 23)
    region1.clicked.connect(
        lambda: self.table_stackedW.setCurrentIndex(0))    # +++
    region1.clicked.connect(
        lambda: self.regionForm_stackedW.setCurrentIndex(0))
    region1.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(0))      # ++++
    region1.setObjectName("Old_World")
    region2 = PushButton_R("New_World")
    region2.setMinimumSize(32, 23)
    region2.clicked.connect(
        lambda: self.table_stackedW.setCurrentIndex(1))
    region2.clicked.connect(
        lambda: self.regionForm_stackedW.setCurrentIndex(1))
    region2.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(1))
    region3 = PushButton_R("Cape_Trelawney")
    region3.setMinimumSize(32, 23)
    region3.clicked.connect(
        lambda: self.table_stackedW.setCurrentIndex(2))
    region3.clicked.connect(
        lambda: self.regionForm_stackedW.setCurrentIndex(2))
    region3.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(2))
    region4 = PushButton_R("The_Arctic")
    region4.setMinimumSize(32, 23)
    region4.clicked.connect(
        lambda: self.table_stackedW.setCurrentIndex(3))
    region4.clicked.connect(
        lambda: self.regionForm_stackedW.setCurrentIndex(3))
    region4.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(3))
    region5 = PushButton_R("Enbesa")
    region5.setMinimumSize(32, 23)
    region5.clicked.connect(
        lambda: self.table_stackedW.setCurrentIndex(4))
    region5.clicked.connect(
        lambda: self.regionForm_stackedW.setCurrentIndex(4))
    region5.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(4))

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

        if region == "Old_World":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = PushButton_C('Main city \n Population:')
            city1.setMinimumSize(100, 40)
            city1.setObjectName("Main_city")
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
