from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class GoatView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Goat Status')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.goat_label = QLabel("Goat detected. Sending it back to the mountains...")
        self.goat_label.setStyleSheet("font-size: 14px;")

        self.remove_goat_btn = QPushButton("Remove Goat")
        self.remove_goat_btn.setStyleSheet("""
            QPushButton {
                background-color: #d9534f;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c9302c;
            }
        """)
        self.remove_goat_btn.clicked.connect(self.remove_goat)

        self.layout.addWidget(self.goat_label)
        self.layout.addWidget(self.remove_goat_btn)

        self.setLayout(self.layout)

    def remove_goat(self):
        self.close()
