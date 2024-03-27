import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import qdarktheme

from MainWindow import LedWidget, SpeechGeneratorWindow
from Utils.FileSystemManager import *
from Utils.ConfigHandle import *
import argparse

import torch


#TODO text in the beggining of the window
#check and create project



if __name__ == '__main__':


    parser = argparse.ArgumentParser(description="Generate speech with specified project, language, and mode")
    parser.add_argument('--project', type=str, required=True, help='Specify project name')
    #parser.add_argument('--lang', type=str, default='en', choices=['en', 'multi'], help="Specify language ('en' or 'multi')")
    parser.add_argument('--theme', type=str, default='light', choices=['auto', 'light', 'dark'], help="Specify theme mode ('auto', 'light', or 'dark')")
    args = parser.parse_args()

    if is_path_not_in_universe('projects/'+args.project):
        print('New Project Created.\n')
        create_new_project('project_name')
    else:
        print('Project found. Continue and Visualize Dataset.\n')
        
    print(f'GPU available: {torch.cuda.is_available()}\n')

    write_config_dictionary(args,project, is_gpu_availabel=torch.cuda.is_available())

    
    qdarktheme.enable_hi_dpi()

    app = QApplication(sys.argv)
    qdarktheme.setup_theme(args.theme)

    window = SpeechGeneratorWindow()
    window.show()
    sys.exit(app.exec_())


