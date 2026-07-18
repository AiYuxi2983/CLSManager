import sys
from main.main import init_application


def CLSManager():
    return init_application()


if __name__ == "__main__":
    app, window = CLSManager()
    window.show()
    sys.exit(app.exec())
