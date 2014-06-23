import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.create_initial_layout()

    def create_initial_layout(self):
        #create widget
        self.text_box = QLineEdit()
        self.button = QPushButton("Submit")
        self.label = QLabel()
        # Create layout
        self.layout = QVBoxLayout()

        # add widget to layout
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        
        #set the centeral widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        #connection
        self.button.clicked.connect(self.display_text)

    def display_text(self):
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))

        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
