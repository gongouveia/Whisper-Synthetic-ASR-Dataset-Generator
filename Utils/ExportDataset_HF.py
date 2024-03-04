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


# from datasets import load_dataset, load_from_disk
# from datasets import Audio

# from transformers import WhisperProcessor
# from transformers import WhisperFeatureExtractor
# from transformers import WhisperTokenizer

# dataset = load_dataset("audiofolder", data_dir="HuggingFaceDataset/")


# print(dataset["train"][0])



# dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))



# feature_extractor = WhisperFeatureExtractor.from_pretrained("openai/whisper-medium")
# tokenizer = WhisperTokenizer.from_pretrained("openai/whisper-medium", language="en", task="transcribe")




# print('Preparing dataset for hugging face with tokenizer and feature extractor\n\n')

# def prepare_dataset(batch):
#     # load and resample audio data from 48 to 16kHz
#     audio = batch["audio"]

#     # compute log-Mel input features from input audio array 
#     batch["input_features"] = feature_extractor(audio["array"], sampling_rate=audio["sampling_rate"]).input_features[0]

#     # encode target text to label ids 
#     batch["labels"] = tokenizer(batch["transcription"]).input_ids
#     return batch

# # https://huggingface.co/docs/datasets/v2.15.0/en/package_reference/main_classes#datasets.Dataset.map
# dataset = dataset.map(prepare_dataset, remove_columns=dataset.column_names["train"], num_proc=1)
# print(dataset)


# print('Dataset Structuration Complete')
# #  Number of processes when downloading and generating the dataset locally. 
# #  This is helpful if the dataset is made of multiple files. Multiprocessing is disabled by default. 
# #  If num_proc is greater than one, then all list values in gen_kwargs must be the same length. These values will be split between calls to the generator.
# #  The number of shards will be the minimum of the shortest list in gen_kwargs and num_proc.




# dataset.save_to_disk("HuggingFace_dataset_test.hf")
# print('Loading_stored_dataset')

# dataset = load_from_disk("HuggingFace_dataset_test.hf")
# print('Complete')

########################### Test



# from datasets import load_dataset, load_from_disk



# dataset = load_from_disk("HuggingFace_dataset_test.hf")


# print(dataset['train'][0])

    


