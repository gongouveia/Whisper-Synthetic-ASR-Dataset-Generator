from datasets import load_dataset
import csv
import os
import sys

"""
This modeules handles exporting Huggingface dataset
it is incomplete, requires a ui.

For now it is exploratory, and checkif fucntions work

"""



def create_fh_audio_dataset(path_to_data):                                   #TODO verify | creates dataset
    dataset = load_dataset("audiofolder", data_dir=path_to_data)
    
    
def dataset_validator(csv_path):                                             #TODO verify | verifyes wetehr the dataset is good to upload 
    with open(csv_path) as f:
        data = list(csv.reader(f))
        
    print(data)    
    print("rows:", len(data))
    print("columns:", len(data[0]))


    return True


def export_dataset_to_HF_hub(dataset,dataset_name='new_dataset', hf_token):                             #TODO verificar  | installs dependencies if necessary and logs in HF account to export
    
    if 'huggingface_hub' not in sys.modules: 
        # os.system('pip install huggingface_hub')
        os.system('pip install -U "huggingface_hub[cli]"')
        print('here')
    else:
        
        login = os.system(f'huggingface-cli login --token {hf_token} --add-to-git-credential')
        print(login)
        repo_create = os.system(f'huggingface-cli repo create {dataset_name} --type dataset')
        print(repo_create)
        upload = os.system('huggingface-cli upload')
        print(upload)
                  
def logout():                                                                #TODO logsout account
    res = os.system('huggingface-cli logout')
    print(res)
    
    


