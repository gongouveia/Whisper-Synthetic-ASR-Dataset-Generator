from faster_whisper import WhisperModel


import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"



def load_translation_model(model_size = 'tiny'):
	model = WhisperModel(model_size, device="auto", compute_type="float32")
	return model


def whisper_translation(model,language, audio_file):
	text = []
	if language == 'en':
		segments, info = model.transcribe(audio_file)
	else:
		segments, info = model.transcribe(audio_file, language = language)
	for segment in segments:
		text.append(segment.text)
	print('translation done')
	return ''.join(text)


def save_translation_to_txt(audio_file, text):
	text_file = audio_file.replace('.wav', '.txt') .replace('/Audios','/Translations')
	text_file = open(text_file, "w")
	text_file.write(text)
	text_file.close()



def save_dataset_csv_audio_text(metadata_file, audio_file, text, sample_rate, audio_duration_ms):
	text_file = open(metadata_file, "a")  #name defined by hf Audio Datasets
	text_file.write(f'{audio_file},{text},{sample_rate},{audio_duration_ms}\n')
	text_file.close()





