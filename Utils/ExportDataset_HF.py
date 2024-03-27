import csv
import os
import sys
from datasets import load_dataset, load_from_disk,Audio, load_dataset
from transformers import WhisperProcessor, WhisperFeatureExtractor, WhisperTokenizer



"""
This modeules handles exporting Huggingface dataset
it is incomplete, requires a ui.

For now it is exploratory, and checkif fucntions work

"""

def dataset_validator(csv_path):                                             #TODO Tested 
    try:
        with open(csv_path) as f:
            data = list(csv.reader(f))
        print("rows:", len(data))
        print("columns:", len(data[0]))
        return 1
    except:
        print('Dataframe format invalid, path does not exist')       
        return None


def create_hf_dataset(data_folder_path = "HuggingFaceDataset/",
                      dataset_name = 'hf_audio_dataset.hf',
                      sampling_rate =16000,
                      model = 'openai/whisper-medium',
                      language = 'en'):

    try:
        dataset = load_dataset("audiofolder", data_dir=data_folder_path)
        if sampling_rate != None:  #resample audio to sampling_rate value, 16khz is best for whisper
            dataset = dataset.cast_column("audio", Audio(sampling_rate=sampling_rate))
        print('here')

        feature_extractor = WhisperFeatureExtractor.from_pretrained(model)
        tokenizer = WhisperTokenizer.from_pretrained(model, language=language, task="transcribe")
        print('here')

        def prepare_dataset(batch):
            # load and resample audio data from 48 to 16kHz
            audio = batch["audio"]
    
            # compute log-Mel input features from input audio array 
            batch["input_features"] = feature_extractor(audio["array"], sampling_rate=audio["sampling_rate"]).input_features[0]
    
            # encode target text to label ids 
            batch["labels"] = tokenizer(batch["transcription"])
            return batch
        print('here')
        #REF: https://huggingface.co/docs/datasets/v2.15.0/en/package_reference/main_classes#datasets.Dataset.map
        dataset = dataset.map(prepare_dataset, remove_columns=dataset.column_names["train"], num_proc=1)
        dataset.save_to_disk(dataset_name)
        return 1
    except:
        return None

def laod_model_from_disk(hf_dataset_name):           #DEBUG purpose, TESTED
    try:
        dataset =  load_from_disk(hf_dataset_name)
        return dataset
    except:
        print('Could not load from disk, file may be non existent or reachable')
        return None


dataset = load_dataset("audiofolder", data_dir=r"C:\Users\gouve\Desktop\gradio_pr\Utils\my_dataset\data")
print(dataset['train'])

# create_hf_dataset(data_folder_path = r"Projects/Project/Audio",
#                       dataset_name = 'hf_audio_dataset.hf',
#                       sampling_rate =16000,
#                       model = 'openai/whisper-small',
#                       language = 'en')


# dataset =  load_from_disk('hf_audio_dataset.hf')
# print(dataset['train'][0])


def export_dataset_to_HF_hub(dataset, hf_token, dataset_name='new_dataset'):                             #TODO verificar  | installs dependencies if necessary and logs in HF account to export
    
    if 'huggingface_hub' not in sys.modules: 
        try:
            # os.system('pip install huggingface_hub')
            syss = os.system('pip install -U "huggingface_hub[cli]"')
            print(syss)
            return 1
        except:
            print('Could not install dependencies. Verify python version and internet connection. ')
            return None
    else:
        try:
            try:
                login = os.system(f'huggingface-cli login --token {hf_token} --add-to-git-credential')
                print(login)
            except:
                print('Action not completed')
            try:
                repo_create = os.system(f'huggingface-cli repo create {dataset_name} --type {dataset}')
                print(repo_create)
            except:
                print('Action not completed')
            try:
                upload = os.system('huggingface-cli upload')  
                print(upload)
            except:
                print('Action not completed')
        except: 
            return None





def logout():         
    try:
        res = os.system('huggingface-cli logout')
        print(res)
    except:
        pass