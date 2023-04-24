import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 300
        self.height = 600
        self.initUI()

    def initUI(self):
        # Create a label
        self.lbl = QLabel("PyQt5 Example App", self)

        # Add an image
        lbl_image = QLabel(self)
        pixmap = QPixmap("python.png").scaled(self.width, self.width)
        lbl_image.setPixmap(pixmap)

        # Create a button
        btn = QPushButton("Click me!", self)
        btn.clicked.connect(self.on_click)

        # Create a vertical layout and add the label and button
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_image)
        vbox.addWidget(self.lbl)
        vbox.addWidget(btn)

        # Set the layout for the window
        self.setLayout(vbox)

        # Set the window size
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowTitle("PyQt5 Example")
        self.show()

    def on_click(self):
        newX = int((self.lbl.x() + 10) % self.width)
        self.lbl.move(newX, self.lbl.y())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
