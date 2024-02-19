# Synthetic Speech Dataset Generator (SpeechGen)

## Overview
This application serves as a Synthetic Speech Generator, enabling users to capture audio, transcribe it, and manage the generated dataset. It provides a user-friendly interface for configuring audio parameters, transcription options, and dataset management.

## Features
- **Audio Capture**: Allows users to capture audio samples with customizable settings such as sample rate and duration.
- **Transcription**: Provides the option to transcribe captured audio into text.
- **Audio Enhancement**: Offers audio enhancement features for better quality recordings.
- **Dataset Management**: Enables users to view, delete, and manage entries in the generated dataset.
- **Export**: Allows exporting of the dataset for further processing or Hugging Face :hugs:.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your/repository.git
    ```
2. Install dependencies:
    ```bash
    pip install PyQt5 qdarktheme faster-whisper sounddevice wavio
    ```
     or, using conda:
    ```bash
     conda install --file requirements.txt
     ```

## Usage
1. Launch the application by running `python speech_gen.py --project project_name --lang <default:'en','multi'> --mode <default:'auto', 'light', 'dark'>,  `
2. Configure audio capture parameters such as sample rate in KHz `default: 16000` and duration in milliseconds `default: 5000`.
3. Choose whether to transcribe the captured audio.
4. Click on "Capture Audio" to start recording.
5. View and manage the dataset using the provided options.

## Configuration
- **Audio Sample Rate**: Set the sample rate for audio capture (in KHz).
- **Audio Duration**: Define the duration of audio samples to capture (in milliseconds).
- **Transcribe**: Choose whether to transcribe captured audio (Yes/No).
- **Audio Enhancement**: Enable or disable audio enhancement features (Yes/No).

## Dataset Management
- **View Dataset**: Opens a new window to view the generated dataset.
- **Delete Entry**: Deletes the last recorded entry from the dataset.


## Exporting Dataset as Hugging Face Audio Dataset
To export the final dataset as a Hugging Face audio dataset, use the Command-Line Interface (CLI) provided.
[https://huggingface.co/docs/datasets/audio_dataset]


## Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow the standard GitHub workflow:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


## License
This project is licensed under the [MIT License](LICENSE).

## Author
[Your Name or Organization]

For any inquiries, please contact [gongou00@gmail.com].
