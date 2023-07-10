import sys
import tkinter as tk
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tkcalendar import DateEntry
from PIL import Image


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DocPuller")
        self.setGeometry(100, 100, 700, 550)
        self.setFixedSize(700, 550)

        # Resize the background image
        background_image = Image.open("images/background.jpeg")
        resized_image = background_image.resize((800, 600))
        self.background_photo = QtGui.QPixmap.fromImage(
            QtGui.QImage(
                resized_image.tobytes(), resized_image.size[0], resized_image.size[1], QtGui.QImage.Format_RGB888
            )
        )

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Headline
        headline = QtWidgets.QLabel("DocPuller", self)
        headline.setAlignment(QtCore.Qt.AlignCenter)
        headline.setStyleSheet("background-color: transparent;")
        headline.setFont(QtGui.QFont("Arial", 24, QtGui.QFont.Bold))
        self.layout.addWidget(headline)
        self.layout.addSpacing(10)

        # Section 0: Free Text Directory Entry
        section0 = QtWidgets.QFrame(self)
        section0_layout = QtWidgets.QVBoxLayout(section0)
        section0.setLayout(section0_layout)
        section0.setFixedWidth(400)
        self.layout.addWidget(section0)
        self.layout.addSpacing(10)

        directory_label = QtWidgets.QLabel("Directories", section0)
        directory_label.setAlignment(QtCore.Qt.AlignCenter)
        directory_label.setStyleSheet("background-color: transparent;")
        section0_layout.addWidget(directory_label)

        self.directory_entry = QtWidgets.QPlainTextEdit(section0)
        self.directory_entry.setFixedHeight(100)
        section0_layout.addWidget(self.directory_entry)

        self.selected_directory_label = QtWidgets.QLabel("Selected:", section0)
        self.selected_directory_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_directory_label.setFont(QtGui.QFont("Arial", 12))
        self.selected_directory_label.setStyleSheet("background-color: transparent;")
        section0_layout.addWidget(self.selected_directory_label)

        # Section 1: Date Selection
        section1 = QtWidgets.QFrame(self)
        section1_layout = QtWidgets.QHBoxLayout(section1)
        section1.setLayout(section1_layout)
        section1.setFixedWidth(400)
        self.layout.addWidget(section1)
        self.layout.addSpacing(10)

        from_date_label = QtWidgets.QLabel("From:", section1)
        from_date_label.setAlignment(QtCore.Qt.AlignCenter)
        from_date_label.setStyleSheet("background-color: transparent;")
        section1_layout.addWidget(from_date_label)

        self.from_date_entry = self.create_date_entry(section1)
        section1_layout.addWidget(self.from_date_entry)

        to_date_label = QtWidgets.QLabel("To:", section1)
        to_date_label.setAlignment(QtCore.Qt.AlignCenter)
        to_date_label.setStyleSheet("background-color: transparent;")
        section1_layout.addWidget(to_date_label)

        self.to_date_entry = self.create_date_entry(section1)
        section1_layout.addWidget(self.to_date_entry)

        # Section 2: Radio Buttons
        section2 = QtWidgets.QFrame(self)
        section2_layout = QtWidgets.QVBoxLayout(section2)
        section2.setLayout(section2_layout)
        section2.setFixedWidth(400)
        self.layout.addWidget(section2)
        self.layout.addSpacing(10)

        radio_label = QtWidgets.QLabel("File Types", section2)
        radio_label.setAlignment(QtCore.Qt.AlignCenter)
        radio_label.setStyleSheet("background-color: transparent;")
        section2_layout.addWidget(radio_label)

        self.radio_var = QtWidgets.QButtonGroup()

        radio1 = QtWidgets.QRadioButton("Document Type", section2)
        self.radio_var.addButton(radio1)
        section2_layout.addWidget(radio1)

        radio2 = QtWidgets.QRadioButton("Every File Type", section2)
        self.radio_var.addButton(radio2)
        section2_layout.addWidget(radio2)

        # Section 3: Free Text Entry
        section3 = QtWidgets.QFrame(self)
        section3_layout = QtWidgets.QVBoxLayout(section3)
        section3.setLayout(section3_layout)
        section3.setFixedWidth(400)
        self.layout.addWidget(section3)
        self.layout.addSpacing(10)

        keyword_label = QtWidgets.QLabel("Keywords", section3)
        keyword_label.setAlignment(QtCore.Qt.AlignCenter)
        keyword_label.setStyleSheet("background-color: transparent;")
        section3_layout.addWidget(keyword_label)

        self.keyword_entry = QtWidgets.QPlainTextEdit(section3)
        self.keyword_entry.setFixedHeight(100)
        section3_layout.addWidget(self.keyword_entry)

        self.selected_keywords_label = QtWidgets.QLabel("Selected:", section3)
        self.selected_keywords_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_keywords_label.setFont(QtGui.QFont("Arial", 12))
        self.selected_keywords_label.setStyleSheet("background-color: transparent;")
        section3_layout.addWidget(self.selected_keywords_label)

        # Section 4: Submit Button
        section4 = QtWidgets.QFrame(self)
        section4_layout = QtWidgets.QHBoxLayout(section4)
        section4.setLayout(section4_layout)
        self.layout.addWidget(section4)
        self.layout.addSpacing(10)

        submit_button = QtWidgets.QPushButton("Generate", section4)
        submit_button.setFixedWidth(200)
        submit_button.setFixedHeight(50)
        section4_layout.addWidget(submit_button)

        # Connect signals and slots
        submit_button.clicked.connect(self.submit)
        self.directory_entry.textChanged.connect(self.update_selected_directories)
        self.keyword_entry.textChanged.connect(self.update_selected_keywords)

    def create_date_entry(self, parent):
        # Create a separate Tk instance for the DateEntry widget
        root = tk.Tk()
        root.withdraw()  # Hide the Tkinter window
        tkcal = DateEntry(parent, date_pattern="dd-mm-yyyy", showweeknumbers=False, firstweekday="sunday")
        tkcal._top_cal.withdraw()  # Hide the calendar pop-up
        return tkcal

    def submit(self):
        selected_from_date = self.from_date_entry.get_date().strftime("%d-%m-%Y")
        selected_to_date = self.to_date_entry.get_date().strftime("%d-%m-%Y")
        selected_radio = self.radio_var.checkedButton().text()
        keywords = self.keyword_entry.toPlainText().strip()
        selected_directories = [dir.strip() for dir in self.directory_entry.toPlainText().split(",") if dir.strip()]

        QMessageBox.information(
            self, "Form Data",
            f"Selected Directories: {', '.join(selected_directories)}\n"
            f"From Date: {selected_from_date}\n"
            f"To Date: {selected_to_date}\n"
            f"Selected Radio: {selected_radio}\n"
            f"Keywords: {keywords}"
        )

    def update_selected_directories(self):
        text = self.directory_entry.toPlainText().strip()
        count_of_directories = text.count(',')
        if count_of_directories != 0 or count_of_directories < 1:
            last_count_of_directories = count_of_directories
            selected_directories = text.split(',')
            self.selected_directory_label.setText(f"Selected: {''.join(selected_directories)}")

    def update_selected_keywords(self):
        text = self.keyword_entry.toPlainText().strip()
        count_of_keywords = text.count(',')
        if count_of_keywords != 0 or count_of_keywords < 1:
            last_count_of_keywords = count_of_keywords
            selected_keywords = text.split(",")
            self.selected_keywords_label.setText(f"Selected: {''.join(selected_keywords)}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
