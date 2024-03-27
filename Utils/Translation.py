from faster_whisper import WhisperModel

def load_translation_model(model_size):         # Load model, it loads to CUDA if available as default
	try:
		model = WhisperModel(model_size)
		return model
	except:
		return None

def whisper_translation(model,language, audio_file, vad_filter = True):           #Trancribes the audio file using faster whisper
	text = []
	result = model.transcribe(audio_file, language = language)
	segments, info = model.transcribe(audio_file, language = language, vad_filter=vad_filter)
	for segment in segments:
		text.append(segment.text)
	print('translation done')
	text = ''.join(text)
	return text

def save_dataset_csv_audio_text(audio_file, text):                              #saves the audio path and its text to the metadata.csv file. Optimal to export audio dataset   
	try:
		text_file = open('projects/Project/metadata.csv', "a")  #name defined by hf Audio Datasets
		text_file.write(f'{audio_file},{text}\n')
		text_file.close()
		return 1
	except:
		return None

def save_translation_to_txt(audio_file, text):                                  #save the audio translation in a txt file with the same name as the audio file (This fucntion will deprecate soon)
	try:
		text_file = audio_file.replace('.wav', '.txt') .replace('/Audios','/Translations')
		text_file = open(text_file, "w")
		text_file.write(text)
		text_file.close()
		return 1
	except:
		return None

#def save_dataset_csv_audio(audio_file):
#	text_file = open('projects/Project/metadata.csv', "a")  #name defined by hf Audio Datasets
#	text_file.write(f'{audio_file}\n')
#	text_file.close()



