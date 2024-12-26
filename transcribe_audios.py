import os
import speech_recognition as sr
from typing import Optional, Dict
from datetime import datetime
import json

def format_transcription(text: str) -> str:
    """Applies transcription formatting conventions"""
    formatting_rules = {
        "  ": " / ",  # Short pauses
        "   ": " // ",  # Long pauses
        "[inaudible]": "(...)",  # Unclear speech
        "...": "...",  # Incomplete speech
        "[": "[",  # Simultaneous speech start
        "]": "]"  # Simultaneous speech end
    }
    
    formatted_text = text
    for pattern, replacement in formatting_rules.items():
        formatted_text = formatted_text.replace(pattern, replacement)
    return formatted_text

def save_metadata(audio_file_path: str, transcription_stats: Dict) -> None:
    """Saves transcription metadata to a JSON file"""
    metadata = {
        'original_file': os.path.basename(audio_file_path),
        'transcription_date': datetime.now().isoformat(),
        'duration_seconds': transcription_stats['duration'],
        'segments_count': transcription_stats['segments'],
        'language': 'es-ES'
    }
    
    metadata_path = f"{os.path.splitext(audio_file_path)[0]}_metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

def transcribe_audio(audio_file_path: str) -> Optional[str]:
    recognizer = sr.Recognizer()
    stats = {'duration': 0, 'segments': 0}
    
    try:
        with sr.AudioFile(audio_file_path) as source:
            transcription = []
            offset = 0
            stats['duration'] = source.DURATION
            
            while offset < source.DURATION:
                try:
                    audio_data = recognizer.record(source, duration=60)
                    segment = recognizer.recognize_google(audio_data, language="es-ES")
                    transcription.append(segment)
                    stats['segments'] += 1
                except sr.UnknownValueError:
                    transcription.append("(...)")
                    stats['segments'] += 1
                except sr.RequestError as e:
                    print(f"Error al solicitar resultados; {e}")
                    break
                offset += 60
                
        full_transcription = " ".join(transcription)
        formatted_transcription = format_transcription(full_transcription)
        
        # Save metadata after successful transcription
        save_metadata(audio_file_path, stats)
        
        return formatted_transcription
    except Exception as e:
        print(f"Error al procesar el audio {audio_file_path}: {e}")
        return None

def transcribe_audios_in_directory(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        print(f"El directorio {directory_path} no existe")
        return

    wav_files = [f for f in os.listdir(directory_path) if f.endswith(".wav")]
    
    if not wav_files:
        print("No se encontraron archivos WAV para procesar")
        return
    
    total_files = len(wav_files)
    processed_files = 0
    
    print(f"Iniciando procesamiento de {total_files} archivos...")
    
    for filename in wav_files:
        audio_file_path = os.path.join(directory_path, filename)
        processed_files += 1
        print(f"Procesando archivo {processed_files}/{total_files}: {filename}")
        
        transcription = transcribe_audio(audio_file_path)
        if transcription:
            output_file_path = os.path.splitext(audio_file_path)[0] + '.txt'
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(transcription)
            print(f"✓ Transcripción guardada en: {output_file_path}")
    
    print(f"\nProceso completado. {processed_files} archivos procesados.")

if __name__ == "__main__":
    directory_path = '/run/media/juav/VOICE/RECORD'
    transcribe_audios_in_directory(directory_path)
