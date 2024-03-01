Project under construction. First release early March 2024 🚧👷‍♂️
What is missing:
- Audio capture is broken (perhaps is my pc audio interface)
- Transcribing in a different threads
- Verification and deployment of dataset in Hugging Face
- Change logo under /Images (It is is just a production example)
- Depending on community change argparse for Hydra  Dynamic config generation.
- Add speaker metadata
# Synthetic Speech Dataset Generator (SpeechGen)

With rising of ASR/NLP open source projects, democtratizing the AI human machine interface, come the necessity to get better and better ASR datasets. This project delves into creating a simple to use platform to create Synthetic speech datasets, creating pairs of audio and text. Translation powered by faster-whisper ⏩:. 
User interface is created using PyQt5 and runs totally on local machine.


## Overview
This application serves as a Synthetic Speech Generator, enabling users to capture audio, transcribe it, and manage the generated dataset. It provides a user-friendly interface for configuring audio parameters, transcription options, and dataset management.

## Features
- **Audio Capture**: Allows users to capture audio samples with customizable settings such as sample rate and duration.
- **Transcription**: Provides the option to transcribe captured audio into text.
- **Audio Enhancement**: Offers audio enhancement features for better quality recordings.
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
2. Install dependencies:
    ```bash
    pip install PyQt5 qdarktheme faster-whisper sounddevice wavio
    ```
     or, using conda:
    ```bash
     conda install --file requirements.txt
     ```

## Usage
1. Launch the application and create or continue a project by running `python speech_gen.py --project project_name --lang <default:'en','multi'> --mode <default:'auto', 'light', 'dark'>,  `
2. Configure audio capture parameters such as sample rate in KHz `default: 16000` and duration in milliseconds `default: 5000`.
3. Choose whether to transcribe audio as it capture is complete.
4. Click on "Capture Audio" to start recording.
5. View and manage the dataset using the provided options.
# Notes
In the case that the Idiom argument is set to ('en') the langauges dropdown menu is not available. 
Case option 3. is disabled, it is possible to transcribe all the captured audios in the dataset viewer window. You can add audios to the Audio dataset, pasting audios in the `/Audios` uder your desired project.

### Configuration
- **Audio Sample Rate**: Set the sample rate for audio capture (in KHz).
- **Audio Duration**: Define the duration of audio samples to capture (in milliseconds).
- **Transcribe**: Choose whether to transcribe captured audio (Yes/No).
- **Audio Enhancement**: Enable or disable audio enhancement features (Yes/No).

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


## License
This project is licensed under the [MIT License](LICENSE).

## Author

For any inquiries or collaboration, please contact [gongou00@gmail.com].
