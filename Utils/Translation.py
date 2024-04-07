from faster_whisper import WhisperModel

def load_translation_model(model_size = 'small.en'):
	model = WhisperModel(model_size)
	return model


def whisper_translation(model,language, audio_file):
	text = []
	result = model.transcribe(audio_file, language = language)
	segments, info = model.transcribe(audio_file, language = language)
	for segment in segments:
		text.append(segment.text)
	print('translation done')
	return ''.join(text)


def save_translation_to_txt(audio_file, text):
	text_file = audio_file.replace('.wav', '.txt') .replace('/Audio','/Translations')
	text_file = open(text_file, "w")
	text_file.write(text)
	text_file.close()



def save_dataset_csv_audio_text(metadata_file, audio_file, text):
	text_file = open(metadata_file, "a")  #name defined by hf Audio Datasets
	text_file.write(f'{audio_file},{text}\n')
	text_file.close()


