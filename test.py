import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit, QPushButton, \
    QFileDialog, QDateTimeEdit, QComboBox, QGraphicsOpacityEffect, QLineEdit, QFormLayout
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont, QTextCharFormat, QTextCursor, QIcon
from PyQt5.QtCore import Qt, QDateTime


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
            format_words.setFontItalic(True)
            format_words.setForeground(Qt.red)

            cursor.setPosition(len(self.previous_text))
            cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)
            cursor.setCharFormat(format_words)
            self.previous_text = current_text


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DocPuller')
        self.setWindowIcon(QIcon('background.jpeg'))
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        # Headline
        headline = QLabel('DocPuller', self)
        headline.setFont(QFont('Arial', 24))
        headline.setAlignment(Qt.AlignCenter)
        layout.addWidget(headline)

        # Mode selection buttons
        mode_selection_layout = QHBoxLayout()
        self.usb_button = QPushButton('USB', self)
        self.usb_button.clicked.connect(lambda: self.change_mode(0))
        self.usb_button.setStyleSheet("""
            QPushButton {
                font: 14px;
                border: 1px solid gray;
                border-radius: 5px;
                padding: 5px;
                background-color: white;
                color: black;
            }
            QPushButton:hover {
                background-color: rgba(200, 200, 200, 50);
            }
        """)
        mode_selection_layout.addWidget(self.usb_button)

        self.ftp_button = QPushButton('FTP', self)
        self.ftp_button.clicked.connect(lambda: self.change_mode(1))
        self.ftp_button.setStyleSheet("""
            QPushButton {
                font: 14px;
                border: 1px solid gray;
                border-radius: 5px;
                padding: 5px;
                background-color: white;
                color: black;
            }
            QPushButton:hover {
                background-color: rgba(200, 200, 200, 50);
            }
        """)
        mode_selection_layout.addWidget(self.ftp_button)

        layout.addLayout(mode_selection_layout)

        # FTP Server IP and Port
        self.server_ip_label = QLabel('Server IP:')
        self.server_ip_entry = QLineEdit(self)
        self.server_port_label = QLabel('Server Port:')
        self.server_port_entry = QLineEdit(self)

        # Form layout for input fields
        form_layout = QFormLayout()

        # Directory Choosing Entry
        self.directory_entry = BoldRedTextEdit(self)
        self.directory_entry.setPlaceholderText('Enter directory names (separated by spaces)')
        self.directory_entry.setFixedHeight(50)
        form_layout.addRow(QLabel('Directories:'), self.directory_entry)

        # Date Entry (From and To)
        self.date_from = QDateTimeEdit(self)
        self.date_from.setDisplayFormat("dd/MM/yyyy")
        self.date_from.setCalendarPopup(True)
        self.date_from.autoFillBackground()
        form_layout.addRow(QLabel('Date From:'), self.date_from)

        self.date_to = QDateTimeEdit(self)
        self.date_to.setDisplayFormat("dd/MM/yyyy")
        self.date_to.setCalendarPopup(True)
        self.date_to.setDateTime(QDateTime.currentDateTime())
        form_layout.addRow(QLabel('Date To:'), self.date_to)

        # File Type Entry
        self.file_type_entry = QComboBox(self)
        self.file_type_entry.addItem("Document")
        self.file_type_entry.addItem("Image")
        self.file_type_entry.addItem("Audio")
        self.file_type_entry.addItem("Video")
        form_layout.addRow(QLabel('File Type:'), self.file_type_entry)

        # Keyword Entry
        self.keyword_entry = BoldRedTextEdit(self)
        self.keyword_entry.setPlaceholderText('Enter keywords (separated by spaces)')
        self.keyword_entry.setFixedHeight(50)
        form_layout.addRow(QLabel('Keywords:'), self.keyword_entry)
        layout.addLayout(form_layout)

        # Generate Button
        self.generate_button = QPushButton('Generate', self)
        self.generate_button.setStyleSheet("""
            QPushButton {
                font: 14px;
                border: 1px solid gray;
                border-radius: 5px;
                padding: 5px;
                background-color: white;
                color: black;
            }
            QPushButton:hover {
                background-color: rgba(200, 200, 200, 50);
            }
        """)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)
        self.update_background()

    def update_background(self):
        background_image_path = 'background.jpeg'
        background = QPixmap(background_image_path).scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(palette)


    def resizeEvent(self, event):
        self.update_background()
        super(MainWindow, self).resizeEvent(event)

    def change_mode(self, index):
        if index == 1:  # FTP mode
            self.layout().insertWidget(3, self.server_ip_label)
            self.layout().insertWidget(4, self.server_ip_entry)
            self.layout().insertWidget(5, self.server_port_label)
            self.layout().insertWidget(6, self.server_port_entry)
        else:  # USB mode
            self.layout().removeWidget(self.server_ip_label)
            self.layout().removeWidget(self.server_ip_entry)
            self.layout().removeWidget(self.server_port_label)
            self.layout().removeWidget(self.server_port_entry)
            self.server_ip_label.setParent(None)
            self.server_ip_entry.setParent(None)
            self.server_port_label.setParent(None)
            self.server_port_entry.setParent(None)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
