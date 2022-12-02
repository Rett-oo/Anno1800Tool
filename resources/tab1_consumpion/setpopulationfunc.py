"""Doc."""
import json
from PyQt5.QtWidgets import QFormLayout, QFrame, QStackedWidget, QLabel, \
    QLineEdit
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt
from resources import gui_icons  # noqa


with open("resources\\tab1_consumpion\\consumption_data_p.json") as p:
    json_table = json.load(p)
with open("resources\\tab1_consumpion\\consumption_data_h.json") as h:
    json_table2 = json.load(h)


def _setPopulation(self, region, R_index_stacked_w, C_index_stacked_w) -> QStackedWidget:
    """Doc.

    Добавление виджетов популяции. Кнопки для переключения.
    StackedLayout для отображения
    """
    # 2 формы для лейблов и едитов
    la_le_fbox = QFormLayout()    # 1 форма
    la_le_fbox.setFieldGrowthPolicy(la_le_fbox.FieldsStayAtSizeHint)
    la_le_fbox.setLabelAlignment(Qt. AlignRight | Qt. AlignTrailing |  # noqa
                                 Qt. AlignVCenter)
    la_le_fbox.setFormAlignment(Qt.AlignLeading | Qt.AlignLeft |  # noqa
                                Qt.AlignVCenter)
    la_le_fbox.setContentsMargins(50, 70, 50, 80)
    la_le_fbox.setVerticalSpacing(3)
    la_le_fbox.setObjectName("type_population_form")

    la_le_fbox2 = QFormLayout()   # 2 форма
    la_le_fbox2.setFieldGrowthPolicy(la_le_fbox2.FieldsStayAtSizeHint)
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

    valid = QRegExp("[0-9 .,]{15}")
    val = QRegExpValidator(valid)

    people_list = []
    home_list = []

    for ki in range(2):
        self.stacked_form_count[R_index_stacked_w,
                                f"type_{ki+1}"] = forms_stackedW

    if region == "Old_World":
        for people in json_table[region][-1].values():
            for people_icon_id in people:
                people_list.append(people_icon_id)

        for homes in json_table2[region][-1].values():
            for home_icon_id in homes:
                home_list.append(home_icon_id)

        for i in people_list:      # заполнение лейблами 1 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox.addRow(tp_labpix, self.edit_)

            self.edit_.textChanged.connect(self.onTextChanged)

        for i in home_list:      # заполнение лейблами 2 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox2.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

    elif region == "New_World":

        for people in json_table[region][-1].values():
            for people_icon_id in people:
                people_list.append(people_icon_id)

        for homes in json_table2[region][-1].values():
            for home_icon_id in homes:
                home_list.append(home_icon_id)

        for i in people_list:      # заполнение лейблами 1 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)
        for i in home_list:      # заполнение лейблами 2 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox2.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

    elif region == "Cape_Trelawney":

        for people in json_table[region][-1].values():
            for people_icon_id in people:
                people_list.append(people_icon_id)

        for homes in json_table2[region][-1].values():
            for home_icon_id in homes:
                home_list.append(home_icon_id)

        for i in people_list:      # заполнение лейблами 1 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)
            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

        for i in home_list:      # заполнение лейблами 2 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)
            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox2.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

    elif region == "The_Arctic":

        for people in json_table[region][-1].values():
            for people_icon_id in people:
                people_list.append(people_icon_id)

        for homes in json_table2[region][-1].values():
            for home_icon_id in homes:
                home_list.append(home_icon_id)

        for i in people_list:      # заполнение лейблами 1 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

        for i in home_list:      # заполнение лейблами 2 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox2.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

    elif region == "Enbesa":
        for people in json_table[region][-1].values():
            for people_icon_id in people:
                people_list.append(people_icon_id)

        for homes in json_table2[region][-1].values():
            for home_icon_id in homes:
                home_list.append(home_icon_id)

        for i in people_list:      # заполнение лейблами 1 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

        for i in home_list:      # заполнение лейблами 2 формы
            tp_labpix = QLabel()
            pic = QPixmap(":" + i)
            tp_labpix.setPixmap(pic)
            tp_labpix.setMinimumSize(30, 30)
            tp_labpix.setMaximumSize(40, 40)
            tp_labpix.setScaledContents(True)

            self.edit_ = QLineEdit()
            self.edit_.setPlaceholderText("0")
            self.edit_.setAlignment(Qt.AlignCenter)
            self.edit_.setMinimumSize(30, 30)
            self.edit_.setMaximumSize(45, 30)
            self.edit_.setValidator(val)
            self.edit_.setMaxLength(4)
            la_le_fbox2.addRow(tp_labpix, self.edit_)
            self.edit_.textChanged.connect(self.onTextChanged)

    return forms_stackedW