"""COMPLETE FORM STACKED WIDGET."""
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


def _setPopulation(self, region,
                   R_index_stacked_w,
                   C_index_stacked_w) -> QStackedWidget:
    """Doc.

    Добавление виджетов популяции. Кнопки для переключения.
    StackedLayout для отображения
    """
    valid = QRegExp("[0-9 .,]{15}")
    val = QRegExpValidator(valid)
    people_list = []
    home_list = []

    forms_stackedW = QStackedWidget()
    for count_stackW in range(2):
        self.stacked_form_count[R_index_stacked_w,
                                f"type_{count_stackW+1}"] = forms_stackedW

    def createform_area(tp_list, objname: str) -> QFrame:
        frame = QFrame()
        fbox = QFormLayout()
        frame.setLayout(fbox)
        fbox.setFieldGrowthPolicy(fbox.FieldsStayAtSizeHint)
        fbox.setLabelAlignment(Qt. AlignCenter | Qt. AlignTrailing |  # noqa
                               Qt. AlignVCenter)
        fbox.setFormAlignment(Qt.AlignLeading | Qt.AlignCenter |  # noqa
                              Qt.AlignVCenter)
        fbox.setContentsMargins(50, 70, 50, 80)
        fbox.setVerticalSpacing(3)
        fbox.setObjectName(objname)

        if tp_list == people_list:
            for people in json_table[region][-1].values():
                for people_icon_id in people:
                    people_list.append(people_icon_id)
        else:
            for homes in json_table2[region][-1].values():
                for home_icon_id in homes:
                    home_list.append(home_icon_id)

        def formcomplete(parent_layout, tp_list: list) -> QFrame:
            for i in tp_list:
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
                parent_layout.addRow(tp_labpix, self.edit_)

                self.edit_.textChanged.connect(self.onTextChanged)

        formcomplete(fbox, tp_list)
        return frame

    forms_stackedW.addWidget(createform_area(people_list,
                                             "type_population_form"))
    forms_stackedW.addWidget(createform_area(home_list,
                                             "type_population_form2"))

    return forms_stackedW
