import sys
import traceback
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout
from qfluentwidgets import (
    PushButton,
    PrimaryPushButton,
    TextEdit,
    TitleLabel,
    BodyLabel,
    isDarkTheme,
)


class CrashDialog(QDialog):
    def __init__(self, error_msg, error_details, parent=None):
        super().__init__(parent)
        self.error_details = error_details
        self.setWindowTitle("程序崩溃")
        self.setFixedSize(550, 420)
        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        self.title_label = TitleLabel("CLSManager - 致命错误", self)

        self.info_label = BodyLabel(
            "程序出错，请尝试重启程序，如未解决，请联系开发者。", self
        )
        self.info_label.setWordWrap(True)

        self.text_edit = TextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlainText(error_details)
        self.text_edit.setFont(QFont("Consolas", 9))

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        btn_layout.addStretch(1)

        self.btn_copy = PushButton("复制错误信息", self)
        self.btn_copy.clicked.connect(self.copy_to_clipboard)

        self.btn_close = PrimaryPushButton("确定", self)
        self.btn_close.clicked.connect(self.accept)

        btn_layout.addWidget(self.btn_copy)
        btn_layout.addWidget(self.btn_close)

        layout.addWidget(self.title_label)
        layout.addWidget(self.info_label)
        layout.addWidget(self.text_edit)
        layout.addLayout(btn_layout)

        self.apply_theme_style()

    def apply_theme_style(self):
        is_dark = isDarkTheme()
        bg_color = "#202020" if is_dark else "#f3f3f3"
        border_color = "rgba(255, 255, 255, 0.08)" if is_dark else "rgba(0, 0, 0, 0.08)"

        self.setStyleSheet(f"""
            QDialog {{
                background-color: {bg_color};
                border: 1px solid {border_color};
                border-radius: 8px;
            }}
        """)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.error_details)
        self.btn_copy.setText("已复制到剪贴板！")


def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    error_details = "".join(
        traceback.format_exception(exc_type, exc_value, exc_traceback)
    )
    sys.stderr.write(error_details)

    app = QApplication.instance() or QApplication(sys.argv)
    app.setFont(QFont("Microsoft YaHei", 9))

    dialog = CrashDialog(str(exc_value), error_details)
    dialog.exec()
    sys.exit(1)


def setup_crash_report():
    sys.excepthook = global_exception_handler
