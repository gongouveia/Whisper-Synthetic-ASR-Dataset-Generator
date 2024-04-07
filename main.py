import sys
from PyQt5.QtWidgets import QApplication
import qdarktheme

from MainWindow import LedWidget, SpeechGeneratorWindow
from Utils.FileSystemManager import *
from Utils.ConfigHandle import write_config_dictionary
import argparse

import torch



if __name__ == '__main__':


    parser = argparse.ArgumentParser(description="Generate speech with specified project, language, and mode")
    parser.add_argument('--project', type=str, required=True, help='Specify project name')
    parser.add_argument('--theme', type=str, default='light', choices=['auto', 'light', 'dark'], help="Specify theme mode ('auto', 'light', or 'dark')")
    args = parser.parse_args()



    if is_path_not_in_universe('Projects/'+args.project):
        print('New Project Created.\n')
        create_new_project(args.project)
    else:
        print('Project found. Continue and Visualize Dataset.\n')
        
    print(f'GPU available: {torch.cuda.is_available()}\n')
    print('here')

    write_config_dictionary(args, torch.cuda.is_available())
    
    qdarktheme.enable_hi_dpi()

    app = QApplication(sys.argv)
    qdarktheme.setup_theme(args.theme)

    window = SpeechGeneratorWindow()
    window.show()
    sys.exit(app.exec_())

