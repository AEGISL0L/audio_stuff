# main.py

import os
from preprocessing import preprocess_audio
from tokenization import split_audio_into_chunks, save_chunks_to_files
from transcription import process_chunks
from annotation import generate_annotated_transcriptions
from database import create_database, save_annotated_transcriptions_to_db
from config import TranscriptionConfig

# Configuración de rutas
config = TranscriptionConfig()
AUDIO_FILE_PATH = config.input_directory
BOOK_FILE_PATH = config.book_file_path
CHUNKS_DIR = config.chunks_directory
DB_FILE_PATH = config.db_file_path

def main():
    # Paso 1: Preprocesar el audio
    print("Preprocesando el archivo de audio...")
    audio = preprocess_audio(AUDIO_FILE_PATH)
    if audio is None:
        print("Error: No se pudo cargar el audio.")
        return
    
    # Paso 2: Dividir el audio en segmentos
    print("Dividiendo el audio en segmentos...")
    chunks = split_audio_into_chunks(audio, chunk_length_ms=30000)
    save_chunks_to_files(chunks, CHUNKS_DIR)
    
    # Paso 3: Procesar los segmentos para transcribir y formatear
    print("Procesando los segmentos para transcribir y formatear...")
    transcriptions = process_chunks(CHUNKS_DIR)
    
    # Paso 4: Generar transcripciones anotadas usando el libro
    print("Generando transcripciones anotadas usando el libro...")
    annotated_transcriptions = generate_annotated_transcriptions(AUDIO_FILE_PATH, BOOK_FILE_PATH)
    
    # Paso 5: Crear la base de datos y guardar las transcripciones anotadas
    print("Creando la base de datos y guardando las transcripciones anotadas...")
    create_database(DB_FILE_PATH)
    save_annotated_transcriptions_to_db(DB_FILE_PATH, annotated_transcriptions)
    
    print("Proceso completado. Las transcripciones anotadas han sido guardadas en la base de datos.")

if __name__ == "__main__":
    main()
