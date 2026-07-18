import sys
from PyQt6.QtCore import qInstallMessageHandler, QtMsgType
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication
from qfluentwidgets import (
    FluentWindow,
    NavigationItemPosition,
    FluentIcon as FIF,
    setTheme,
    Theme,
)
from pages import home, settings
from core import get_theme
from core.crashReporter import setup_crash_report


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.setWindowTitle("CLSManager")

        self._home_page = home.HomePage(self)
        self._settings_page = settings.SettingsPage(self)

        self._init_navigation()

    def _init_navigation(self):
        self.addSubInterface(
            interface=self._home_page,
            icon=FIF.HOME,
            text="主页",
            position=NavigationItemPosition.TOP,
        )

        self.addSubInterface(
            interface=self._settings_page,
            icon=FIF.SETTING,
            text="设置",
            position=NavigationItemPosition.BOTTOM,
        )

    setTheme(Theme.DARK)
    get_theme_color = get_theme


def qt_message_handler(msg_type, context, msg):
    if "QFont::setPointSize" in msg:
        return
    if msg_type in (
        QtMsgType.QtWarningMsg,
        QtMsgType.QtCriticalMsg,
        QtMsgType.QtFatalMsg,
    ):
        sys.stderr.write(f"Qt Warning: {msg}\n")
    else:
        sys.stdout.write(f"Qt Info: {msg}\n")


def init_application():
    setup_crash_report()
    qInstallMessageHandler(qt_message_handler)

    app = QApplication.instance() or QApplication(sys.argv)
    app.setFont(QFont("Microsoft YaHei", 9))

    window = MainWindow()
    return app, window
