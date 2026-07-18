from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import TitleLabel  # 👈 導入 QFluentWidgets 原生大標題組件


class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("HomePage")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 使用 Qt 原生佈局內邊距代替 QSS 的 padding: 32px
        # 原生方法直接參與佈局引擎計算，100% 穩定，位置絕對不移動
        layout.setContentsMargins(32, 32, 32, 32)

        # TitleLabel 字型本身就是粗體/大字，且會隨主題自動適應黑/白色！
        title = TitleLabel("主页", self)
        layout.addWidget(title)
