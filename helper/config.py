from qfluentwidgets import isDarkTheme


# get current theme color
def get_theme():
    if isDarkTheme():
        return "white"
    else:
        return "black"
