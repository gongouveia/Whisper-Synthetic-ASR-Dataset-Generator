import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QPushButton, QMessageBox, QApplication, QHeaderView, QSizePolicy, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os
import csv

class NewWindow(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.setWindowTitle("Data Viewer")  # Setting window title
        self.setFixedSize(800, 600)  # Fixing window size
        self.setWindowIcon(QIcon('Images/fig2.png'))  # Set window icon

        self.file_path = file_path

        self.table_view = QTableView()
        self.model = QStandardItemModel(self)
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # Adjust column widths

        self.loadCSV(file_path)

        self.delete_button = QPushButton("Delete Row")
        self.delete_button.clicked.connect(self.deleteRow)
        self.delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy

        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.saveChanges)
        self.save_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy
        
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refreshCSV)
        self.refresh_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy
        
        self.transcribe_button = QPushButton("Transcribe Remaining Files")
        self.transcribe_button.clicked.connect(self.transcribeRemainingFiles)
        self.transcribe_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Setting fixed size policy


        # Set the width of all buttons to the width of the widest button
        self.delete_button.setFixedWidth(100)
        self.save_button.setFixedWidth(150)
        self.refresh_button.setFixedWidth(150)
        self.transcribe_button.setFixedWidth(250)

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

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Terminal box
        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.terminal.setFixedHeight(100)  # Adjusting height of the terminal box
        layout.addWidget(self.terminal)

    def loadCSV(self, csv_file):
        try:
            with open(csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
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

    # def deleteRow(self):
    #     selected = self.table_view.selectedIndexes()
    #     if selected:
    #         rows_to_delete = set(index.row() for index in selected)
    #         for row in sorted(rows_to_delete, reverse=True):
    #             self.model.removeRow(row)
        

    def deleteRow(self):                                                  #melhorar esta função
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
                if os.path.exists(row_data[0].replace('.wav','.txt')):                                                #TODO    .replace('.wav','.txt').replace('/Audios','/Translations' nesta linha tmb
                    os.remove(row_data[0].replace('.wav','.txt').replace('/Audios','/Translations'))
    def saveChanges(self):
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
        self.model.clear()
        self.loadCSV(self.file_path)

    def transcribeRemainingFiles(self):
        self.terminal.append("fiugfah")


