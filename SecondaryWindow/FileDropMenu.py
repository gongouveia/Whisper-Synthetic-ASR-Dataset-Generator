import sys
import os
import shutil
import wave
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class FileDropWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Drop Menu")
        self.setGeometry(100, 100, 500, 300)
        self.setWindowIcon(QIcon('Images/fig.png'))  # Set window icon

        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)

        self.drop_label = QLabel("Drop .wav files here", self)
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.drop_label)

        self.select_files_button = QPushButton("Select Files", self)
        self.select_files_button.clicked.connect(self.select_files)
        self.layout.addWidget(self.select_files_button)

        self.output_textedit = QTextEdit(self)
        self.output_textedit.setReadOnly(True)  # Make it read-only
        self.output_textedit.setMaximumHeight(100)  # Set maximum height
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
            dropped_folder = 'Dropped'
            if not os.path.exists(dropped_folder):
                os.makedirs(dropped_folder)
            for file in wav_files:
                try:
                    destination_path = os.path.join(dropped_folder, os.path.basename(file))
                    shutil.copy(file, destination_path)
                    with wave.open(destination_path, 'rb') as wav_file:
                        frames = wav_file.getnframes()
                        rate = wav_file.getframerate()
                        duration = frames / float(rate)
                        self.output_textedit.append(f"File: {destination_path}, Length: {duration:.2f} seconds, Sample Rate: {rate} Hz")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error processing {file}: {str(e)}")

    def select_files(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("WAV files (*.wav)")
        if file_dialog.exec_():
            files = file_dialog.selectedFiles()
            dropped_folder = 'Dropped'
            if not os.path.exists(dropped_folder):
                os.makedirs(dropped_folder)
            for file in files:
                try:
                    destination_path = os.path.join(dropped_folder, os.path.basename(file))
                    shutil.copy(file, destination_path)
                    self.output_textedit.append(f"File: {destination_path} added via Select Files button")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error processing {file}: {str(e)}")

if __name__ == "__main__":   
    app = QApplication(sys.argv)
    widget = FileDropWidget()
    widget.show()
    sys.exit(app.exec_())
