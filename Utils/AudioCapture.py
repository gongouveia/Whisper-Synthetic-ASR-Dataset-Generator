import threading
import sounddevice as sd
import wavio

def record_audio_thread(milliseconds, filename, samplerate=16000, channels=1):
    print("Recording audio...")
    seconds = milliseconds / 1000.0

    def _record():
        try:
            audio_data = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
            sd.wait()

            wavio.write(filename, audio_data, samplerate, sampwidth=2)

            print(f"Audio recorded successfully and saved as '{filename}'")
        except Exception as e:
            print(f"An error occurred: {e}")

    recording_thread = threading.Thread(target=_record)
    recording_thread.start()



# # record_audio_thread(1, 'projects/Project/Audios/idaidua.wav')