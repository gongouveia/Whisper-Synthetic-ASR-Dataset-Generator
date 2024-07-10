# Synthetic Speech Dataset Generator (SpeechGen)

With the rise of ASR/NLP open source projects democratizing the AI human-machine interface, the necessity for better ASR datasets has grown. WhisperTemple provides a simple-to-use platform to create synthetic speech datasets, pairing audio and text. Powered by faster-whisper, WhisperTemple allows synthetic translations to be edited in a UI Data viewer. The user interface, created using PyQt5, runs entirely on a local machine.

## Overview
This application serves as a Synthetic Speech Generator, enabling users to transcribe captured audio and manage generated datasets. It provides a user-friendly interface for configuring audio parameters, transcription options, and dataset management.

![Screenshot 2024-06-16 223519](https://github.com/gongouveia/Whisper-Temple-Synthetic-ASR-Dataset-Generator/assets/68733294/24d41a0c-3592-4a0d-8c0d-61aa1aac83c1)

## Features
- **Audio Capture**: Users can capture audio samples with customizable settings such as sample rate and duration.
- **Transcription**: Provides the option to transcribe captured audio into text.
- **Audio Metadata**: Allows adding metadata to the dataset, such as audio sample rate and duration.
- **Dataset Management**: Enables users to view, delete, and manage entries in the generated dataset.
- **Export**: Allows exporting of the dataset for further processing or Hugging Face 🤗.

## Future Releases
- Adding metadata to each dataset entry, such as audio sample rate, length, or speaker gender and age.
- Updating ReadMe with UI screenshot and video.

## Installation (Experimental. Not yet complete; will do PyPI and conda install)
First, create and activate a new virtual environment using `conda` or `virtualenv`. Then follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/gongouveia/Synthetic-Speech-Dataset-Generator.git
    ```
2. Install dependencies:
    ```bash
    conda env create -f req.yml
    ```
3. Follow the instructions in the Usage Section.

## Usage
1. Launch the application and create or continue a project by running:
    ```bash
    python temple.py --project <default:Project> --theme <default:'auto', 'light', 'dark'>
    ```
2. Export the audio dataset project to Hugging Face using:
    ```bash
    python export.py --project <default:Project> --language <default:'en'>
    ```
    For more information, see:
    ```bash
    python export.py --help
    ```
3. Configure audio capture parameters such as sample rate in KHz (`default: 16000`) and duration in milliseconds (`default: 5000`).
4. If CUDA is found, transcribe audio records at the end of each recording. Otherwise, batch transcribe the audios in the DatasetViewer.
5. Choose whether to use VAD (Voice Activity Detection) in transcription or not. The default is enabled for faster transcription.
6. Click on "Capture Audio" to start a new audio recording.
7. View and manage the audio dataset using provided menu options.
8. Edit weak transcriptions to create a more robust training dataset for Whisper.

## Notes
- If the language argument is set to 'en', the languages dropdown menu is not available.
- If option 3 is disabled, transcribe all captured audios in the dataset viewer window. You can add audios to the audio dataset by pasting them in the `/Audios` folder under your desired project.

### Configuration
- **Audio Sample Rate**: Set the sample rate for audio capture (in KHz).
- **Audio Duration**: Define the duration of audio samples to capture (in milliseconds).
- **Transcribe**: Choose whether to transcribe captured audio (Yes/No).
- **VAD**: Enable or disable VAD in transcription (Yes/No).

### Dataset Management
- **View Dataset**: Opens a new window to view the generated dataset.
- **Refresh Dataset**: Refreshes the dataset, useful if metadata.csv has changed.
- **Delete Entry**: Deletes the last recorded entry from the dataset.

## Exporting Dataset as Hugging Face Audio Dataset
To export the final dataset as a Hugging Face 🤗 Datasets, use the Command-Line Interface (CLI) provided.

[Hugging Face Audio Dataset Documentation](https://huggingface.co/docs/datasets/audio_dataset)

You can log in to the UI by providing the HF token [Hugging Face Security Tokens](https://huggingface.co/docs/hub/security-tokens).

## Future Releases or On-Demand Solutions
Depending on community demand or necessity, the following features may be merged:

- Adding a new translation engine or more translation configuration options.
- Adding more metadata to the dataset, such as speaker and file type information.
- Exporting as Kaldi ☕ dataset format.
- Adding loading bars for the dataset batch translation.
- A new window to train Whisper with the new pseudo-synthetic dataset (**on-request**, contact me if you need this solution).
