Project under construction. First release early March 2024 🚧👷‍♂️
First Release is fucntional but complete

What is missing:
- Audio capture is broken (first 0.3 seconds are corrupted, I believe that is due to pyqt and python multithread erratic behaviour),
    This issue is being adressed.
- Verification and deployment of dataset in Hugging Face
- Add in the main window led the 🔴🟠🟢🔵 cycle (idle, audio setup, audio capture and transcription if gpu is available)
- HF export not complete 
# Synthetic Speech Dataset Generator (SpeechGen)

With rising of ASR/NLP open source projects, democtratizing the AI human machine interface, come the necessity to get better and better ASR datasets. This project delves into creating a simple to use platform to create Synthetic speech datasets, creating pairs of audio and text. Translation powered by faster-whisper ⏩ Synthetic translations can be eddited in UI Data viewer . 
User interface is created using PyQt5 and runs totally on local machine.


## Overview
This application serves as a Synthetic Speech Generator, enabling users to transcribe captured audio and managing generated datasets. It provides a user-friendly interface for configuring audio parameters, transcription options, and dataset management.
![progview](https://github.com/gongouveia/Synthetic-Speech-Dataset-Generator-Powered-by-Whisper-Train-Whisper/assets/68733294/eeda9460-029b-4a9a-bfa7-176086313f11)

## Features
- **Audio Capture**: Allows users to capture audio samples with customizable settings such as sample rate and duration.
- **Transcription**: Provides the option to transcribe captured audio into text.
- **Audio Metadata**: Allows to add metadata to dataset, such as audio sample rate and duration.
- **Dataset Management**: Enables users to view, delete, and manage entries in the generated dataset.
- **Export**: Allows exporting of the dataset for further processing or Hugging Face :hugs:.

## Future Releases
Adding metadata to each dataset entry, audio sample rate, length, or speaker gender and age.
ReadMe update with UI screenshot and video

## Installation  (Experimenta. Not yet complete, will do Pypi and conda install)
I suggest that first you create and activate a new environment using `conda` or `virtenv`. Then follow steps ⬇️
1. Clone the repository:
    ```bash
    https://github.com/gongouveia/Syntehtic-Speech-Dataset-Generator.git
    ```
2. Install dependencies in requirements.txt
3. Follow instruction in Usage Section.

## Usage
1. Launch the application and create or continue a project by running `python speech_gen.py --project project_name --mode <default:'auto', 'light', 'dark'>,  `
2. Configure audio capture parameters such as sample rate in KHz `default: 16000` and duration in milliseconds `default: 5000`.
3. Choose whether to add metadata to dataset or not, e.g. samplerate and audio duration. Age, gender and name of speaker in future releases.
5. Click on "Capture Audio" to start recording.
6. View and manage Audio dataset using provided menu options.
# Notes
In the case that the Idiom argument is set to ('en') the langauges dropdown menu is not available. 
Case option 3. is disabled, it is possible to transcribe all the captured audios in the dataset viewer window. You can add audios to the Audio dataset, pasting audios in the `/Audios` uder your desired project.

### Configuration
- **Audio Sample Rate**: Set the sample rate for audio capture (in KHz).
- **Audio Duration**: Define the duration of audio samples to capture (in milliseconds).
- **Transcribe**: Choose whether to transcribe captured audio (Yes/No).
- **Audio Enhancement**: Enable or disable audio metadata in dataset (Yes/No).

### Dataset Management
- **View Dataset**: Opens a new window to view the generated dataset.
- **Delete Entry**: Deletes the last recorded entry from the dataset.


## Exporting Dataset as Hugging Face Audio Dataset
To export the final dataset as a Hugging Face 🤗 Datasets, use the Command-Line Interface (CLI) provided.
[https://huggingface.co/docs/datasets/audio_dataset]

You can login in UI providing the  hf token [https://huggingface.co/docs/hub/security-tokens].
## Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow the standard GitHub workflow:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## Author

For any inquiries or collaboration, please contact [gongou00@gmail.com].
I would be thankful to be cited in created datasets.
