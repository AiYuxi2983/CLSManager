import sys
from app.app import launch


def CLSManager():
    return launch()


if __name__ == "__main__":
    app, window = CLSManager()
    window.show()
    sys.exit(app.exec())
