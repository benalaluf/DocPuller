import sys
import qdarktheme
import tkinter as tk
from tkinter import filedialog

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import (
    QPixmap, QPalette, QBrush, QFont, QTextCharFormat, QTextCursor, QIcon
)
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QDateTimeEdit, QComboBox, QLineEdit, QFormLayout
)


class BoldRedTextEdit(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super(BoldRedTextEdit, self).__init__(*args, **kwargs)
        self.previous_text = ''
        self.previous_space_count = 0
        self.cursorPositionChanged.connect(self.format_words)

    def format_words(self):
        current_text = self.toPlainText()
        if current_text.count(' ') == 0:
            self.previous_space_count = 0
            self.previous_text = ''

        if current_text.count(' ') > self.previous_space_count:
            cursor = self.textCursor()
            self.previous_space_count = current_text.count(' ')

            # Apply formatting
            format_words = QTextCharFormat()
            format_words.setFontWeight(QFont.Bold)
            # format_words.setFontItalic(True)
            format_words.setForeground(Qt.cyan)

            cursor.setPosition(len(self.previous_text))
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)
            cursor.setCharFormat(format_words)
            self.previous_text = current_text


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DocPuller')
        self.setWindowIcon(QIcon('backgrond.jpeg'))
        self.setGeometry(100, 100, 700, 850)

        layout = QVBoxLayout()

        # Headline
        headline = QLabel('DocPuller', self)
        headline.setFont(QFont('Arial', 48, QFont.Bold))
        headline.setAlignment(Qt.AlignCenter)
        headline.setStyleSheet("padding: px50")
        layout.addWidget(headline)

        # Mode selection buttons
        mode_selection_layout = QHBoxLayout()

        self.usb_button = QPushButton('USB', self)
        self.usb_button.setCheckable(True)
        self.usb_button.setChecked(True)
        self.usb_button.clicked.connect(lambda: self.change_mode(0))
        self.usb_button.setStyleSheet("""
            QPushButton {
                font: 18px;
                border: 2px solid #555555;
                border-radius: 15px;
                padding: 12px;
                background-color: #555555;
                color: #ffffff;
            }
            QPushButton:checked {
                background-color: #ffffff;
                color: #555555;
            }
        """)
        mode_selection_layout.addWidget(self.usb_button)

        self.ftp_button = QPushButton('FTP', self)
        self.ftp_button.setCheckable(True)
        self.ftp_button.setChecked(False)
        self.ftp_button.clicked.connect(lambda: self.change_mode(1))
        self.ftp_button.setStyleSheet("""
            QPushButton {
                font: 18px;
                border: 2px solid #555555;
                border-radius: 15px;
                padding: 12px;
                background-color: #555555;
                color: #ffffff;
            }
            QPushButton:checked {
                background-color: #ffffff;
                color: #555555;
            }
        """)
        mode_selection_layout.addWidget(self.ftp_button)

        layout.addLayout(mode_selection_layout)

        # Form layout for input fields
        form_layout = QFormLayout()
        form_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)



        # Directory Choosing Entry
        self.directory_entry = BoldRedTextEdit(self)
        self.directory_entry.setFont(QFont('Ariel'))
        self.directory_entry.setPlaceholderText('Enter directory names (separated by spaces)')
        self.directory_entry.setFixedHeight(70)
        self.directory_entry.setStyleSheet("font-size: 16px;")
        self.directory_label = QLabel('Directories:')
        self.directory_label.setStyleSheet("""
            font-size: 20px;
        """)
        form_layout.addRow(self.directory_label, self.directory_entry)

        # Date Entry (From and To)
        self.date_from = QDateTimeEdit(self)
        self.date_from.setDisplayFormat("dd/MM/yyyy")
        self.date_from.setCalendarPopup(True)
        self.date_from.setStyleSheet("""
            QDateTimeEdit {
                border: 2px solid #555555;
                border-radius: 15px;
                padding: 10px;
                font: 16px;
            }
        """)
        self.date_from_label = QLabel('Date From:')
        self.date_from_label.setStyleSheet("""
            font-size: 20px;
            text-align: left;
        """)
        form_layout.addRow(self.date_from_label, self.date_from)

        self.date_to = QDateTimeEdit(self)
        self.date_to.setDisplayFormat("dd/MM/yyyy")
        self.date_to.setCalendarPopup(True)
        self.date_to.setDateTime(QDateTime.currentDateTime())
        self.date_to.setStyleSheet("""
            QDateTimeEdit {
                border: 2px solid #555555;
                border-radius: 15px;
                padding: 10px;
                font: 16px;
            }
        """)
        self.date_to_label = QLabel('Date To:')
        self.date_to_label.setStyleSheet("""
            font-size: 20px;
            text-align: left;
        """)
        form_layout.addRow(self.date_to_label, self.date_to)

        # File Type Entry
        self.file_type_entry = QComboBox(self)
        self.file_type_entry.addItem("Document")
        self.file_type_entry.addItem("Image")
        self.file_type_entry.addItem("Audio")
        self.file_type_entry.addItem("Video")
        self.file_type_entry.setStyleSheet("""
            QComboBox {
                border: 2px solid #555555;
                border-radius: 15px;
                padding: 10px;
                font: 16px;
            }
        """)
        self.file_type_label = QLabel('File Type:')
        self.file_type_label.setStyleSheet("""
            font-size: 20px;
        """)
        form_layout.addRow(self.file_type_label, self.file_type_entry)

        # Keyword Entry
        self.keyword_entry = BoldRedTextEdit(self)
        self.keyword_entry.setPlaceholderText('Enter keywords (separated by spaces)')
        self.keyword_entry.setFixedHeight(70)
        self.keyword_entry.setStyleSheet("font-size: 16px;")

        self.keyword_label = QLabel('Keywords:')
        self.keyword_label.setStyleSheet("""
            font-size: 20px;
            text-align: left;
        """)
        form_layout.addRow(self.keyword_label, self.keyword_entry)
        layout.addLayout(form_layout)
        form_layout.setLabelAlignment(Qt.AlignLeft)

        # FTP Server IP and Port
        self.server_ip_label = QLabel('Server IP:')
        self.server_ip_entry = QLineEdit(self)
        self.server_port_label = QLabel('Server Port:')
        self.server_port_entry = QLineEdit(self)

        self.server_ip_label.setParent(None)
        self.server_ip_entry.setParent(None)
        self.server_port_label.setParent(None)
        self.server_port_entry.setParent(None)

        # Generate Button
        self.generate_button = QPushButton('Generate', self)
        self.generate_button.clicked.connect(self.generate)

        self.generate_button.setStyleSheet("""
            QPushButton {
                font: 18px;
                border: 2px solid #555555;
                border-radius: 15px;
                padding: 12px;
                background-color: #555555;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #777777;
            }
        """)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)
        self.update_background()

    def update_background(self):
        background_image_path = 'GUI/macos.jpeg'
        background = QPixmap(background_image_path).scaled(
            self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation
        )
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.update_background()
        super(MainWindow, self).resizeEvent(event)

    def change_mode(self, index):
        if index == 0:  # USB mode
            self.ftp_button.setChecked(False)
            self.usb_button.setChecked(True)
            self.server_ip_label.setParent(None)
            self.server_ip_entry.setParent(None)
            self.server_port_label.setParent(None)
            self.server_port_entry.setParent(None)
        else:  # FTP mode
            self.usb_button.setChecked(False)
            self.ftp_button.setChecked(True)
            self.layout().insertWidget(3, self.server_ip_label)
            self.layout().insertWidget(4, self.server_ip_entry)
            self.layout().insertWidget(5, self.server_port_label)
            self.layout().insertWidget(6, self.server_port_entry)





    def generate(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askdirectory()
        print(file_path)
        # Retrieve values from the entries
        directories = self.directory_entry.toPlainText().split()
        date_from = self.date_from.dateTime().toString("dd-MM-yyyy")
        date_to = self.date_to.dateTime().toString("dd-MM-yyyy")
        file_type = self.file_type_entry.currentText()
        keywords = self.keyword_entry.toPlainText().split()

        # Print the retrieved values
        print("Directories:", directories)
        print("Date From:", date_from)
        print("Date To:", date_to)
        print("File Type:", file_type)
        print("Keywords:", keywords)


class DocPullerGUI:

    def main(self):
        app = QApplication(sys.argv)
        qdarktheme.setup_theme()
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())

