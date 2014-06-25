import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
            super().__init__()
            self.setWindowTitle("Hello World")
            self.stacked_layout = QStackedLayout()
            self.create_initial_layout()
            self.create_second_layout()
            self.widget = QWidget()
            self.widget.setLayout(self.stacked_layout)
            self.setCentralWidget(self.widget)
            

    def create_initial_layout(self):
            #create widget
            self.text_box = QLineEdit()
            self.submit_button = QPushButton("Submit")
            # Create layout
            self.layout = QVBoxLayout()
            # add widget to layout
            self.layout.addWidget(self.text_box)
            self.layout.addWidget(self.submit_button)
            self.initial_widget = QWidget()
            self.initial_widget.setLayout(self.layout)
            self.stacked_layout.addWidget(self.initial_widget)
            self.submit_button.clicked.connect(self.switch_layout)
            self.submit_button.clicked.connect(self.display_text)
            

    def create_second_layout(self):
            #create widget
            self.second_label = QLabel()
            self.back_button = QPushButton("Back")
            # Create layout
            self.second_layout = QVBoxLayout()
            # add widget to layout
            self.second_layout.addWidget(self.back_button)
            self.second_layout.addWidget(self.second_label)
            self.second_widget = QWidget()
            self.second_widget.setLayout(self.second_layout)
            self.stacked_layout.addWidget(self.second_widget)
            self.back_button.clicked.connect(self.switch_layout)

    def display_text(self):
            name = self.text_box.text()
            self.second_label.setText("Hello {0}!".format(name))

    def switch_layout(self):
        if self.stacked_layout.currentIndex() == 0:
            self.stacked_layout.setCurrentIndex(1)
        else:
            self.stacked_layout.setCurrentIndex(0)
            self.text_box.clear()



if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
