from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from Controller.input_validation import validate_input
from View.cow_view import CowView
from View.goat_view import GoatView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cow Strike')
        self.setGeometry(100, 100, 500, 500)

        self.layout = QVBoxLayout()

        self.animal_id_input_label = QLabel("Enter Cow ID:")
        self.animal_id_input_label.setAlignment(Qt.AlignLeft)  # Align label text to the left
        self.animal_id_input_label.setStyleSheet(
            "font-size: 14px; margin-bottom: 5px;")

        self.animal_id_input = QLineEdit()
        # Set placeholder text in input field
        self.animal_id_input.setPlaceholderText("Cow ID")
        self.animal_id_input.setStyleSheet("font-size: 14px; padding: 5px;")

        # submit button
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #5cb85c;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #4cae4c;
            }
        """)  # Button styling with hover effect
        self.submit_btn.clicked.connect(self.submit_btnClicked)

        self.layout.addWidget(self.animal_id_input_label)
        self.layout.addWidget(self.animal_id_input)
        self.layout.addWidget(self.submit_btn)

        self.setLayout(self.layout)

    def submit_btnClicked(self):
        animal_id = self.animal_id_input.text()
        animal_type, udders, age = validate_input(animal_id)
        
        if animal_type == "cow":
            self.cow_view = CowView(animal_id, udders, age)
            self.cow_view.show()
        elif animal_type == "goat":
            self.goat_view = GoatView()
            self.goat_view.show()
        else:
            self.show_alert("No animal found with this ID.")

    def show_alert(self, message="This is an alert message!"):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('Alert')
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)
        msg_box.exec_()