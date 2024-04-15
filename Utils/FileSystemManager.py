
import os
import csv
import json



def is_path_not_in_universe(folder_file_path):
    	return not os.path.exists(folder_file_path)


def get_files_in_folder(folder_path, is_wav_txt ='.wav'):
    files_list = []
    if os.path.exists(folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                files_list.append(item_path.replace(is_wav_txt,''))
    else:
        print(f"The folder path '{folder_path}' does not exist.")
    
    return files_list


def create_metadata_file(file_path):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['file_name', 'transcription','sample_rate','duration_ms'])
        print(f"metadata CSV file created successfully at {file_path}")
    except Exception as e:
        print(f"Error occurred: {e}")



def create_new_project(project_name):
    path_name = f"Projects/{project_name}"
    if not os.path.isdir(path_name): 
        os.makedirs(path_name )
        os.makedirs(path_name + '/Audios/' )
        os.makedirs(path_name + '/Translations/')
        create_metadata_file(path_name +'/metadata.csv')
        return True
    return False


def delete_files_in_folder(folder_path):
    # Delete all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File {file_path} deleted successfully.")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")
