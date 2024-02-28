from datasets import load_dataset
import csv
import os
import sys

"""
This modeules handles exporting Huggingface dataset
it is incomplete, requires a ui.

For now it is exploratory, and checkif fucntions work

"""

def split_train_validation_test(train, validation, test):                     #TODO it is still very incomplete, not usre how to do valdiation
    if train + validation + test == 1:
        print('it is possible')
        
    else:
        print('split dataset in fodlers')



def create_fh_audio_dataset(path_to_data):                                   #TODO verify | creates dataset
    dataset = load_dataset("audiofolder", data_dir=path_to_data)
    
    
def dataset_validator(csv_path):                                             #TODO verify | verifyes wetehr the dataset is good to upload 
    with open(csv_path) as f:
        data = list(csv.reader(f))
        
    print(data)    
    print("rows:", len(data))
    print("columns:", len(data[0]))




def export_dataset_to_HF_hub(dataset, hf_token):                             #TODO verificar  | installs dependencies if necessary and logs in HF account to export
    
    if 'huggingface_hub' not in sys.modules: 
        # os.system('pip install huggingface_hub')
        os.system('pip install -U "huggingface_hub[cli]"')
        print('here')
    else:
        
        os.system(f'huggingface-cli login --token {hf_token} --add-to-git-credential')


def logout():                                                                #TODO logsout account
    res = os.system('huggingface-cli logout')
    print(res)
    
    


