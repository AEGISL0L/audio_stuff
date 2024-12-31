import speech_recognition as sr
from typing import Optional
from utils import format_transcription, save_metadata

def transcribe_audio(audio_file_path: str, language: str = "es-ES", chunk_size: int = 60) -> Optional[str]:
    """Transcribes audio using the SpeechRecognition library (Google API by default).

    Splits audio into segments defined by 'chunk_size', processes each one, and
    accumulates recognized text. Implements basic error handling for unknown speech.

    Args:
        audio_file_path (str): Path to the audio file.
        language (str): Language code for recognition.
        chunk_size (int): Number of seconds to process in each chunk.

    Returns:
        Optional[str]: The fully combined and formatted transcription, or None on error.
    """
    recognizer = sr.Recognizer()
    stats = {'duration': 0, 'segments': 0}
    
    try:
        with sr.AudioFile(audio_file_path) as source:
            transcription = []
            offset = 0
            stats['duration'] = source.DURATION
            
            while offset < source.DURATION:
                try:
                    audio_data = recognizer.record(source, duration=chunk_size)
                    segment = recognizer.recognize_google(audio_data, language=language)
                    transcription.append(segment)
                    stats['segments'] += 1
                except sr.UnknownValueError:
                    transcription.append("(...)")
                    stats['segments'] += 1
                except sr.RequestError as e:
                    print(f"Error al solicitar resultados; {e}")
                    break
                offset += chunk_size
                
            full_transcription = " ".join(transcription)
            formatted_transcription = format_transcription(full_transcription)
            
            save_metadata(audio_file_path, stats)
            
            return formatted_transcription
    except Exception as e:
        print(f"Error al procesar el audio {audio_file_path}: {e}")
        return None
