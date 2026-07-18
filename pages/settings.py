# pages/settings.py
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from qfluentwidgets import (
    TitleLabel,
    BodyLabel,
    ComboBox,
    SimpleCardWidget,
    setTheme,
    Theme,
    isDarkTheme,
    InfoBar,
    InfoBarPosition,
)


class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("SettingsPage")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(36, 36, 36, 36)
        layout.setSpacing(24)

        title = TitleLabel("设置", self)
        layout.addWidget(title)

        self.card = SimpleCardWidget(self)
        card_layout = QHBoxLayout(self.card)
        card_layout.setContentsMargins(16, 12, 16, 12)

        self.theme_label = BodyLabel("应用主题", self.card)

        self.theme_combo = ComboBox(self.card)
        self.theme_combo.setPlaceholderText("选择应用主题")
        self.theme_combo.addItems(["浅色", "深色"])
        self.theme_combo.setFixedWidth(80)

        current_index = 1 if isDarkTheme() else 0
        self.theme_combo.setCurrentIndex(current_index)

        card_layout.addWidget(self.theme_label)
        card_layout.addStretch(1)
        card_layout.addWidget(self.theme_combo)

        layout.addWidget(self.card)

        self.theme_combo.currentIndexChanged.connect(self._on_theme_changed)

    def _on_theme_changed(self, index: int):
        if index == -1:
            return

        target_theme = Theme.LIGHT if index == 0 else Theme.DARK
        setTheme(target_theme)

        theme_text = "浅色模式" if index == 0 else "深色模式"
        InfoBar.success(
            title="设置成功",
            content=f"已成功切换至 {theme_text}",
            orient=Qt.Orientation.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self.window(),
        )
