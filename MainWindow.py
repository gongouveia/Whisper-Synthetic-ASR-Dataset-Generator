from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QLineEdit, QLabel, QButtonGroup, QComboBox, QTextEdit, QFileDialog
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
import random
from Utils.AudioCapture import record_audio_thread
from Utils.Translation import *
from DatasetViewer import DataWindow
from SecondaryWindow.FileDropMenu import FileDropWidget
from Utils.ConfigHandle import read_parameters_from_json
import torch
import json
import threading

class LedWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(20, 20)
        self.setStyleSheet("background-color: red; border-radius: 10px;")

    def setGreen(self):
        self.setStyleSheet("background-color: green; border-radius: 10px;")

    def setBlue(self):
        self.setStyleSheet("background-color: blue; border-radius: 10px;")


class SpeechGeneratorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = None
        self.parameters = read_parameters_from_json()
    def initUI(self):
        self.setWindowTitle("Synthetic Speech Generator")
        self.setFixedSize(650, 500)
        self.setWindowIcon(QIcon('Images/fig.png'))

        self.audio_rate_label = QLabel("Audio Sample Rate: (KHz)  ")
        self.audio_rate_input = QLineEdit()
        self.audio_rate_input.setFixedSize(100, 20)
        self.audio_rate_input.setText("16000")

        self.audio_duration_label = QLabel("Audio Duration: (ms)         ")
        self.audio_duration_input = QLineEdit()
        self.audio_duration_input.setFixedSize(100, 20)
        self.audio_duration_input.setText("1000")

        self.transcribe_label = QLabel("Transcribe after Record:")
        self.audio_vad_label = QLabel("Add VAD to Whisper Engine:")

        self.transcribe_yes_radio = QRadioButton("Yes")
        self.transcribe_no_radio = QRadioButton("No")
        self.vad_yes_radio = QRadioButton("Yes")
        self.vad_no_radio = QRadioButton("No")

        self.start_button = QPushButton("◉ Capture Audio")
        self.view_dataset_button = QPushButton("View Dataset")
        self.delete_button = QPushButton("Drop and find audio files")
        self.led_widget = LedWidget()
        self.language_label = QLabel("Language and Model:")
        self.language_dropdown = QComboBox()
        self.language_dropdown.addItems(['english','multilignual'])

        self.model_entry_dropdown = QComboBox()
        self.model_entry_dropdown.addItems(["tiny.en","medium.en", "small.en"])

        self.console = QTextEdit()
        self.console.setReadOnly(True)

        self.transcribe_yes_radio.setChecked(True)
        self.vad_yes_radio.setChecked(True)

        hbox_transcribe = QHBoxLayout()
        hbox_transcribe.addWidget(self.transcribe_label)
        hbox_transcribe.addWidget(self.transcribe_yes_radio)
        hbox_transcribe.addWidget(self.transcribe_no_radio)

        if not torch.cuda.is_available():
            self.console.append(f"INFO: GPU is not available, will not allow to transcribe after each audio recording. Please open Dataset Viewer and transcribe audios in the end.")

            self.transcribe_no_radio.setChecked(True)
            self.transcribe_no_radio.setEnabled(False)
            self.transcribe_yes_radio.setEnabled(False)
        else:
            self.console.append(f"INFO: GPU available, allowed to transcribe after each audio recording. Or transcribe audios in the end.")

        hbox_vad = QHBoxLayout()
        hbox_vad.addWidget(self.audio_vad_label)
        hbox_vad.addWidget(self.vad_yes_radio)
        hbox_vad.addWidget(self.vad_no_radio)

        hbox_led = QHBoxLayout()
        hbox_led.addWidget(self.led_widget)
        hbox_led.addWidget(self.start_button)

        hbox_audio_rate = QHBoxLayout()
        hbox_audio_rate.addWidget(self.audio_rate_label)
        hbox_audio_rate.addWidget(self.audio_rate_input)
        hbox_audio_rate.addStretch(1)

        hbox_audio_duration = QHBoxLayout()
        hbox_audio_duration.addWidget(self.audio_duration_label)
        hbox_audio_duration.addWidget(self.audio_duration_input)
        hbox_audio_duration.addStretch(1)

        hbox_language = QHBoxLayout()
        hbox_language.addWidget(self.language_label)
        hbox_language.addWidget(self.language_dropdown)
        hbox_language.addWidget(self.model_entry_dropdown)
        self.new_button = QPushButton("Set Model")
        hbox_language.addWidget(self.new_button)
        hbox_view_dataset = QHBoxLayout()
        hbox_view_dataset.addWidget(self.view_dataset_button)

        hbox_delete = QHBoxLayout()
        hbox_delete.addWidget(self.delete_button)
    
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_audio_rate)
        vbox.addLayout(hbox_audio_duration)
        vbox.addLayout(hbox_transcribe)
        vbox.addLayout(hbox_vad)
        vbox.addLayout(hbox_language)
        vbox.addLayout(hbox_led)
        vbox.addLayout(hbox_view_dataset)
        vbox.addLayout(hbox_delete)
        vbox.addWidget(self.console)

        self.setLayout(vbox)
        
        
        self.new_button.clicked.connect(self.printMessage)

        self.start_button.clicked.connect(self.TranscribeFucntion)
        self.view_dataset_button.clicked.connect(self.openDataWindow)
        self.delete_button.clicked.connect(self.openFileDropWindow)

        self.transcribe_group = QButtonGroup()
        self.transcribe_group.addButton(self.transcribe_yes_radio)
        self.transcribe_group.addButton(self.transcribe_no_radio)

        self.vad_group = QButtonGroup()
        self.vad_group.addButton(self.vad_yes_radio)
        self.vad_group.addButton(self.vad_no_radio)

        self.language_dropdown.currentTextChanged.connect(self.updateModelDropdown)
        

    def TranscribeFucntion(self):
        audio_duration = int(self.audio_duration_input.text())
        sample_rate = int(self.audio_rate_input.text())
        self.disableWidgets()
        self.led_widget.setGreen()
        wav_name = str(random.randint(0, 1e6)) + '.wav'
        filename =  self.parameters['audios_path'] + '/audio_' + wav_name
        record_audio_thread(audio_duration, filename)
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.enableWidgets)
        self.timer.start(audio_duration)

        if self.transcribe_no_radio.isChecked(): 
            save_dataset_csv_audio_text(self.parameters['metadata'],"Audios/"+wav_name, 'No trancription found.',sample_rate, audio_duration)

        else:
            self.console.append('Transcribing audio')                                              #TODO not yet done
            #text =whisper_translation(self.model,'en', filename)
            save_dataset_csv_audio_text(self.parameters['metadata'],"Audios/"+wav_name, 'transcribed',sample_rate, audio_duration)
            self.console.append('Done')


        save_translation_to_txt(filename, 'INFO: Not translated. Press "Translate all files" to transcribe remaining files')

    def disableWidgets(self):                                                   #TODO disableWidgets and enableWidgets can be same function
        self.audio_rate_input.setEnabled(False)
        self.audio_duration_input.setEnabled(False)

        for button in self.transcribe_group.buttons():
            button.setEnabled(False)
        for button in self.vad_group.buttons():
            button.setEnabled(False)
        self.start_button.setEnabled(False)
        self.view_dataset_button.setEnabled(False)
        self.delete_button.setEnabled(False)
        self.language_dropdown.setEnabled(False)

    def enableWidgets(self):
        self.audio_rate_input.setEnabled(True)
        self.audio_duration_input.setEnabled(True)
        for button in self.transcribe_group.buttons():
            button.setEnabled(True)
        for button in self.vad_group.buttons():
            button.setEnabled(True)
        self.start_button.setEnabled(True)
        self.view_dataset_button.setEnabled(True)
        self.delete_button.setEnabled(True)
        self.led_widget.setStyleSheet("background-color: red; border-radius: 10px;")

    def updateModelDropdown(self, text):
        if text == "en":
            self.model_entry_dropdown.clear()
            self.model_entry_dropdown.addItems(["tiny.en","medium.en", "small.en"])
        else:
            self.model_entry_dropdown.clear()
            self.model_entry_dropdown.addItems(["large", "medium",'small'])

    def openDataWindow(self):
        metadata = self.parameters['metadata']
        if metadata:
            self.new_window = DataWindow(metadata)
            self.new_window.show()


    def openFileDropWindow(self):
        audio_path = self.parameters['audios_path']
        metadata = self.parameters['metadata']

        self.new_window = FileDropWidget(metadata, audio_path)
        self.new_window.show()


    def printMessage(self):
        self.console.append(f'Setting up model, please do not close while model is not loaded.')
        model_option = self.model_entry_dropdown.currentText()
        vad_option = self.vad_yes_radio.isChecked()
        threading.Thread(target=self.load_translation_model, args=(model_option,)).start()


    def load_translation_model(self, model_option):
        self.model = load_translation_model(model_size=model_option)
        self.console.append(f'Model loaded: {model_option}')
