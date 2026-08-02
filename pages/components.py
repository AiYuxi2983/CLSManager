from PyQt6.QtGui import QFont
from qfluentwidgets import BodyLabel, qconfig
from helper import config


class StyledTitle(BodyLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)

        # 1. 使用原生 QFont 设置字体，彻底避开 QSS 导致的 Point Size <= 0 错误
        title_font = QFont("Microsoft YaHei", 22)  # Windows 推荐雅黑，Mac 会自动映射
        title_font.setBold(True)
        self.setFont(title_font)

        self.update_style()
        qconfig.themeChanged.connect(self.update_style)

    def update_style(self):
        color = config.get_theme()

        self.setStyleSheet(f"""
            color: {color};
            padding: 32px;
        """)
