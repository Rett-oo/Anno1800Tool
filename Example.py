import sys
from PyQt5.Qt import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button2m_x = 0
        self.property_buttons = []

        list_value_substate = ["2", "3", "5", "1"]
        list_value_substate_05 = ["-2", "-3", "-5", "-1"]
        list_value_substate_2 = ["10", "11"]
        list_value_substate_25 = ["-10", "-11"]
        list_value_substate_3 = ["100", "200"]
        list_value_substate_35 = ["-100", "-200"]

        self.centrawidget = QWidget(self)
        self.setCentralWidget(self.centrawidget)
        self.layout = QGridLayout(self.centrawidget)

        self.condition_1 = QPushButton(f"Condition 1")
        self.condition_1.clicked.connect(lambda: self.tc_stacked_w.setCurrentIndex(0))
        self.condition_1.clicked.connect(
            lambda: self.table_stacked_widget.setCurrentIndex(0))
        self.condition_1.clicked.connect(
            lambda: self.property_stacked_w.setCurrentIndex(0))

        self.condition_2 = QPushButton(f"Condition 2")
        self.condition_2.clicked.connect(lambda: self.tc_stacked_w.setCurrentIndex(1))
        self.condition_2.clicked.connect(
            lambda: self.table_stacked_widget.setCurrentIndex(1))
        self.condition_2.clicked.connect(
            lambda: self.property_stacked_w.setCurrentIndex(1))

        self.condition_3 = QPushButton(f"Condition 3")
        self.condition_3.clicked.connect(
            lambda: self.tc_stacked_w.setCurrentIndex(2))
        self.condition_3.clicked.connect(
            lambda: self.table_stacked_widget.setCurrentIndex(2))
        self.condition_3.clicked.connect(
            lambda: self.property_stacked_w.setCurrentIndex(2))

        self.layout.addWidget(self.condition_1, 0, 1)
        self.layout.addWidget(self.condition_2, 0, 3)
        self.layout.addWidget(self.condition_3, 0, 5)

        substate_1 = QPushButton("substate_1")
        substate_1.clicked.connect(lambda: self.tc("substate_1"))
        substate_1.clicked.connect(lambda: self.table_stacked_w("substate_1"))

        substate_2 = QPushButton("substate_2")
        substate_2.clicked.connect(lambda: self.tc("substate_2"))
        substate_2.clicked.connect(lambda: self.table_stacked_w("substate_2"))

        self.layout.addWidget(substate_1, 1, 0)
        self.layout.addWidget(substate_2, 1, 1)

# !!! +++
        self.substate_count = {}           # !!! +++ # <----------------------

# добавил  ---------------------------> vvvvvvvvvvvvvvv  <--------------------
        def type_condition(self, types, index_stacked_w):
            """Создание форм Substate"""
            substate_form = QFormLayout()
            substate_form_2 = QFormLayout()

            type_1 = QFrame()
            type_1.setStyleSheet("background-color: #1F1F41; color: #FFF;")   # +++

            type_2 = QFrame()
            type_2.setStyleSheet("background-color: #411F1F; color: #FFF;")   # +++

            type_1.setLayout(substate_form)
            type_2.setLayout(substate_form_2)
            tc = QStackedWidget()
            tc.addWidget(type_1)
            tc.addWidget(type_2)

# !!! ---            self.substate_count = {}  # останется только последний

###            for i in range(3):              # ??? (3) почему три
            print(f'\ndef type_condition(self, types):: {types}; {index_stacked_w}\n') #  self.tc_stacked_w
            for i in range(2):
#                self.substate_count[i, 0] = tc
                self.substate_count[index_stacked_w, f'substate_{i+1}'] = tc
# поменял ключ -------------------> ^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^        <----
# смотрите что получилось vvvvvvvvvvvvvvvvvvvvvvvvvv
            for k, v in self.substate_count.items():
                print(k, v)
# смотрите что получилось ^^^^^^^^^^^^^^^^^^^^^^^^^^

            if types == "Condition_1":
                for i in list_value_substate:
                    label = QLabel(i)
                    line_edit = QLineEdit("")
                    substate_form.addRow(label, line_edit)
                for i in list_value_substate_05:
                    label = QLabel(i)
                    line_edit = QLineEdit()
                    substate_form_2.addRow(label, line_edit)

            elif types == "Condition_2":
                for i in list_value_substate_2:
                    label = QLabel(i)
                    line_edit = QLineEdit()
                    substate_form.addRow(label, line_edit)
                for i in list_value_substate_25:
                    label = QLabel(i)
                    line_edit = QLineEdit()
                    substate_form_2.addRow(label, line_edit)

            elif types == "Condition_3":
                for i in list_value_substate_3:
                    label = QLabel(i)
                    line_edit = QLineEdit()
                    substate_form.addRow(label, line_edit)
                for i in list_value_substate_35:
                    label = QLabel(i)
                    line_edit = QLineEdit()
                    substate_form_2.addRow(label, line_edit)

            return tc

# добавил  -----------------------------------------> v <---------------------
        init_tc = type_condition(self, "Condition_1", 0)     # index для tc_stacked_w
        init_tc_2 = type_condition(self, "Condition_2", 1)
        init_tc_3 = type_condition(self, "Condition_3", 2)

        print(f'\ninit_tc =   {init_tc} \ninit_tc_2 = {init_tc_2} \ninit_tc_3 = {init_tc_3}') #

        self.tc_stacked_w = QStackedWidget()
        self.tc_stacked_w.addWidget(init_tc)
        self.tc_stacked_w.addWidget(init_tc_2)
        self.tc_stacked_w.addWidget(init_tc_3)

        self.layout.addWidget(self.tc_stacked_w, 2, 0, 5, 2)


        def table(self, types):
            if types == "Condition_1":
                table = QTableWidget(5,1)
                self.table_row_count = {}

                for row in range(table.rowCount()):
                    frame_1 = QFrame()
                    grid_1 = QGridLayout(frame_1)
                    frame_2 = QFrame()
                    grid_2 = QGridLayout(frame_2)

                    table_stacked_w = QStackedWidget()
                    table_stacked_w.addWidget(frame_1)
                    table_stacked_w.addWidget(frame_2)
                    table.setCellWidget(row,0, table_stacked_w)

                    self.table_row_count[row, 0] = table_stacked_w

                    grid_1.addWidget(QLabel(f"Condition_1 value {row}"))
                    grid_2.addWidget(QLabel(f"Condition_1 value -{row}"))
            elif types == "Condition_2":
                table = QTableWidget(3,1)
                self.table_row_count = {}

                for row in range(table.rowCount()):
                    frame_1 = QFrame()
                    grid_1 = QGridLayout(frame_1)
                    frame_2 = QFrame()
                    grid_2 = QGridLayout(frame_2)

                    table_stacked_w = QStackedWidget()
                    table_stacked_w.addWidget(frame_1)
                    table_stacked_w.addWidget(frame_2)
                    table.setCellWidget(row,0, table_stacked_w)

                    self.table_row_count[row, 0] = table_stacked_w

                    grid_1.addWidget(QLabel(f"Condition_2 value {row}"))
                    grid_2.addWidget(QLabel(f"Condition_2 value -{row}"))
            elif types == "Condition_3":
                table = QTableWidget(10,1)
                self.table_row_count = {}

                for row in range(table.rowCount()):
                    frame_1 = QFrame()
                    grid_1 = QGridLayout(frame_1)
                    frame_2 = QFrame()
                    grid_2 = QGridLayout(frame_2)

                    table_stacked_w = QStackedWidget()
                    table_stacked_w.addWidget(frame_1)
                    table_stacked_w.addWidget(frame_2)
                    table.setCellWidget(row,0, table_stacked_w)

                    self.table_row_count[row, 0] = table_stacked_w

                    grid_1.addWidget(QLabel(f"Condition_3 value {row}"))
                    grid_2.addWidget(QLabel(f"Condition_3 value -{row}"))

            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            return table

        self.table_stacked_widget = QStackedWidget()
        table_1 = table(self, "Condition_1")
        table_2 = table(self, "Condition_2")
        table_3 = table(self, "Condition_3")
        self.table_stacked_widget.addWidget(table_1)
        self.table_stacked_widget.addWidget(table_2)
        self.table_stacked_widget.addWidget(table_3)
        self.layout.addWidget(self.table_stacked_widget, 1, 2, 5, 3)

        def condition_property(self, types):
            """Doc."""
            # макет кнопок добавления города
            self.v1_box = QVBoxLayout()
            self.v1_box.setSizeConstraint(QLayout.SetDefaultConstraint)
            self.v1_box.setContentsMargins(0, 0, 0, 0)
            self.v1_box.setAlignment(Qt.AlignTop)
            self.scroll_area = QScrollArea(self)
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.property_widget = QWidget()
            self.v2_box_2 = QVBoxLayout(self.property_widget)
            self.v2_box_2.setSizeConstraint(QLayout.SetDefaultConstraint)
            self.v2_box_2.setContentsMargins(0, 0, 0, 0)
            self.v2_box_2.setAlignment(Qt.AlignTop)

            if types == "Condition_1":
                self.scroll_area.setWidget(self.property_widget)
                self.scroll_area.setWidgetResizable(True)
                self.v1_box.addWidget(self.scroll_area)

                main_property = QPushButton("Main Property_1")
                self.v2_box_2.addWidget(main_property, alignment=Qt.AlignTop)

                self.button = 1
                self.advanced_prop = QPushButton('+', self)
                self.v2_box_2.addWidget(self.advanced_prop, alignment=Qt.AlignTop)
                self.advanced_prop.clicked.connect(
                    lambda x, pb=self.advanced_prop,
                    layout=self.v2_box_2: self.add_property(pb, layout))

            elif types == "Condition_2":
                self.scroll_area.setWidget(self.property_widget)
                self.scroll_area.setWidgetResizable(True)
                self.v1_box.addWidget(self.scroll_area)

                main_property = QPushButton('Main Property_2')
                self.v2_box_2.addWidget(main_property, alignment=Qt.AlignTop)

                self.button = 1
                self.advanced_prop = QPushButton('+', self)
                self.v2_box_2.addWidget(self.advanced_prop, alignment=Qt.AlignTop)
                self.advanced_prop.clicked.connect(
                    lambda x, pb=self.advanced_prop,
                    layout=self.v2_box_2: self.add_property(pb, layout))

            elif types == "Condition_3":
                self.scroll_area.setWidget(self.property_widget)
                self.scroll_area.setWidgetResizable(True)
                self.v1_box.addWidget(self.scroll_area)

                main_property = QPushButton('Main Property_3')
                self.v2_box_2.addWidget(main_property, alignment=Qt.AlignTop)

                self.button = 1
                self.advanced_prop = QPushButton('+', self)
                self.v2_box_2.addWidget(self.advanced_prop, alignment=Qt.AlignTop)
                self.advanced_prop.clicked.connect(
                    lambda x, pb=self.advanced_prop,
                    layout=self.v2_box_2: self.add_property(pb, layout))
            return self.v1_box

        prop_1 = condition_property(self,"Condition_1")
        prop_2 = condition_property(self,"Condition_2")
        prop_3 = condition_property(self,"Condition_3")

        prop_frame1 = QFrame()
        prop_frame1.setLayout(prop_1)
        prop_frame2 = QFrame()
        prop_frame2.setLayout(prop_2)
        prop_frame3 = QFrame()
        prop_frame3.setLayout(prop_3)

        self.property_stacked_w = QStackedWidget()
        self.property_stacked_w.setMinimumSize(100,300)

        self.property_stacked_w.addWidget(prop_frame1)
        self.property_stacked_w.addWidget(prop_frame2)
        self.property_stacked_w.addWidget(prop_frame3)

        self.layout.addWidget(self.property_stacked_w,1,5,5,2)

# !!! vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def tc(self, text):
        #print(f'\ndef tc(self, text): {self.tc_stacked_w.currentIndex()}; {text}; \n') #  self.tc_stacked_w

        ind = self.tc_stacked_w.currentIndex()
        _stacked_w = self.substate_count.get((ind, text))
        print(f'\nind = {ind}; text = {text}; ----> {_stacked_w} <----\n')

        if text == "substate_1":
            _stacked_w.setCurrentIndex(0)
#            for i in self.substate_count.values():
#                i.setCurrentIndex(0)
        elif text == "substate_2":
            _stacked_w.setCurrentIndex(1)
#            for i in self.substate_count.values():
#                i.setCurrentIndex(1)
# !!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def table_stacked_w(self, text):
        if text == "substate_1":
            for r in self.table_row_count.values():
                r.setCurrentIndex(0)
        elif text == "substate_2":
            for r in self.table_row_count.values():
                r.setCurrentIndex(1)

    @pyqtSlot()
    def add_property(self, pb, layout):
        """Doc."""
        del_widget = QWidget()
        del_box = QHBoxLayout(del_widget)
        del_box.setContentsMargins(0, 0, 0, 0)
        del_box.setSpacing(0)


        self.button2 = QPushButton("New property:")
        self.button2.setMinimumSize(100,35)
        self.button -= layout.indexOf(self.button2)

        del_button = QToolButton(self.button2)
        del_button.setText("x")
        self.property_buttons.append(del_button)

        del_box.addWidget(self.button2)
        del_button.move(80, 5)
        del_button.clicked.connect(
                   lambda: self.del_property(del_widget, del_button))

        self.v2_box_2.insertWidget(self.v2_box_2.count()-1, del_widget)
        self.v2_box_2.insertWidget(self.button+1, pb)

    @pyqtSlot()
    def del_property(self, property_widget, del_button):
        """Doc."""
        self.v2_box_2.removeWidget(property_widget)
        property_widget.setParent(None)
        property_widget.deleteLater()
        self.property_buttons.remove(del_button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())