"""PAINT INTERPHACE."""
from PyQt5.QtWidgets import *  # noqa
from PyQt5.QtGui import *  # noqa
from PyQt5.QtCore import *  # noqa


class Frame_tb(QFrame):
    """PAINT TOP BAR BACKGROUND."""

    def __init__(self, parent=None):
        """INIT CLASS."""
        QFrame.__init__(self)

    def paintEvent(self, event):
        """PAINT EVENT."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), QPixmap(
            "resources/images/assets/bgr_popup_banner_0.png"))
        QFrame.paintEvent(self, event)


class PushButton_tb(QAbstractButton):
    """PAINT TOP BAR BUTTONS."""

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_tb, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_text60_purple_0.png")
        self.pixmap_hover = QPixmap(
            "resources/images/assets/btn_bg/btn_text60_disabled_0.png")
        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/btn_text60_hover_0.png")
        self.setCheckable(True)
        self.text = text

    def paintEvent(self, event):
        """PAINT EVENT."""
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_clicked

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), pix)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setPen(QColor("#fff4d7"))
        painter.setFont(QFont("Heuristica", 9))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class Frame_si(QFrame):
    """PAINT SETTINGS AND INFO BACKGROUND."""

    def __init__(self, parent=None):
        """INIT CLASS."""
        QFrame.__init__(self)

    def paintEvent(self, event):
        """PAINT EVENT."""
        QFrame.paintEvent(self, event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), QPixmap(
            "resources/images/assets/bgr_banner_small_diplomacy_frame_0.png"))
        painter.drawPixmap(self.rect(), QPixmap(
            "resources/images/assets/bgr_banner_small_diplomacy_0.png"))


class PushButton_si(QAbstractButton):
    """PAINT SETTINGS AND INFO BUTTONS."""

    def __init__(self, si, parent=None):
        """INIT CLASS."""
        super(QAbstractButton, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_transparent_small_normal_0.png")  # noqa
        self.pixmap_hover = QPixmap(
            "resources/images/assets/btn_bg/btn_transparent_small_hover_0.png")
        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/btn_transparent_small_clicked_0.png")  # noqa
        self.setCheckable(True)
        self.si = si
        if self.si == "settings":
            self.si = QPixmap("resources/images/icon/btn/i_btn_settings_2.png")
        else:
            self.si = QPixmap("resources/images/icon/btn/i_btn_explorer_2.png")

    def paintEvent(self, event):
        """PAINT EVENT."""
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_clicked
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(2, 2, 25, 25, QPixmap(
            "resources/images/assets/btn_bg/btn_bar72_purple_0.png"))
        painter.drawPixmap(self.rect(), pix)
        painter.drawPixmap(5, 5, 20, 20, self.si)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class Frame_label(QFrame):
    """PAINT BACKGROUND LABELS. 3 TEXT VALUES.

    IF VALUES: POPULATION - BG UNDER TYPE POPULATION BUTTONS AND LABEL
    ELIF VALUES: REQUIREMENTS - BG UNDER LABEL
    ELIF VALUES: CITY - BG UNDER REGION'S BUTTONS AND LABEL.
    """

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        QFrame.__init__(self)

        self.text = text

    def paintEvent(self, event):
        """PAINT EVENT."""
        QFrame.paintEvent(self, event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setPen(QColor("#fff4d7"))
        painter.setFont(QFont("Heuristica", 12))
        if self.text == "Requirements":
            painter.drawPixmap(self.rect(), QPixmap(
                "resources/images/assets/bg_bar_0.png"))
            painter.setRenderHint(QPainter.TextAntialiasing)
            painter.drawText(self.rect(), Qt.AlignCenter, self.text)
        elif self.text == "Population":
            painter.drawPixmap(self.rect(), QPixmap(
                "resources/images/assets/bgr_system_popup_0.png"))
            painter.setRenderHint(QPainter.TextAntialiasing)
            painter.drawText(9, 15, 170, 30, Qt.AlignHCenter, self.text)
        else:
            painter.drawPixmap(self.rect(), QPixmap(
                "resources/images/assets/bgr_system_popup_0.png"))
            painter.setRenderHint(QPainter.TextAntialiasing)
            painter.drawText(3, 15, 170, 30, Qt.AlignHCenter, self.text)


class Frame_tp(QFrame):
    """PAINT BACKGROUND TYPE POPULATION BUTTONS AND POPULATION FORM."""

    def __init__(self, parent=None):
        """INIT CLASS."""
        QFrame.__init__(self)

    def paintEvent(self, event):
        """PAINT EVENT."""
        QFrame.paintEvent(self, event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(QRect(QPoint(11, 50), QSize(170, 700)), QPixmap(
            "resources/images/assets/bgr_om_base_light_0.png"))


class PushButton_TP(QAbstractButton):
    """PAINT TYPE POPULATION BUTTONS. 2 VALUES: PEOPLE, BUILDINGS."""

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_TP, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_chat_transparent_normal_0.png")
        self.pixmap_hover = QPixmap(
            "resources/images/assets/btn_bg/btn_chat_transparent_selected_0.png")  # noqa
        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/bg_edit_field_selected_0.png")
        self.setCheckable(True)
        self.text = text

        if self.text == "Population":
            self.text = QPixmap(
                "resources/images/icon/btn/i_btn_resource_population_2.png")
        else:
            self.text = QPixmap(
                "resources/images/icon/btn/i_btn_buildings_2.png")

    def paintEvent(self, event):
        """PAINT EVENT."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        pix = self.pixmap_clicked
        painter.drawPixmap(3, 2, 44, 21, pix)
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_hover
            painter.drawPixmap(1, 1, 48, 25, pix)
        painter.drawPixmap(1, 1, 48, 25, pix)
        painter.drawPixmap(15, 3, 19, 20, self.text)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class PushButton_R(QAbstractButton):
    """REGION BUTTONS.

    5 VALUES: OLD_WORLD, NEW_WORLD, CAPE_TRELAWNEY, THE ARCTIC, ENBESA.
    """

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_R, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_chat_transparent_normal_0.png")
        self.pixmap_hover = QPixmap(
            "resources/images/assets/btn_bg/btn_chat_transparent_selected_0.png")  # noqa
        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/bg_edit_field_selected_0.png")
        self.setCheckable(True)
        self.text = text

        if self.text == "Old_World":
            self.text = QPixmap(
                "resources/images/icon/btn/i_btn_old_world_2.png")
        elif self.text == "New_World":
            self.text = QPixmap(
                "resources/images/icon/btn/i_btn_new_world_2.png")
        elif self.text == "Cape_Trelawney":
            self.text = QPixmap(
                "resources/images/icon/btn/i_btn_cape_trelawney_2.png")
        elif self.text == "The_Arctic":
            self.text = QPixmap(
                "resources/images/icon/btn/i_btn_the_arctic_2.png")
        elif self.text == "Enbesa":
            self.text = QPixmap(
                "resources/images/icon/btn/i_btn_enbesa_2.png")

    def paintEvent(self, event):
        """PAINT EVENT."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        pix = self.pixmap_clicked
        painter.drawPixmap(2, 1, 26, 20, pix)
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_hover
            painter.drawPixmap(self.rect(), pix)
        painter.drawPixmap(2, 1, 26, 20, pix)
        painter.drawPixmap(6, 4, 18, 14, self.text)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class PushButton_F(QAbstractButton):
    """FILTER BUTTON."""

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_F, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_text60_purple_0.png")
        self.pixmap_hover = QPixmap(
            "resources/images/assets/btn_bg/btn_text60_hover_0.png")
        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/btn_text60_selected_0.png")
        self.setCheckable(True)
        self.text = text

    def paintEvent(self, event):
        """PAINT EVENT."""
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_clicked

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), pix)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setPen(QColor("#fff4d7"))
        painter.setFont(QFont("Heuristica", 9))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class PushButton_C(QAbstractButton):
    """PAINT CITY BUTTONS."""

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_C, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_text40_purple_0.png")
        self.pixmap_hover = QPixmap(
            "resources/images/assets/btn_bg/btn_text40_gray_0.png")
        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/btn_text40_click_0.png")
        self.setCheckable(True)
        self.text = text

    def paintEvent(self, event):
        """PAINT EVENT."""
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_clicked

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), pix)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setPen(QColor("#fff4d7"))
        painter.setFont(QFont("Heuristica", 8))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class PushButton_AC(QAbstractButton):
    """PAINT ADD CITY BUTTON."""

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_AC, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_text40_purple_0.png")
        self.pixmap_hover = QPixmap(
            "resources/images/assets/btn_bg/btn_text40_gray_0.png")
        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/btn_text40_click_0.png")
        self.setCheckable(True)
        self.text = text

    def paintEvent(self, event):
        """PAINT EVENT."""
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_clicked

        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(self.rect(), pix)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setPen(QColor("#fff4d7"))
        painter.setFont(QFont("Heuristica-bold", 8))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class ToolButton_DC(QAbstractButton):
    """PAINT DELETE CITY TOOL BUTTON."""

    def __init__(self, parent=None):
        """INIT CLASS."""
        super(ToolButton_DC, self).__init__(parent)

        self.pixmap_clicked = QPixmap(
            "resources/images/assets/btn_bg/goods_rarity_0.png")  # noqa
        self.setCheckable(True)
        self.delpix = QPixmap("resources/images/icon/btn/i_btn_untick_2.png")

    def paintEvent(self, event):
        """PAINT EVENT."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        if self.isDown():
            pix = self.pixmap_clicked
            painter.drawPixmap(0, 1, 25, 25, pix)
        painter.drawPixmap(0, 0, 25, 25, self.delpix)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class PushButton_Settings(QAbstractButton):
    """PAINT SETTINGS BUTTONS."""

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_Settings, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/bg_recipebook_activestate_marker_0.png")  # noqa

        self.setCheckable(True)
        self.text = text

    def paintEvent(self, event):
        """PAINT EVENT."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        if self.text == "Exit":
            self.pixmap = QPixmap(
                "resources/images/assets/btn_bg/bg_recipebook_activestate_marker_3_0.png")  # noqa
        if self.underMouse():
            pix = self.pixmap
            painter.setOpacity(0.5)
            painter.drawPixmap(self.rect(), pix)
        elif self.isDown():
            pix = self.pixmap
            painter.setOpacity(0.75)
            painter.drawPixmap(self.rect(), pix)
        else:
            pix = self.pixmap
            painter.drawPixmap(self.rect(), pix)

        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setPen(QColor("#1a1918"))
        if self.text == "Exit":
            painter.setPen(QColor("#fff4d7"))
        painter.setFont(QFont("Heuristica", 12))
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()


class PushButton_HC(QAbstractButton):
    """PAINT HIDE AND CLOSE BUTTONS IN SETTINGS TAB."""

    def __init__(self, text, parent=None):
        """INIT CLASS."""
        super(PushButton_HC, self).__init__(parent)

        self.pixmap = QPixmap(
            "resources/images/assets/btn_bg/btn_icon60_orange_0.png")

        self.setCheckable(True)
        self.text = text

    def paintEvent(self, event):
        """PAINT EVENT."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        if self.text == "Hide":
            self.pixmap = QPixmap(
                "resources/images/assets/btn_bg/btn_icon60_gray_0.png")
        if self.underMouse():
            pix = self.pixmap
            painter.setOpacity(0.5)
            painter.drawPixmap(self.rect(), pix)
        elif self.isDown():
            pix = self.pixmap
            painter.setOpacity(0.9)
            painter.drawPixmap(self.rect(), pix)
        else:
            pix = self.pixmap
            painter.drawPixmap(self.rect(), pix)

        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setPen(QColor("#fff4d7"))
        painter.setFont(QFont("Heuristica", 12))
        if self.text == "Exit":
            painter.drawText(self.rect(), Qt.AlignCenter, "X")
        else:
            painter.drawText(self.rect(), Qt.AlignCenter, "_")

    def enterEvent(self, event):
        """MOUSE ON BUTTON EVENT."""
        self.update()

    def leaveEvent(self, event):
        """MOUSE LEAVE BUTTON EVENT."""
        self.update()
# text color: fff4d7 f4d700 ff817f87
