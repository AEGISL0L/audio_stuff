import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            # Divide el audio en fragmentos de 1 minuto
            offset = 0
            duration = 60  # duración en segundos
            transcription = ""
            while True:
                audio_data = recognizer.record(source, duration=duration, offset=offset)
                try:
                    transcription_segment = recognizer.recognize_google(audio_data, language="es-ES")
                    transcription += transcription_segment + " "
                except sr.UnknownValueError:
                    transcription += "[Inaudible] "
                except sr.RequestError as e:
                    print(f"Error al solicitar resultados; {e}")
                    break
                offset += duration
                if offset >= source.DURATION:
                    break
        return transcription
    except Exception as e:
        print(f"Error al procesar el audio: {e}")
        return None

audio_file_path = '20241122120846.WAV'
transcription = transcribe_audio(audio_file_path)
if transcription:
    print(transcription)
