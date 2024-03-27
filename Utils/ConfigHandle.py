import json


def write_dict_to_json(dictionary, file_path = 'config.json'):
    with open(file_path, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)


write_config_dictionary(args,project, is_gpu_availabel=torch.cuda.is_available())
def write_config_dictionary(args):
    print("Generating speech with the following parameters:")
    print(f"Project: {args.project}")
    print(f"Language: {args.lang}")
    print(f"Mode: {args.theme}")


    configs = {'project_name': args.project ,
               'window_theme': args.theme,
                'GPU_avail': is_gpu_availabel,
                'project_path': project
               }
    write_dict_to_json(configs)

def retrieve_config_params(file_path = 'config.json'):
    with open(file_path, 'r') as json_file:
        config_data = json.load(json_file)
    return config_data



