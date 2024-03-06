import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QPushButton, QMessageBox, QApplication, QHeaderView, QSizePolicy, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
import os
import csv

class DataWindow(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.setWindowTitle("Data Viewer")  # Setting window title
        self.setFixedSize(800, 600)  # Fixing window size
        self.setWindowIcon(QIcon('Images/fig.png'))  # Set window icon

        self.file_path = file_path

        self.table_view = QTableView()
        self.model = QStandardItemModel(self)
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Adjust column widths to fill the available space
        self.table_view.verticalHeader().setVisible(False)  # Hide vertical header

        self.loadCSV(file_path)

        self.delete_button = QPushButton("Delete Row")
        self.delete_button.clicked.connect(self.deleteRow)
        self.delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy

        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.saveChanges)
        self.save_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy
        
        self.refresh_button = QPushButton("Refresh Data View")
        self.refresh_button.clicked.connect(self.refreshCSV)
        self.refresh_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy
        
        self.transcribe_button = QPushButton("Transcribe Remaining Files")
        self.transcribe_button.clicked.connect(self.transcribeRemainingFiles)
        self.transcribe_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy

        self.extra_button = QPushButton("Export to Huggingface")
        self.extra_button.clicked.connect(self.showMessage)
        self.extra_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy
        self.extra_button.setEnabled(False)  # Disable the button initially

        # Set the width of all buttons to the width of the widest button
        self.delete_button.setFixedWidth(100)
        self.save_button.setFixedWidth(150)
        self.refresh_button.setFixedWidth(160)
        self.transcribe_button.setFixedWidth(250)
        self.extra_button.setFixedWidth(160)

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)

        # Create a QHBoxLayout to hold the buttons
        button_layout = QHBoxLayout()

        # Add the refresh button to the left side
        button_layout.addWidget(self.refresh_button)

        # Add spacers to push other buttons to the right
        button_layout.addStretch(1)

        # Add the other buttons to the right side
        button_layout.addWidget(self.transcribe_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.save_button)
        # button_layout.addWidget(self.extra_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        self.setLayout(layout)
        layout.addWidget(self.extra_button)

        # Terminal box
        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.terminal.setFixedHeight(100)  # Adjusting height of the terminal box
        layout.addWidget(self.terminal)


    def loadCSV(self, csv_file):
        try:
            with open(csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)  # Get the header from the first row
                self.model.setHorizontalHeaderLabels(header)  # Set the header labels
                for i, row in enumerate(reader):
                    items = []
                    for j, field in enumerate(row):
                        item = QStandardItem(field)
                        if j == 1:  # Allow editing only for the second column
                            item.setEditable(True)
                        else:
                            item.setEditable(False)
                        items.append(item)
                    self.model.appendRow(items)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while opening the CSV file:\n{str(e)}")

    def deleteRow(self):
        selected = self.table_view.selectedIndexes()
        if selected:
            rows_to_delete = set(index.row() for index in selected)
            for row in sorted(rows_to_delete, reverse=True):
                # Print the data of the row before deleting
                row_data = []
                for col in range(self.model.columnCount()):
                    item = self.model.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  # Append an empty string if item is None
                print("Deleting row:", row_data)
                self.model.removeRow(row)
                if os.path.exists(row_data[0]):
                    os.remove(row_data[0])
                if os.path.exists(row_data[0].replace('.wav','.txt')):
                    os.remove(row_data[0].replace('.wav','.txt').replace('/Audios','/Translations'))

    def saveChanges(self):
        self.terminal.append("Changes Saved")

        self.saveCSV()
        QMessageBox.information(self, "Save Changes", "Changes saved successfully!")

    def saveCSV(self):
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in range(self.model.rowCount()):
                    data = [self.model.item(row, col).text() for col in range(self.model.columnCount())]
                    writer.writerow(data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving the CSV file:\n{str(e)}")

    def refreshCSV(self):
        self.terminal.append("Refreshed Data Viewer")
        self.model.clear()
        self.loadCSV(self.file_path)

    def transcribeRemainingFiles(self):
        transcribed_files = self.find_files_to_transcribe()
        self.terminal.append("Transcribing Remaining files. Transcriptions will be saved automatically at each file iteration.")
        self.terminal.append("Transcribed Files:")
        for file in transcribed_files:
            # Set 'Transcribed' in the second column of the current row
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == file:
                    item = QStandardItem('Transcribed')
                    self.model.setItem(row, 1, item)  # Setting the second column to 'Transcribed'
                    break
            self.terminal.append(file)

    def find_files_to_transcribe(self):
        transcribed_files = []
        for row in range(self.model.rowCount()):
            transcription = self.model.item(row, 1).text().strip()
            if transcription == 'text':
                file_path = self.model.item(row, 0).text()
                transcribed_files.append(file_path)
        return transcribed_files

    def showMessage(self):
        QMessageBox.information(self, "Information", "You clicked the extra button!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataWindow("your_csv_file.csv")  # Replace "your_csv_file.csv" with the path to your CSV file
    window.show()
    sys.exit(app.exec_())
