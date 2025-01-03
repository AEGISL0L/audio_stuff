# transcription.py

import speech_recognition as sr
import os
from pydub import AudioSegment
from config import TranscriptionConfig
from vosk import Model, KaldiRecognizer
import wave

def transcribe_audio_chunk(chunk_path: str) -> str:
    """
    Transcribe un segmento de audio usando múltiples motores de reconocimiento de voz.
    
    Args:
        chunk_path (str): La ruta al archivo del segmento de audio.
    
    Returns:
        str: El texto transcrito del segmento de audio.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
        
        # Google API
        try:
            google_text = recognizer.recognize_google(audio_data, language="es-ES")
        except sr.UnknownValueError:
            google_text = "[inaudible]"
        except sr.RequestError as e:
            google_text = f"Error: {e}"
        
        # Vosk API
        try:
            wf = wave.open(chunk_path, "rb")
            model = Model("model")
            vosk_recognizer = KaldiRecognizer(model, wf.getframerate())
            vosk_text = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if vosk_recognizer.AcceptWaveform(data):
                    vosk_text += vosk_recognizer.Result()
            wf.close()
        except Exception as e:
            vosk_text = f"Error: {e}"
        
        # Combine results
        combined_text = f"Google: {google_text}\nVosk: {vosk_text}"
        return combined_text
    except sr.UnknownValueError:
        return "[inaudible]"
    except sr.RequestError as e:
        return f"Error: {e}"

def format_transcription(text: str) -> str:
    """
    Aplica reglas de formato al texto de la transcripción con marcadores mejorados.
    
    Reglas de formato:
        - Pausas: "  " -> " / " (corta), "   " -> " // " (larga) 
        - Inaudible: "[inaudible]" -> "(...)"
        - Énfasis: "*word*" -> "«word»"
        - Solapamiento: "[overlap]" -> "⟨overlap⟩"
        - Acciones: "{action}" -> "【action】"
    
    Args:
        text (str): El texto de la transcripción a formatear.
    
    Returns:
        str: El texto de la transcripción formateado.
    """
    formatting_rules = {
        "  ": " / ",  # Pausa corta
        "   ": " // ",  # Pausa larga
        "[inaudible]": "(...)",
        "*": "«»",  # Énfasis
        "[overlap]": "⟨⟩",  # Solapamiento
        "{": "【",  # Acción inicio
        "}": "】"   # Acción fin
    }
    
    formatted_text = text
    for pattern, replacement in formatting_rules.items():
        if len(replacement) == 2:  # Manejar marcadores emparejados
            parts = formatted_text.split(pattern)
            formatted_text = replacement[0].join(parts[::2]) + \
                           replacement[1].join(parts[1::2])
        else:
            formatted_text = formatted_text.replace(pattern, replacement)
            
    return formatted_text

def transcribe_and_format_chunk(chunk_path: str) -> str:
    """
    Transcribe y aplica formato a un segmento de audio.
    
    Args:
        chunk_path (str): La ruta al archivo del segmento de audio.
    
    Returns:
        str: El texto transcrito y formateado del segmento de audio.
    """
    transcription = transcribe_audio_chunk(chunk_path)
    formatted_transcription = format_transcription(transcription)
    return formatted_transcription

def process_chunks(chunk_directory: str):
    """
    Procesa todos los segmentos de audio en un directorio: transcribe y aplica formato.
    
    Args:
        chunk_directory (str): El directorio donde se encuentran los archivos de segmentos de audio.
    
    Returns:
        dict: Un diccionario con los índices de los segmentos y sus transcripciones formateadas.
    """
    transcriptions = {}
    for filename in os.listdir(chunk_directory):
        if filename.endswith(".wav"):
            chunk_path = os.path.join(chunk_directory, filename)
            chunk_index = int(filename.split("_")[1].split(".")[0])
            formatted_transcription = transcribe_and_format_chunk(chunk_path)
            transcriptions[chunk_index] = formatted_transcription
    
    return transcriptions

# Ejemplo de uso
if __name__ == "__main__":
    config = TranscriptionConfig()
    chunk_dir = config.chunks_directory  # Reemplaza con el directorio de tus archivos de segmentos
    
    transcriptions = process_chunks(chunk_dir)
    for index, transcription in sorted(transcriptions.items()):
        print(f"--- Chunk {index} ---")
        print(transcription)
