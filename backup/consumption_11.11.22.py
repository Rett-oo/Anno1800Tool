"""Doc."""
import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QAction, QMainWindow, QMenu, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLayout, \
    QFormLayout, QFrame, QAbstractItemView,  QSizePolicy, \
    QTabWidget, QScrollArea,  QStackedWidget, QStackedLayout, QSpacerItem   # noqa
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
sys.path.append(os.path.abspath('resourсes/'))
import gui_icons  # noqa
from table import _createtable  # noqa

with open("resourсes\\consumption_data_p.json") as p:
    json_table = json.load(p)
with open("resourсes\\consumption_data_h.json") as h:
    json_table2 = json.load(h)


def _consumptiontab(self):

    # макет кнопок Home and People
    type_polutation_box = QHBoxLayout()
    type_polutation_box.setSizeConstraint(QLayout.SetDefaultConstraint)
    type_polutation_box.setContentsMargins(0, 0, 0, 0)
    type_polutation_box.setSpacing(0)
    type_polutation_box.setObjectName("Type Population Button")
    # макет для кнопок и формы
    buttons_form = QVBoxLayout()
    buttons_form.setSizeConstraint(QLayout.SetDefaultConstraint)
    buttons_form.setContentsMargins(-1, -1, 0, -1)
    buttons_form.setSpacing(5)
    buttons_form.setObjectName("Buttons and form type population")

    # поиск и кпопка поиска
    self.search_box = QHBoxLayout()
    self.search_table_box = QVBoxLayout()  # таблица и поиск
    self.search_table_box.setSizeConstraint(QLayout.SetMaximumSize)
    self.search_table_box.setContentsMargins(0, -1, -1, -1)
    self.search_table_box.setSpacing(5)
    self.search_table_box.setObjectName("Search and table")

    # макет кнопок выбора региона
    region_box = QHBoxLayout()
    region_box.setSizeConstraint(QLayout.SetDefaultConstraint)
    region_box.setContentsMargins(0, 0, 0, 0)
    region_box.setSpacing(0)
    region_box.setObjectName("Region")

    # макет выбора региона и добавление города
    region_city_box = QVBoxLayout()
    region_city_box.setSizeConstraint(QLayout.SetFixedSize)
    region_city_box.setAlignment(Qt.AlignTop)
    region_city_box.setContentsMargins(0, 0, 0, 0)
    region_city_box.setSpacing(5)
    region_city_box.setObjectName("Region and City")
    # макет с "Buttons and form type population" ,
    # "Search and table","Region and City"
    tp_table_rc = QHBoxLayout()
    tp_table_rc.setObjectName("TypePopulation, Table, AddCity")
    tp_table_rc_frame = QFrame()
    tp_table_rc_frame.setLayout(tp_table_rc)

    pop_label = QLabel("Population")
    sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,  QtWidgets.QSizePolicy.Fixed)
    pop_label.setSizePolicy(sizePolicy)
    pop_label.setAlignment(Qt.AlignCenter)
    pop_label.setObjectName("Type_of_population")
    buttons_form.addWidget(pop_label)

    self.people_btn = QPushButton(QIcon(':Population.webp'), '')
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalPolicy(0)
    sizePolicy.setHeightForWidth(
        self.people_btn.sizePolicy().hasHeightForWidth())
    self.people_btn.setSizePolicy(sizePolicy)
    self.people_btn.setMaximumSize(50, 25)
    self.people_btn.setObjectName("people_btn")
    self.people_btn.clicked.connect(
        lambda: self.column3_stacked_w("People"))
    self.people_btn.clicked.connect(
        lambda: self.stacked_form_box("type_1"))

    self.house_btn = QPushButton(QIcon(':3d_storage.png'), '')
    sizePolicy2 = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.Expanding,
        QtWidgets.QSizePolicy.Fixed)
    sizePolicy2.setHorizontalStretch(1)
    sizePolicy2.setVerticalPolicy(0)
    sizePolicy2.setHeightForWidth(
        self.house_btn.sizePolicy().hasHeightForWidth())
    self.house_btn.setSizePolicy(sizePolicy2)
    self.house_btn.setMaximumSize(50, 25)
    self.house_btn.setObjectName("house_btn")
    self.house_btn.clicked.connect(
        lambda: self.column3_stacked_w("Home"))
    self.house_btn.clicked.connect(
        lambda: self.stacked_form_box("type_2"))

    type_polutation_box.addWidget(self.people_btn)
    type_polutation_box.addWidget(self.house_btn)
    type_polutation_box.setStretch(1, 1)
    buttons_form.addLayout(type_polutation_box)



    self.stacked_form_count = {}

    def _setPopulation(self, region, index_stacked_w):
        """Doc.

        Добавление виджетов популяции. Кнопки для переключения.
        StackedLayout для отображения
        """
        # 2 формы для лейблов и едитов
        la_le_box = QFormLayout()    # 1 форма
        la_le_box.setSizeConstraint(QLayout.SetDefaultConstraint)
        la_le_box.setFieldGrowthPolicy(la_le_box.FieldsStayAtSizeHint)
        la_le_box.setRowWrapPolicy(la_le_box.DontWrapRows)
        la_le_box.setLabelAlignment(Qt. AlignRight | Qt. AlignTrailing
                                    | Qt. AlignVCenter)
        la_le_box.setFormAlignment(Qt.AlignLeading
                                   | Qt.AlignLeft | Qt.AlignVCenter)
        la_le_box.setContentsMargins(50, 70, 50, 80)
        la_le_box.setVerticalSpacing(3)
        la_le_box.setObjectName("type_population_form")
        la_le_box2 = QFormLayout()   # 2 форма
        la_le_box2.setSizeConstraint(QLayout.SetDefaultConstraint)
        la_le_box2.setFieldGrowthPolicy(la_le_box2.FieldsStayAtSizeHint)
        la_le_box2.setRowWrapPolicy(la_le_box2.DontWrapRows)
        la_le_box2.setLabelAlignment(Qt. AlignRight | Qt. AlignTrailing
                                     | Qt. AlignVCenter)
        la_le_box2.setFormAlignment(Qt.AlignLeading
                                    | Qt.AlignLeft | Qt.AlignVCenter)
        la_le_box2.setContentsMargins(50, 70, 50, 80)
        la_le_box2.setVerticalSpacing(3)
        la_le_box2.setObjectName("type_population_form2")
        # макет для форм
        form1_box = QFrame()
        form2_box = QFrame()
        stacked_form_box = QStackedWidget()
        stacked_form_box.addWidget(form1_box)
        stacked_form_box.addWidget(form2_box)
        form1_box.setLayout(la_le_box)
        form2_box.setLayout(la_le_box2)

        valid = QtCore.QRegExp("[0-9 .,]{15}")
        val = QtGui.QRegExpValidator(valid)

        people_list = []
        home_list = []

        for ki in range(2):
            self.stacked_form_count[index_stacked_w,
                                    f"type_{ki+1}"] = stacked_form_box

        if region == "Old_World":
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    people_list.append(people_icon_id)

            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    home_list.append(home_icon_id)
            for i in people_list:      # заполнение лейблами 1 формы
                pic_laybel = QLabel()
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box2.addRow(pic_laybel, self.edit_)
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
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box2.addRow(pic_laybel, self.edit_)
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
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box2.addRow(pic_laybel, self.edit_)
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
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box2.addRow(pic_laybel, self.edit_)
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
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
            for i in home_list:      # заполнение лейблами 2 формы
                pic_laybel = QLabel()
                pic = QPixmap(":"+i)
                pic_laybel.setPixmap(pic)
                pic_laybel.setMinimumSize(30, 30)
                pic_laybel.setMaximumSize(40, 40)
                pic_laybel.setScaledContents(True)
                self.edit_ = QLineEdit("0")
                self.edit_.setMinimumSize(30, 30)
                self.edit_.setMaximumSize(45, 30)
                self.edit_.setValidator(val)
                self.edit_.setMaxLength(4)
                la_le_box2.addRow(pic_laybel, self.edit_)
                self.edit_.textChanged.connect(self.onTextChanged)
        return stacked_form_box

    self.stacked_form_region_box = QStackedWidget()
    form_1 = _setPopulation(self, "Old_World", 0)
    form_2 = _setPopulation(self, "New_World", 1)
    form_3 = _setPopulation(self, "Cape_Trelawney", 2)
    form_4 = _setPopulation(self, "The_Arctic", 3)
    form_5 = _setPopulation(self, "Enbesa", 4)

    self.stacked_form_region_box.addWidget(form_1)
    self.stacked_form_region_box.addWidget(form_2)
    self.stacked_form_region_box.addWidget(form_3)
    self.stacked_form_region_box.addWidget(form_4)
    self.stacked_form_region_box.addWidget(form_5)

    buttons_form.addWidget(self.stacked_form_region_box)
    tp_table_rc.addLayout(buttons_form)

    req_label = QLabel("Requirements")
    req_label.setAlignment(Qt.AlignCenter)
    sizePolicy = QtWidgets.QSizePolicy(
                 QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalPolicy(0)
    sizePolicy.setHeightForWidth(
               req_label.sizePolicy().hasHeightForWidth())
    req_label.setSizePolicy(sizePolicy)
    req_label.setObjectName("Requirements")
    self.search_table_box.addWidget(req_label)

    searchbutton = QPushButton('Filters')
    searchbutton.setStyleSheet("background-color: #ced2bc; \
                  font: 12px;border-radius: 3px;font-style: Roboto")
    searchbutton.setMinimumSize(100, 20)
    searchedit = QLineEdit()
    searchedit.setMinimumSize(290, 20)
    self.search_box.addWidget(searchbutton)
    self.search_box.addWidget(searchedit)
    self.search_box.addSpacerItem(QSpacerItem(100, 0,
                                  QSizePolicy.Maximum, QSizePolicy.Fixed))
    self.search_table_box.addLayout(self.search_box)

    table_1 = _createtable(self, "Old_World")
    table_2 = _createtable(self, "New_World")
    table_3 = _createtable(self, "Cape_Trelawney")
    table_4 = _createtable(self, "The_Arctic")
    table_5 = _createtable(self, "Enbesa")

    self.stacked_table_box = QStackedWidget()

    self.stacked_table_box.addWidget(table_1)
    self.stacked_table_box.addWidget(table_2)
    self.stacked_table_box.addWidget(table_3)
    self.stacked_table_box.addWidget(table_4)
    self.stacked_table_box.addWidget(table_5)

    self.search_table_box.addWidget(self.stacked_table_box)
    tp_table_rc.addLayout(self.search_table_box)

    city_label = QLabel("City")
    city_label.setAlignment(Qt.AlignCenter)
    city_label.setObjectName("City")
    region_city_box.addWidget(city_label)

    region1 = QPushButton(QIcon(':oldworld_.webp'), '')
    region1.clicked.connect(
        lambda: self.stacked_table_box.setCurrentIndex(0))
    region1.clicked.connect(
        lambda: self.stacked_form_region_box.setCurrentIndex(0))
    region1.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(0))

    region2 = QPushButton(QIcon(':newworld_.webp'), '')
    region2.clicked.connect(
        lambda: self.stacked_table_box.setCurrentIndex(1))
    region2.clicked.connect(
        lambda: self.stacked_form_region_box.setCurrentIndex(1))
    region2.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(1))
    region3 = QPushButton(QIcon(':capetrelawney_.webp'), '')
    region3.clicked.connect(
        lambda: self.stacked_table_box.setCurrentIndex(2))
    region3.clicked.connect(
        lambda: self.stacked_form_region_box.setCurrentIndex(2))
    region3.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(2))
    region4 = QPushButton(QIcon(':arctic_.webp'), '')
    region4.clicked.connect(
        lambda: self.stacked_table_box.setCurrentIndex(3))
    region4.clicked.connect(
        lambda: self.stacked_form_region_box.setCurrentIndex(3))
    region4.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(3))
    region5 = QPushButton(QIcon(':enbesa_.webp'), '')
    region5.clicked.connect(
        lambda: self.stacked_table_box.setCurrentIndex(4))
    region5.clicked.connect(
        lambda: self.stacked_form_region_box.setCurrentIndex(4))
    region5.clicked.connect(
        lambda: self.city_stacked_w.setCurrentIndex(4))

    region_box.addWidget(region1)
    region_box.addWidget(region2)
    region_box.addWidget(region3)
    region_box.addWidget(region4)
    region_box.addWidget(region5)
    region_city_box.addLayout(region_box)

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
        self.city_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.city_scrollArea.setObjectName("Scroll_Area")

        self.city_widget = QWidget()
        self.city_widget.setObjectName("City_widget")
        self.city_widget.setStyleSheet("border-color: 3px solid black")

        self.city_box_2 = QVBoxLayout(self.city_widget)
        self.city_box_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.city_box_2.setContentsMargins(0, 0, 0, 0)
        self.city_box_2.setSpacing(0)
        self.city_box_2.setAlignment(Qt.AlignTop)

        self.city_select_stacked_w_f = QStackedWidget()
        self.city_select_stacked_w_t = QStackedWidget()

        self.city_count[index_stacked_wi] = self.city_box_2

        if region == "Old_World":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = QPushButton('Main city \n Population:')
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = QPushButton('+', self)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        elif region == "New_World":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = QPushButton('Main city \n Population:')
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = QPushButton('+', self)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        elif region == "Cape_Trelawney":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = QPushButton('Main city \n Population:')
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = QPushButton('+', self)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        elif region == "The_Arctic":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = QPushButton('Main city \n Population:')
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = QPushButton('+', self)
            self.city_box_2.addWidget(self.anothercity, alignment=Qt.AlignTop)
            self.anothercity.clicked.connect(
                lambda x, pb=self.anothercity,
                layout=self.city_box_2: self.add_city(pb, layout))

        elif region == "Enbesa":
            self.city_scrollArea.setWidget(self.city_widget)
            self.city_scrollArea.setWidgetResizable(True)
            self.city_box.addWidget(self.city_scrollArea)

            city1 = QPushButton('Main city \n Population:')
            self.city_box_2.addWidget(city1, alignment=Qt.AlignTop)

            self.button = 1
            self.anothercity = QPushButton('+', self)
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

    region_city_box.addWidget(self.city_stacked_w)
    region_city_box.setAlignment(Qt.AlignTop)

    tp_table_rc.addLayout(region_city_box)
    tp_table_rc.setStretch(1, 1)

    return tp_table_rc_frame
