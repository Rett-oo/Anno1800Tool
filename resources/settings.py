"""Doc."""

from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton


class Widget_settings(QWidget):
    """Doc."""

    def __init__(self, parent=None):
        """Doc."""
        super().__init__()

        self.initSubWindow

    def initSubWindow(self):
        """Doc."""
        self.setGeometry(300, 300, 300, 300)
        settings_layout = QGridLayout()
        self.setLayout(settings_layout)

        for i in range(5):
            pb = QPushButton("HELLO")
            settings_layout.addWidget(pb)
