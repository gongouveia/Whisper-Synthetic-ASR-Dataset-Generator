from datasets import load_dataset
import csv
import os
import sys

from datasets import load_dataset, load_from_disk
from datasets import Audio

from transformers import WhisperProcessor
from transformers import WhisperFeatureExtractor
from transformers import WhisperTokenizer


"""
This modeules handles exporting Huggingface dataset
it is incomplete, requires a ui.

For now it is exploratory, and checkif fucntions work

"""



def create_hf_audio_dataset(path_to_data):                                   #TODO verify | creates dataset
    dataset = load_dataset("audiofolder", data_dir=path_to_data)
    return dataset


def dataset_validator(csv_path):                                             #TODO verify | verifyes wetehr the dataset is good to upload 
    with open(csv_path) as f:
        data = list(csv.reader(f))
        
    print(data)    
    print("rows:", len(data))
    print("columns:", len(data[0]))
    return True


def export_dataset_to_HF_hub(dataset, hf_token, dataset_name='new_dataset'):                             #TODO verificar  | installs dependencies if necessary and logs in HF account to export
    
    if 'huggingface_hub' not in sys.modules: 
        # os.system('pip install huggingface_hub')
        os.system('pip install -U "huggingface_hub[cli]"')
        print('here')
    else:
        
        login = os.system(f'huggingface-cli login --token {hf_token} --add-to-git-credential')
        print(login)
        repo_create = os.system(f'huggingface-cli repo create {dataset_name} --type dataset')
        print(repo_create)
        upload = os.system('huggingface-cli upload')                                                     #Verificar
        print(upload)
                  


def feature_token_extraction(whisper_model = "openai/whisper-medium", language = 'en'):
    feature_extractor = WhisperFeatureExtractor.from_pretrained(whisper_model)
    tokenizer = WhisperTokenizer.from_pretrained(whisper_model, language=language, task="transcribe")
    print('Preparing dataset for hugging face with tokenizer and feature extractor\n\n')

    return feature_extractor, tokenizer


def prepare_dataset(batch, feature_extractor, tokenizer):
    # load and resample audio data from 48 to 16kHz
    audio = batch["audio"]
    batch["input_features"] = feature_extractor(audio["array"], sampling_rate=audio["sampling_rate"]).input_features[0]
    batch["labels"] = tokenizer(batch["transcription"]).input_ids
    print('dataset_prepared')
    return batch

# # https://huggingface.co/docs/datasets/v2.15.0/en/package_reference/main_classes#datasets.Dataset.map

def prepare_and_store_dataset_to_hf(hf_dataset_name):                                                                                                             #TODO verificar o remove_collumns
    dataset = dataset.map(prepare_dataset, remove_columns=dataset.column_names["train"], num_proc=1)
    print(dataset)
    dataset.save_to_disk(hf_dataset_name)
    print('Loading_stored_dataset')
    
    return dataset


def laod_model_from_disk(hf_dataset_name):
    dataset =  load_from_disk(hf_dataset_name)
    print(dataset)
    return dataset

def logout():                                                                #TODO logsout account
    res = os.system('huggingface-cli logout')
    print(res)

    
