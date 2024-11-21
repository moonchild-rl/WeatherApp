import sys
import requests  # type: ignore
from PyQt5.QtWidgets import (  # type: ignore
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

# For alignment
from PyQt5.QtCore import Qt  # type: ignore


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
