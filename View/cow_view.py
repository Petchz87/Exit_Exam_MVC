from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from Controller.calculate_milk import cal_milk

class CowView(QWidget):
    total_milk = 0  # keep track of total milk production

    def __init__(self, animal_id, udders, age):
        super().__init__()
        self.setWindowTitle('Cow Status')
        self.setGeometry(100, 100, 400, 250)

        # Store variables
        self.animal_id = animal_id
        self.udders = udders
        self.age = age

        self.layout = QVBoxLayout()

        self.result_label = QLabel("")
        self.result_label.setStyleSheet("font-size: 14px;")

        self.milk_result_label = QLabel("")
        self.milk_result_label.setStyleSheet("font-size: 14px;")

        self.milk_button = QPushButton("Milk Cow")
        self.milk_button.setStyleSheet("font-size: 14px;")
        self.milk_button.clicked.connect(self.milk_cow)
        self.milk_button.setEnabled(False)

        self.return_button = QPushButton("Return to Input")
        self.return_button.setStyleSheet("font-size: 14px;")
        self.return_button.clicked.connect(self.return_to_input)

        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.milk_result_label)
        self.layout.addWidget(self.milk_button)
        self.layout.addWidget(self.return_button)
        self.setLayout(self.layout)

        # Display results after initializing widgets
        self.display_result(animal_id, udders, age)

    def display_result(self, animal_id, udders, age):
        if udders == 4:
            self.milk_result_label.setText("This cow has 4 udders. Ready for milking!")
            self.milk_button.setEnabled(True)
        else:
            self.milk_result_label.setText("This cow does not have 4 udders. Milking may not be possible.")
            self.milk_button.setEnabled(False)
        milk = cal_milk(animal_id, udders, age)
        CowView.total_milk += milk
        self.display_milk_result(animal_id, milk)

    def milk_cow(self):
        QMessageBox.information(self, "Milking", "Milking the cow... Done!")
        # Use to recalculate and update
        self.display_result(self.animal_id, self.udders, self.age)

    def display_milk_result(self, animal_id, milk):
        message = (f"This cow with ID {animal_id} can produce {milk:.2f} liters.\n"
                   f"Total milk production is: {CowView.total_milk:.2f} liters.")
        self.milk_result_label.setText(message)

    def return_to_input(self):
        # Close current window and return to input screen (assuming you have a main window or input screen to return to)
        self.close()
