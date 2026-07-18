from qfluentwidgets import isDarkTheme


def get_theme():
    if isDarkTheme():
        return "white"
    else:
        return "black"
