import sys
import argparse
import torch
from PyQt5.QtWidgets import QApplication
import qdarktheme

from MainWindow import SpeechGeneratorWindow
from Utils.FileSystemManager import create_new_project, is_path_not_in_universe
from Utils.ConfigHandle import write_config_dictionary


def main():
    parser = argparse.ArgumentParser(
        description="Speech Generation Application: Generate speech with specified project, language, and mode",
        epilog="Author: Gonçalo Gouveia | Lisbon, PT"
    )
    parser.add_argument(
        '--project', '-p',
        type=str,
        default='Project',
        help='Specify the name of the project'
    )
    parser.add_argument(
        '--theme', '-t',
        type=str,
        default='light',
        choices=['auto', 'light', 'dark'],
        help="Specify theme mode ('auto', 'light', or 'dark')"
    )
    
    args = parser.parse_args()
    
    print(f'GPU available: {torch.cuda.is_available()}\n')

    project_path = f'Projects/{args.project}'
    
    if is_path_not_in_universe(project_path):
        print('New Project Created.\n')
        create_new_project(args.project)
    else:
        print('Project found. Continue and Visualize Dataset.\n')

    write_config_dictionary(args, torch.cuda.is_available())

    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(args.theme)
    
    window = SpeechGeneratorWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
