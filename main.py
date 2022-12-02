"""
Порядок создания имени переменной.

VariabelName_TypeWidget
где VariabelName - название виджета, TypeWidget - тип виджета

Если переменная создаётся несколько раз ей присвается индекс.
Он отражается в имени переменной:
VariabelName_TypeWidget_{VariabelIndex}
Если в виджет находятся больше 1 виджета допускается уточнение
в имени переменной:
VariabelNameRole_TypeWidget
VariabelNameRole_TypeWidget_{VariabelIndex}
"""
import sys
from PyQt5.QtCore import pyqtSlot  # noqa
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDesktopWidget,
                             QGridLayout, QHBoxLayout, QLayout,
                             QMainWindow, QVBoxLayout, QWidget, QStackedWidget)
import resources
from painter import *  # noqa
from resources.settings import Widget_settings  # noqa
from resources.tab1_consumpion.setpopulationfunc import _setPopulation


class MainWindow(QMainWindow):
    """Doc."""

    def __init__(self, parent=None):
        """Doc."""
        super().__init__()
        self.initUI()

    # def paintEvent(self, event):
    #     """PAINT EVENT."""
    #     QMainWindow.paintEvent(self, event)

    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.SmoothPixmapTransform)
    #     painter.setPen(QColor("red"))
    #     painter.drawRect(self.rect())  # noqa

        self.button2m_x = 0
        self.buttons_city = []
        self.countslfbtns0 = []
        self.countfrm0 = []
        self.count_city = {"Old_World": [1],
                           "New_World": [1]}

    def initUI(self):
        """Doc."""
        self.setMinimumSize(800, 600)
        self.setWindowTitle('Anno 1800 tools')
        self.setWindowIcon(QIcon(':Site-logo.webp'))
        # self.setWindowFlag(Qt.FramelessWindowHint)  # убирает границы окна
        # self.setAttribute(Qt.WA_TranslucentBackground)  # невидимый фон
        self.setAutoFillBackground(True)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        centralwidget = QWidget(self)
        self.setCentralWidget(centralwidget)
        main_gbox = QGridLayout(centralwidget)
        # main_box policy
        main_gbox.setContentsMargins(0, 0, 0, 0)
        main_gbox.setSpacing(0)

        topBar_hbox = QHBoxLayout()
        topBar_hbox.setSizeConstraint(QLayout.SetDefaultConstraint)
        topBar_hbox.setContentsMargins(0, 0, 0, 0)
        topBar_hbox.setSpacing(0)

        topBarBtn_f = Frame_tb()
        topBarBtn_hbox = QHBoxLayout()
        topBarBtn_hbox.setSpacing(0)
        topBarBtn_hbox.setContentsMargins(43, 0, 47, 20)
        topBarBtn_f.setLayout(topBarBtn_hbox)

        settingsInfo_f = Frame_si()
        settingsInfo_vbox = QVBoxLayout()
        settingsInfo_f.setLayout(settingsInfo_vbox)
        settingsInfo_vbox.setSizeConstraint(QLayout.SetDefaultConstraint)
        settingsInfo_vbox.setSpacing(5)
        settingsInfo_vbox.setContentsMargins(15, 12, 15, 25)

        topBar_hbox.addWidget(topBarBtn_f)
        topBar_hbox.addWidget(settingsInfo_f)
        topBar_hbox.setStretch(0, 10)

        main_gbox.addLayout(topBar_hbox, 0, 0, 1, 3)

        def create_top_bar():
            """Doc.

            Функция создания кнопок для TopBar.
            """
            self.consumption_btn = PushButton_tb("Consumption \n calculator")
            self.consumption_btn.clicked.connect(
                lambda: self.tab_stackedW.setCurrentIndex(0))
            production_chains_btn = PushButton_tb("Production\n chains")
            production_chains_btn.clicked.connect(
                lambda: self.tab_stackedW.setCurrentIndex(1))
            products_btn = PushButton_tb("Goods")
            products_btn.clicked.connect(
                lambda: self.tab_stackedW.setCurrentIndex(2))
            NateWorkshop_btn = PushButton_tb("Old Nate's\n Workshop")
            NateWorkshop_btn.clicked.connect(
                lambda: self.tab_stackedW.setCurrentIndex(3))
            NateWorkshop_btn.setObjectName("NateWorkshop_btn")
            MZG_btn = PushButton_tb("Museum,Zoo \nand Garden")
            MZG_btn.clicked.connect(
                lambda: self.tab_stackedW.setCurrentIndex(4))
            logistics_btn = PushButton_tb("Logistics\n chains")
            logistics_btn.clicked.connect(
                lambda: self.tab_stackedW.setCurrentIndex(5))
            cards_btn = PushButton_tb("Cards")
            cards_btn.clicked.connect(
                lambda: self.tab_stackedW.setCurrentIndex(6))
            settings_btn = PushButton_si("settings")
            settings_btn.setFixedSize(30, 30)
            settings_btn.clicked.connect(self.open_settings)

            info_btn = PushButton_si("info")
            info_btn.setFixedSize(30, 30)
            settingsInfo_vbox.addWidget(settings_btn)
            settingsInfo_vbox.addWidget(info_btn)

            tabs_list = (self.consumption_btn, production_chains_btn,
                         products_btn, NateWorkshop_btn,
                         MZG_btn, logistics_btn, cards_btn)
            for tabs in tabs_list:
                tabs.setMinimumSize(90, 40)
                topBarBtn_hbox.addWidget(tabs)

        create_top_bar()
        # Создание QStackedWidget для всех Tab

        def create_stucked_w():

            self.tab_stackedW = QStackedWidget()

            self.cons_tab = resources._consumptiontab(self)
            self.production_chains_tab = resources.production_chains(self)
            self.goods_tab = resources.goods(self)
            self.on_workshop = resources.old_Nate_workshop(self)
            self.mzg = resources.mzg(self)
            self.logistics_chains = resources.logistics_chains(self)
            self.cards_tab = resources.cards_tab(self)

            self.tab_stackedW.addWidget(self.cons_tab)
            self.tab_stackedW.addWidget(self.production_chains_tab)
            self.tab_stackedW.addWidget(self.goods_tab)
            self.tab_stackedW.addWidget(self.on_workshop)
            self.tab_stackedW.addWidget(self.mzg)
            self.tab_stackedW.addWidget(self.logistics_chains)
            self.tab_stackedW.addWidget(self.cards_tab)

            main_gbox.addWidget(self.tab_stackedW, 1, 0, 1, 3)

        create_stucked_w()

    def action1(self, text, col5, col2):
        """Doc.

        Расчет необходимого.
        type_population*base_consumption/(productivity/100)*base_output
        """
        _value = float(text)
        _value2 = float(col2)
        col5.setText(f'{round(_value/100*_value2,2)}')
        # добавить значения 3 колонки

    @pyqtSlot()
    def onTextChanged(self):
        """Doc."""
        try:
            popul = int(self.edit_.text())
        except ValueError:
            self.edit_.setText("0")
            popul = 0
        proizv = int(self.column4_le.text())
        col2 = int(self.column2_text.text())

        self.column5_la.setText(f"{round(popul / (proizv / 100 * col2),2)}")

    def column3_stacked_w(self, text):
        """Doc."""
        ind = self.regionTable_stackedW.currentIndex()
        _stacked_w_list = self.table_count
        _stacked_w = _stacked_w_list[ind]
        if text == "People":
            for r in _stacked_w.values():
                r.setCurrentIndex(0)
        elif text == "Home":
            for r in _stacked_w.values():
                r.setCurrentIndex(1)

    def forms_stackedW(self, text):
        """Doc."""
        ind = self.cityForm_stackedW.currentIndex()
        # ind2 = self.cityForm_stackedW0.currentIndex()
        # _city_stacked_w = self.countfrm0.get(ind2)
        # print(_city_stacked_w)
        _stacked_w = self.stacked_form_count.get((ind, text))

        ############################################## ОСТАНОВИЛСЯ ТУТ <<<---------------------
        if text == "type_1":
            _stacked_w.setCurrentIndex(0)

        elif text == "type_2":
            _stacked_w.setCurrentIndex(1)

    def city_select(self, reg, btn_name):
        """Choose city."""
        if reg == "Old_World":
            self.cityForm_stackedW0.setCurrentIndex(self.countslfbtns0.index(self.findChild(QAbstractButton, btn_name.objectName())) + 1)
            print(self.cityForm_stackedW0.currentIndex())

        # self.regionForm_stackedW.setCurrentIndex(self.count_city)

    @pyqtSlot()
    def add_city(self, pb: QPushButton, layout, reg: str):
        """Doc."""
        del_widget = QWidget()
        del_box = QHBoxLayout(del_widget)
        del_box.setContentsMargins(0, 0, 0, 0)
        del_box.setSpacing(0)

        self.button2 = PushButton_C("New city \n Population:", self)
        self.button2.setMinimumSize(100, 40)
        self.button -= layout.indexOf(self.button2)
        self.button2.setObjectName(f"citybtn_{self.button}")

        print("**************************\n" + "ИНДЕКС КНОПКИ НОВОГО ГОРОДА: " + str(self.button))

        self.btn = self.findChild(PushButton_C, f"citybtn_{self.button}")
        self.btn.clicked.connect(lambda x, btn_name=self.btn: self.city_select(reg, btn_name))
        print("Кнопка называется: " + self.btn.objectName())

        del_button = ToolButton_DC(self.button2)
        del_button.setMinimumSize(10, 10)
        self.buttons_city.append(del_button)

        del_box.addWidget(self.button2)
        del_button.move(138, 7)
        del_button.clicked.connect(
            lambda: self.del_city(del_widget, del_button))

        ind = self.city_stacked_w.currentIndex()
        _stack = self.city_count.get((ind))

        _stack.insertWidget(self.city_box_2.count() - 1, del_widget)
        _stack.insertWidget(self.button + 1, pb)

        if reg == "Old_World":
            self.count_city.update({"Old_World": f"{int(self.count_city.get('Old_World')[0])+1}"})
            new_cityform = _setPopulation(self, "Old_World", self.city_stacked_w.currentIndex(), (self.count_city.get("Old_World")[0]))
            self.countfrm0.insert(0, new_cityform)
            print("КОЛИЧЕСТВО ГОРОДОВ В РЕГИОНЕ: " + str(self.count_city.get("Old_World")[0]))
            self.cityForm_stackedW0.addWidget(new_cityform)
            self.countslfbtns0.insert(0, self.btn)
            print("В СЛОВАРЕ ЕСТЬ: " + str(self.countslfbtns0))
            print("КОЛИЧЕСТВО ВИДЖЕТОВ В СТАРОМ МИРЕ: " + str(self.cityForm_stackedW0.count()))

    @pyqtSlot()
    def del_city(self, city_widget, del_button):
        """Doc."""
        self.city_box_2.removeWidget(city_widget)
        city_widget.setParent(None)
        city_widget.deleteLater()
        self.buttons_city.remove(del_button)

    def open_settings(self):
        """Doc."""
        if not Widget_settings.isEnabled(self):
            pass
        else:
            ws = Widget_settings(self)
            ws.show()
            print("false")

    def closeMWindow(self):
        """Doc."""
        self.close
         # СОБЫТИЕ ЗАКРЫТИЯ
    # def closeEvent(self, event):
    #     """CLOSE EVENT."""
    #     reply = QMessageBox.question(
    #         self, "Message",
    #         "Are you sure you want to quit? Any unsaved work will be lost.",
    #         QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
    #         QMessageBox.Save)

#   def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         self.close()

        # if reply == QMessageBox.Close:
        #     event.accept()
        # else:
        #     event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("resources\\style.qss", "r") as h:
        app.setStyleSheet(h.read())
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
