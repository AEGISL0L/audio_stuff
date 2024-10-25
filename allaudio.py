import os
import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            transcription = ""
            offset = 0
            while offset < source.DURATION:
                try:
                    audio_data = recognizer.record(source, duration=60)
                    transcription_segment = recognizer.recognize_google(audio_data, language="es-ES")
                    transcription += transcription_segment + " "
                except sr.UnknownValueError:
                    transcription += "[Inaudible] "
                except sr.RequestError as e:
                    print(f"Error al solicitar resultados; {e}")
                    break
                offset += 60
        return transcription
    except Exception as e:
        print(f"Error al procesar el audio {audio_file_path}: {e}")
        return None

def transcribe_audios_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".wav"):
            audio_file_path = os.path.join(directory_path, filename)
            print(f"Procesando archivo: {audio_file_path}")  # Debugging line
            transcription = transcribe_audio(audio_file_path)

            if transcription:
                output_file_path = os.path.splitext(audio_file_path)[0] + '.txt'
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(transcription)
                print(f"Transcripción de {filename} completada y guardada en {output_file_path}.")

# Configuración
directory_path = '/run/media/juav/VOICE/RECORD'  # Reemplaza con la ruta al directorio que contiene los archivos de audio

transcribe_audios_in_directory(directory_path)
