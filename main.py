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
from PyQt5.QtWidgets import (QAction, QApplication, QDesktopWidget,
                             QGridLayout, QHBoxLayout, QLayout, QMainWindow,
                             QMenu, QVBoxLayout, QWidget, QStackedWidget)
import resources
from painter import *  # noqa
from resources.settings import Widget_settings    # noqa


class MainWindow(QMainWindow):
    """Doc."""

    def __init__(self, parent=None):
        """Doc."""
        super().__init__()
        self.initUI()

        self.button2m_x = 0
        self.buttons_city = []

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
        _value = int(text)
        _value2 = float(col2)
        col5.setText(f'{round(_value/100*_value2,2)}')
        # добавить значения 3 колонки

    def action2(self, text2, col5):
        """Doc."""
        pass

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

        # finally:
        #     self.column5_la.setText(popul/(proizv/100*col2))

    def column3_stacked_w(self, text):
        """Doc."""
        ind = self.table_stackedW.currentIndex()
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
        ind = self.regionForm_stackedW.currentIndex()
        _stacked_w = self.stacked_form_count.get((ind, text))

        if text == "type_1":
            _stacked_w.setCurrentIndex(0)

        elif text == "type_2":
            _stacked_w.setCurrentIndex(1)

    @pyqtSlot()
    def add_city(self, pb, layout):
        """Doc."""
        del_widget = QWidget()
        del_box = QHBoxLayout(del_widget)
        del_box.setContentsMargins(0, 0, 0, 0)
        del_box.setSpacing(0)

        self.button2 = PushButton_C("New city \n Population:")
        self.button2.setMinimumSize(100, 40)
        self.button -= layout.indexOf(self.button2)

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

        # self.city_select_stacked_w_t.addWidget(self.stacked_table_box)
        # self.citySelectForm_stackedW.addWidget(self.regionForm_stackedW)
        # self.button2.clicked.connect(
        #     lambda: self.city_select_stacked_w_t.setCurrentIndex(
        #         _stack.count() - 1))
        # self.button2.clicked.connect(
        #     lambda: self.citySelectForm_stackedW.setCurrentIndex(
        #         _stack.count() - 1))

    @pyqtSlot()
    def del_city(self, city_widget, del_button):
        """Doc."""
        self.city_box_2.removeWidget(city_widget)
        city_widget.setParent(None)
        city_widget.deleteLater()
        self.buttons_city.remove(del_button)

    def open_settings(self):
        """Doc."""
        self.settings_win = Widget_settings(self)
        self.settings_win.show()

    def _createActions(self):       # button click actions
        self.newfileAction = QAction('&New', self)
        self.newfileAction.setStatusTip('Create new file')

        self.openfileAction = QAction('&Open', self)
        self.openfileAction.setStatusTip(' Open the existing settings ')

        self.saveAction = QAction('&Save', self)
        self.saveAction.setStatusTip('Save current settings')
        self.saveasAction = QAction('&Save as', self)
        self.saveasAction.setStatusTip('Save current settings \
                                        in new file or another directory')
        self.exitAction = QAction(QIcon(':logout_.png'), 'Quit', self)
        self.exitAction.triggered.connect(self.close)
        self.exitAction.setShortcut('Ctrl+Q')             # create shortcut
        self.settings = QAction('& App Settings', self)
        self.settings.setStatusTip('All settings')
        self.gvsettings = QAction(QIcon(':conversion.svg'),
                                  'Game version', self)
        self.gvsettings.setStatusTip('Change your game version')
        self.wikiAction = QAction(QIcon(':info_.png'), '&Anno 1800 Wiki', self)
        self.wikiAction.setStatusTip('Databases of Anno 1800')
        self.adviceAction = QAction('&Useful advices', self)
        self.adviceAction.setStatusTip('Give some advice')
        self.aboutAction = QAction('&About', self)
        self.aboutAction.setStatusTip('About App')

    def _createMenuBar(self):     # create buttons in Menu Bar
        menuBar = self.menuBar()
        fileMenu = QMenu('&File', self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newfileAction)
        fileMenu.addAction(self.openfileAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.saveasAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        settings = menuBar.addMenu('&Settings')
        settings.addAction(self.settings)
        settings.addAction(self.gvsettings)
        helpMenu = menuBar.addMenu('&Help')
        adviceMenu = helpMenu.addMenu('Help content')
        adviceMenu.addAction(self.adviceAction)
        adviceMenu.addAction(self.wikiAction)
        helpMenu.addAction(self.aboutAction)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("resources\\style.qss", "r") as h:
        app.setStyleSheet(h.read())
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
