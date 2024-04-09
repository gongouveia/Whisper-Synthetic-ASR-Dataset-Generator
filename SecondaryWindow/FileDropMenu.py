import sys
import os
import shutil
import wave
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

# from Utils.Translation import save_dataset_csv_audio_text


class FileDropWidget(QWidget):
    def __init__(self,metadata_path, new_path):
        super().__init__()

        self.new_path = new_path
        self.metadata_file = metadata_path


        self.setWindowTitle("File Drop Menu")
        self.setGeometry(100, 100, 500, 200)
        self.setWindowIcon(QIcon('Images/fig.png'))  

        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)

        self.drop_label = QLabel("Drop .wav files here or use the Select Files button", self)
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.drop_label)

        self.select_files_button = QPushButton("Select Files", self)
        self.select_files_button.clicked.connect(self.select_files)
        self.layout.addWidget(self.select_files_button)

        self.output_textedit = QTextEdit(self)
        self.output_textedit.setReadOnly(True)  
        self.layout.addWidget(self.output_textedit)



    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        wav_files = [file for file in files if file.endswith('.wav')]
        if len(wav_files) != len(files):
            QMessageBox.warning(self, "Warning", "Only WAV files are allowed!")
        else:
            if not os.path.exists(self.new_path):
                os.makedirs(self.new_path)
            for file in wav_files:
                try:
                    destination_path = os.path.join(self.new_path, os.path.basename(file))
                    shutil.copy(file, destination_path)

                    print(os.path.basename(file))
                    


                    with wave.open(destination_path, 'rb') as wav_file:
                        frames = wav_file.getnframes()
                        rate = wav_file.getframerate()
                        duration = frames / float(rate)
                        self.output_textedit.append(f"File: {destination_path}, Length: {duration:.2f} seconds, Sample Rate: {rate} Hz")

                    text_file = open(self.metadata_file, "a")  #name defined by hf Audio Datasets, kind adoing it now
                    text_file.write(f"{os.path.basename(file)},{'Not translated: Coming from file drop.'},{int(rate)}, {int(duration)}\n")
                    text_file.close()

                    
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error processing {file}: {str(e)}")

    def select_files(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("WAV files (*.wav)")
        if file_dialog.exec_():
            files = file_dialog.selectedFiles()
            if not os.path.exists(self.new_path):
                os.makedirs(self.new_path)
            for file in files:
                try:
                    destination_path = os.path.join(self.new_path, os.path.basename(file))
                    shutil.copy(file, destination_path)
                    self.output_textedit.append(f"File: {destination_path} added via Select Files button")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error processing {file}: {str(e)}")

