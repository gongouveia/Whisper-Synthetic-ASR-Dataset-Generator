import sys
import argparse
import torch
from PyQt5.QtWidgets import QApplication
import qdarktheme

from MainWindow import SpeechGeneratorWindow
from Utils.FileSystemManager import create_new_project, is_path_not_in_universe
from Utils.ConfigHandle import write_config_dictionary, read_parameters_from_json
from Utils.ExportDataset_HF import *


def main():
    parser = argparse.ArgumentParser(
        description="Speech Generation Application: Export dataset project to a HF.",
        epilog="Author: Gonçalo Gouveia | Lisbon, PT"
    )
    parser.add_argument(
        '--project', '-p',
        type=str,
        default='Project',
        help='Specify the name of the project'
    )
    parser.add_argument(
        '--size', '-s',
        type=str,
        default='tiny',
        choices=['tiny', 'medium', 'large'],
        help="Whisper Tokenizer model size."
    )
    parser.add_argument(
        '--language', '-l',
        type=str,
        default='en',
        help="Specify main dataset language ('en','pt',...)"
    )
    parser.add_argument(
        '--sample_rate', '-sr',
        type=int,
        default=16000,
        help="Resample audio to sampling_rate value, 16khz."
    )

    args = parser.parse_args()
    print(f'GPU available: {torch.cuda.is_available()}\n')

    if is_path_not_in_universe(f'Projects/{args.project}'):
        print('Project not found\n')
    else:
        print('Project found\n')

        parameters = read_parameters_from_json('config.json')
        csv_path = parameters['metadata']
        project_folder = parameters['project_path']
        hf_folder = parameters['HFmodel_path']

        dataset_validator(csv_path)
        create_hf_dataset(
            data_folder_path=project_folder,
            dataset_name=f'{hf_folder}/hf_dataset.hf',
            sampling_rate=16000,
            model=f'openai/whisper-{args.size}',
            language=args.language
        )

        print('Audio Dataset exported to HF')


if __name__ == '__main__':
    main()
