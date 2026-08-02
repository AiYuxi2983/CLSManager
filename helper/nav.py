from qfluentwidgets import NavigationItemPosition, FluentIcon as FIF


def init_navigation(self):
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
