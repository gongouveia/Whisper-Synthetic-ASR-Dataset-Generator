import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QLineEdit, QLabel, QButtonGroup, QComboBox, QTextEdit, QFileDialog
from PyQt5.QtCore import QTimer, Qt
from SecondaryWindow.DatasetViewer import NewWindow
from PyQt5.QtGui import QIcon
import time
import random
from Utils.AudioCapture import record_audio_thread
from Utils.Translation import *



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
        self.last_audio = 'No audio generated yet'                                                                                                                #TODO
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Synthetic Speech Generator")  # Setting window title
        self.setFixedSize(650, 500)  # Fixing window size
        self.setWindowIcon(QIcon('Images/fig2.png'))  # Set window icon

        #self.speaker_name_label = QLabel("Speaker Name  ")
        #self.speaker_name_input = QLineEdit()
        #self.speaker_name_input.setFixedSize(100, 20)  # Set size of input box
        #self.speaker_name_input.setText("None")  # Set default value to 5


        self.audio_rate_label = QLabel("Audio Sample Rate: (KHz)  ")
        self.audio_rate_input = QLineEdit()
        self.audio_rate_input.setFixedSize(100, 20)  # Set size of input box
        self.audio_rate_input.setText("16000")  # Set default value to 5

        self.audio_duration_label = QLabel("Audio Duration: (ms)         ")
        self.audio_duration_input = QLineEdit()
        self.audio_duration_input.setFixedSize(100, 20)  # Set size of input box
        self.audio_duration_input.setText("5000")  # Set default value to 10000

        self.transcribe_label = QLabel("Transcribe after Record:")
        self.audio_enhancement_label = QLabel("Metadata to Dataset:")

        self.transcribe_yes_radio = QRadioButton("Yes")
        self.transcribe_no_radio = QRadioButton("No")
        self.enhancement_yes_radio = QRadioButton("Yes")
        self.enhancement_no_radio = QRadioButton("No")

        self.start_button = QPushButton("Capture Audio")
        self.view_dataset_button = QPushButton("View Dataset")
        self.delete_button = QPushButton("Delete Last Audio")
        self.led_widget = LedWidget()
        self.delete_entry_label = QLabel("Language and Model:")
        self.delete_entry_dropdown = QComboBox()
        self.delete_entry_dropdown.addItem("en")
        self.delete_entry_dropdown.addItem("es")
        self.delete_entry_dropdown.addItem("pt")

        self.model_entry_dropdown = QComboBox()
        self.model_entry_dropdown.addItem("large")
        self.model_entry_dropdown.addItem("medium")
        self.model_entry_dropdown.addItem("small")



        self.console = QTextEdit()
        self.console.setReadOnly(True)

        self.transcribe_yes_radio.setChecked(True)
        self.enhancement_yes_radio.setChecked(True)

        hbox_transcribe = QHBoxLayout()
        hbox_transcribe.addWidget(self.transcribe_label)
        hbox_transcribe.addWidget(self.transcribe_yes_radio)
        hbox_transcribe.addWidget(self.transcribe_no_radio)

        hbox_enhancement = QHBoxLayout()
        hbox_enhancement.addWidget(self.audio_enhancement_label)
        hbox_enhancement.addWidget(self.enhancement_yes_radio)
        hbox_enhancement.addWidget(self.enhancement_no_radio)

        hbox_led = QHBoxLayout()
        hbox_led.addWidget(self.led_widget)
        hbox_led.addWidget(self.start_button)

        hbox_audio_speaker = QHBoxLayout()
        hbox_audio_speaker.addWidget(self.speaker_name_label)
        hbox_audio_speaker.addWidget(self.speaker_name_input)
        hbox_audio_speaker.addStret

	    
        #hbox_audio_rate = QHBoxLayout()
        #hbox_audio_rate.addWidget(self.audio_rate_label)
        #hbox_audio_rate.addWidget(self.audio_rate_input)
        #hbox_audio_rate.addStretch(1)  # Add stretch at the end

        hbox_audio_duration = QHBoxLayout()
        hbox_audio_duration.addWidget(self.audio_duration_label)
        hbox_audio_duration.addWidget(self.audio_duration_input)
        hbox_audio_duration.addStretch(1)  # Add stretch at the end

        hbox_delete_entry = QHBoxLayout()
        hbox_delete_entry.addWidget(self.delete_entry_label)
        hbox_delete_entry.addWidget(self.delete_entry_dropdown)
        hbox_delete_entry.addWidget(self.model_entry_dropdown)

        hbox_view_dataset = QHBoxLayout()
        hbox_view_dataset.addWidget(self.view_dataset_button)

        hbox_delete = QHBoxLayout()
        hbox_delete.addWidget(self.delete_button)

        vbox = QVBoxLayout()
#    	vbox.addLayout(hbox_audio_speaker)

        vbox.addLayout(hbox_audio_rate)
        vbox.addLayout(hbox_audio_duration)
        vbox.addLayout(hbox_transcribe)
        vbox.addLayout(hbox_enhancement)
        vbox.addLayout(hbox_delete_entry) # New row for dropdown
        vbox.addLayout(hbox_led)
        vbox.addLayout(hbox_view_dataset)
        vbox.addLayout(hbox_delete)
        vbox.addWidget(self.console)

        self.setLayout(vbox)

        self.start_button.clicked.connect(self.TranscribeFucntion)
        self.transcribe_yes_radio.toggled.connect(self.enableDropdown)
        self.view_dataset_button.clicked.connect(self.openNewWindow)
        self.delete_button.clicked.connect(self.printMessage)  # Connect delete button to function

        self.transcribe_group = QButtonGroup()
        self.transcribe_group.addButton(self.transcribe_yes_radio)
        self.transcribe_group.addButton(self.transcribe_no_radio)

        self.enhancement_group = QButtonGroup()
        self.enhancement_group.addButton(self.enhancement_yes_radio)
        self.enhancement_group.addButton(self.enhancement_no_radio)

    def printMessage(self):
            self.console.append(self.last_audio)  # Append the message to the QTextEdit widget

    def TranscribeFucntion(self):
        audio_duration = int(self.audio_duration_input.text())

        self.disableWidgets()
        self.led_widget.setGreen()
        filename = 'projects/Project/Audios/audio_' + str(random.randint(0, 1e6)) + '.wav'
        record_audio_thread(audio_duration,filename )                                                                    #TODO add sample rate
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.enableWidgets)
    
        self.timer.start(audio_duration)

        self.last_audio  = filename

        save_dataset_csv_audio_text(filename, 'text')
        save_translation_to_txt(filename, 'text')
	
    def disableWidgets(self):
        self.audio_rate_input.setEnabled(False)
        self.audio_duration_input.setEnabled(False)
        
        for button in self.transcribe_group.buttons():
            button.setEnabled(False)
        for button in self.enhancement_group.buttons():
            button.setEnabled(False)
        self.start_button.setEnabled(False)
        self.view_dataset_button.setEnabled(False)
        self.delete_button.setEnabled(False)
        self.delete_entry_dropdown.setEnabled(False)

    def enableWidgets(self):
        self.audio_rate_input.setEnabled(True)
        self.audio_duration_input.setEnabled(True)
        for button in self.transcribe_group.buttons():
            button.setEnabled(True)
        for button in self.enhancement_group.buttons():
            button.setEnabled(True)
        self.start_button.setEnabled(True)
        self.view_dataset_button.setEnabled(True)
        self.delete_button.setEnabled(True)
        self.led_widget.setStyleSheet("background-color: red; border-radius: 10px;")

    def enableDropdown(self, checked):
        if checked:
            self.delete_entry_dropdown.setEnabled(True)
        else:
            self.delete_entry_dropdown.setEnabled(False)

    def openNewWindow(self):
        file_path = 'projects/Project/metadata.csv'
        if file_path:
            self.new_window = NewWindow(file_path)
            self.new_window.show()


