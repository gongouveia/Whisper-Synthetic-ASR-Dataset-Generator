import json



def write_config_dictionary(args, gpu_avail = False):
    print("Generating speech with the following parameters:")
    configs = {'project_name': args.project ,
               'window_theme': args.theme,
                'GPU_avail': gpu_avail,
                'project_path': 'Projects/' + args.project,
                'audios_path': 'Projects/' + args.project + '/Audios',
                'text_path': 'Projects/' + args.project + '/Translations',
                'HFmodel_path': 'Projects/' + args.project + '/HFmodel',
                'metadata': 'Projects/' + args.project + '/metadata.csv',
               }
    write_dict_to_json(configs)



def write_dict_to_json(dictionary, file_path = 'config.json'):
    with open(file_path, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)



def read_parameters_from_json(json_file_path= 'config.json'):
    with open(json_file_path, 'r') as file:
        parameters = json.load(file)
    return parameters





