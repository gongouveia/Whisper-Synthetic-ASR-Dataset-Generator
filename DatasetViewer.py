import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QPushButton, QMessageBox, QApplication, QHeaderView, QSizePolicy, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
import os
import csv
from Utils.ConfigHandle import read_parameters_from_json
import threading
from Utils.Translation import load_translation_model, whisper_translation

class DataWindow(QWidget):
    def __init__(self, file_path):
        super().__init__()

        self.file_path = file_path

        self.transcriber = load_translation_model()

        self.setWindowTitle("Data Viewer") 
        self.setFixedSize(800, 600) 
        self.setWindowIcon(QIcon('Images/fig.png'))  

        self.table_view = QTableView()
        self.model = QStandardItemModel(self)
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Adjust column widths to fill the available space
        self.table_view.verticalHeader().setVisible(False)  # Hide vertical header

        self.loadCSV(file_path)

        self.delete_button = QPushButton("Delete Row")
        self.delete_button.clicked.connect(self.deleteRow)
        self.delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)   

        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.saveChanges)
        self.save_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)   
        
        self.refresh_button = QPushButton("Refresh Data View")
        self.refresh_button.clicked.connect(self.refreshCSV)
        self.refresh_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)   
        
        self.transcribe_button = QPushButton("Transcribe Remaining Files")
        self.transcribe_button.clicked.connect(self.transcribeRemainingFiles)
        self.transcribe_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  

        self.extra_button = QPushButton("Export to Huggingface")
        self.extra_button.clicked.connect(self.showMessage)
        self.extra_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  
        self.extra_button.setEnabled(False)  # Disable the button initially

        self.delete_button.setFixedWidth(100)
        self.save_button.setFixedWidth(150)
        self.refresh_button.setFixedWidth(160)
        self.transcribe_button.setFixedWidth(250)
        self.extra_button.setFixedWidth(160)

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addStretch(1)

        button_layout.addWidget(self.transcribe_button)
        button_layout.addWidget(self.delete_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        self.setLayout(layout)
        layout.addWidget(self.extra_button)

        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.terminal.setFixedHeight(100)  
        layout.addWidget(self.terminal)


    def loadCSV(self, csv_file):
        try:
            with open(csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader) 
                self.model.setHorizontalHeaderLabels(header)  
                for i, row in enumerate(reader):
                    items = []
                    for j, field in enumerate(row):
                        item = QStandardItem(field)
                        if j == 1:  
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
                row_data = []
                for col in range(self.model.columnCount()):
                    item = self.model.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  
                print("Deleting row:", row_data)
                self.model.removeRow(row)
                if os.path.exists(row_data[0]):
                    os.remove(row_data[0])
                if os.path.exists(row_data[0].replace('.wav','.txt')):
                    os.remove(row_data[0].replace('.wav','.txt').replace('/Audios','/Translations'))
        self.saveCSV()
        QMessageBox.information(self, "Save Changes", "Changes saved successfully!")


    def saveChanges(self):
        self.terminal.append("Changes Saved")

        self.saveCSV()
        QMessageBox.information(self, "Save Changes", "Changes saved successfully!")

    def saveCSV(self):
        try:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['file_name', 'transcription','sample_rate','duration_ms'])
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
        parameters = read_parameters_from_json('config.json')
        audio_path =parameters['audios_path']
        transcribed_files = self.find_files_to_transcribe()
        self.terminal.append("Transcribing Remaining files. Transcriptions will be saved automatically at each file iteration.")
        self.terminal.append("Transcribed Files:")
        for file in transcribed_files:
            print(file)



            text = whisper_translation(self.transcriber, 'en', audio_path +'/'+ file)                                                                                    #TODO


            # Set 'Transcribed' in the second column of the current row                                                                                                #transcribe Here
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == file:
                    item = QStandardItem(text)
                    self.model.setItem(row, 1, item)  # Setting the second column to 'Transcribed'
                    break
            self.terminal.append(file)
            self.saveCSV()
        QMessageBox.information(self, "Save Changes", "Changes saved successfully!")



    def find_files_to_transcribe(self):
        transcribed_files = []
        for row in range(self.model.rowCount()):
            transcription = self.model.item(row, 1).text().strip()
            if transcription in ['No trancription found.',"Not translated: Coming from file drop."]:                    #this is the cases in which
                file_path = self.model.item(row, 0).text()
                transcribed_files.append(file_path)
        return transcribed_files

    def showMessage(self):
        QMessageBox.information(self, "Information", "You clicked the extra button!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataWindow("projects/Project/metadata.csv") 
    window.show()
    sys.exit(app.exec_())
