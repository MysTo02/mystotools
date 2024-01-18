import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #main window
        self.setWindowTitle("MysTo Tools")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #152238; color: white;")
        self.setWindowIcon(QIcon('images/talk.png'))

        #Create central widget and layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        logo_and_buttons_layout = QHBoxLayout()
        logo_layout = QVBoxLayout()

        logo_label = QLabel(self)
        logo_pixmap = QPixmap("images/talk.png")  
        logo_pixmap = logo_pixmap.scaledToWidth(100)  
        logo_pixmap = logo_pixmap.scaledToHeight(100) 
        logo_label.setPixmap(logo_pixmap)
        logo_layout.addWidget(logo_label)

        text_label = QLabel("MysTo Tools", self)
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setStyleSheet("color: white; font-family: Arial; font-size: 20px; font-weight: bold; font-style: italic;")
        logo_layout.addWidget(text_label)

        logo_and_buttons_layout.addLayout(logo_layout)
        logo_and_buttons_layout.addSpacing(50)
        buttons_layout = QVBoxLayout()

        #Set central widget
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
