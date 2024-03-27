import json



def write_config_dictionary(args, gpu_avail = False):
    print("Generating speech with the following parameters:")
    configs = {'project_name': args.project ,
               'window_theme': args.theme,
                'GPU_avail': gpu_avail,
                'project_path': 'Projects/' + args.project,
                'Audios_path': 'Projects/' + args.project + '/Audio',
                'Text_path': 'Projects/' + args.project + '/Transcription',
                'metadata': 'Projects/' + args.project + '/metadata.csv',

               }
    write_dict_to_json(configs)



def write_dict_to_json(dictionary, file_path = 'config.json'):
    with open(file_path, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)



def retrieve_config_params(file_path = 'config.json'):
    with open(file_path, 'r') as json_file:
        config_data = json.load(json_file)
    return config_data



