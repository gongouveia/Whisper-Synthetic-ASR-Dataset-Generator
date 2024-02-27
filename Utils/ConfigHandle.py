import json



def write_config_dictionary(args):
    print("Generating speech with the following parameters:")
    print(f"Project: {args.project}")
    print(f"Language: {args.lang}")
    print(f"Mode: {args.theme}")
    if args.lang == 'en':
        model = 'medium.en'
    else: 
        model = 'medium'

    configs = {'project_name': args.project ,
               'lang': args.lang,
               'window_theme': args.theme,
               'model' : model

               }
    write_dict_to_json(configs)


def write_dict_to_json(dictionary, file_path = 'config.json'):
    with open(file_path, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)



def retrieve_config_params(file_path = 'config.json'):
    with open(file_path, 'r') as json_file:
        config_data = json.load(json_file)
    return config_data



def updateJsonFile(config_param, updated_value, file_path = 'config.json'):                            #TODO not tested yet, will update speaker name/gender/age if available
    with open(os.path.join(src, file_path), "r+") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.truncate(0)
        jsonFile.seek(0)
        data[config_param] = updated_value
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()


