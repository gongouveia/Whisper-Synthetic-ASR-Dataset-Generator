Project is working. Minor bugs (under construction. 🚧👷‍♂️)

## Exsting samll bugs:

🟡 In some OS dark theme template of pyqtdarktheme is not found.


# Synthetic Speech Dataset Generator 

With the rising number of ASR/NLP open source projects democratizing the AI human-machine interface comes with the necessity of getting better ASR datasets. <Whisper Temple delves creates a simple-to-use platform to create Synthetic speech datasets, creating pairs of audio and text. Translation powered by faster-whisper ⏩ Synthetic translations can be edited in UI Data viewer. 
User interface is created using PyQt5 and runs totally on local machine.


## Overview
This application serves as a Synthetic Speech Generator, enabling users to transcribe captured audio and manage generated datasets. It provides a user-friendly interface for configuring audio parameters, transcription options, and dataset management.
![Screenshot 2024-06-16 223519](https://github.com/gongouveia/Whisper-Temple-Synthetic-ASR-Dataset-Generator/assets/68733294/24d41a0c-3592-4a0d-8c0d-61aa1aac83c1)

## Features
- **Audio Capture**: Users can capture audio samples with customizable settings such as sample rate and duration.
- **Transcription**: Provides the option to transcribe captured audio into text.
- **Audio Metadata**: Allows to add metadata to dataset, such as audio sample rate and duration.
- **Dataset Management**: Enables users to view, delete, and manage entries in the generated dataset.
- **Export**: Allows exporting of the dataset for further processing or Hugging Face :hugs:.

## Future Releases
Adding metadata to each dataset entry, audio sample rate, length, or speaker gender and age.
ReadMe update with UI screenshot and video

## Installation  (Experimenta. Not yet complete; will do Pypi and conda install)
First, I suggest you create and activate a new virtual environment using `conda` or `virtenv`. Then follow steps ⬇️
1. Clone the repository:
    ```bash
    git clone  https://github.com/gongouveia/Syntehtic-Speech-Dataset-Generator.git
    ```
2. Install dependencies in req.yml `conda env create -f req.yml`
3. Follow instruction in Usage Section.

## Usage
1. Launch the application and create or continue a project by running `python temple.py --project <default:Project> --theme <default:'auto', 'light', 'dark'>,  `
    OR Export the audio Dataset project to HuggingFace using `python export.py --project <default:Project> --language <default:'eu'>....., ` For more info. see `python export.py --help `
3. Configure audio capture parameters such as sample rate in KHz `default: 16000` and duration in milliseconds `default: 5000`.
4. If CUDA is found, it is possibel to transcribe audio records at the ed of each recording. Otherwise, yo can batch transcribe the audios in the DatasetViewer..
5. Choose whether to use VAD option in transcripion or not, default is enabled and allows for a faster trancription.
6. Click on "Capture Audio" to start a new audio recording.
7. View and manage Audio dataset using provided menu options.
8. Edit weak Transcriptions, creating a even more robust training dataset for Whisper.
# Notes
If the Idiom argument is set to ('en'), the languages dropdown menu is not available. 
If option 3 is disabled, it is possible to transcribe all the captured audios in the dataset viewer window. You can add audios to the Audio dataset by pasting them in the `/Audios` folder under your desired project.

### Configuration
- **Audio Sample Rate**: Set the sample rate for audio capture (in KHz).
- **Audio Duration**: Define the duration of audio samples to capture (in milliseconds).
- **Transcribe**: Choose whether to transcribe captured audio (Yes/No).
- **VAD**: Enable or disable VAD in transcription (Yes/No).

### Dataset Management
- **View Dataset**: Opens a new window to view the generated dataset.
- **Refresh Dataset**: Refreshes dataset, use if changed metadata.csv.
- **Delete Entry**: Deletes the last recorded entry from the dataset.


## Exporting Dataset as Hugging Face Audio Dataset
To export the final dataset as a Hugging Face 🤗 Datasets, use the Command-Line Interface (CLI) provided.
[https://huggingface.co/docs/datasets/audio_dataset]

You can log in to UI by providing the hf token [https://huggingface.co/docs/hub/security-tokens].

## Future releases or on demand solutions:
 Dependinfg on community or necessity, this features will be merged: 

  - Adding a new translation engine or more translation configuration options;
  - Adding more metadata to the Dataset, such as speaker and file type information;
  - Export as kaldi ☕ dataset format;
  - Adding a loading bars for the dataset batch translation;
  - New window to train whisper with the new pseudo-synthetic dataset (**on-request**, contact me if you need this solution).

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
