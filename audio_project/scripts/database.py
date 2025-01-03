# database.py

import sqlite3
from datetime import datetime

def create_database(db_path: str):
    """
    Crea una base de datos SQLite y las tablas necesarias.
    
    Args:
        db_path (str): La ruta al archivo de la base de datos.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transcriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chunk_index INTEGER,
                transcription TEXT,
                comment TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
        print(f"Base de datos creada en {db_path} con la tabla 'transcriptions'.")
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

def save_annotated_transcriptions_to_db(db_path: str, annotated_results: list):
    """
    Guarda las transcripciones anotadas en una base de datos SQLite.
    
    Args:
        db_path (str): La ruta al archivo de la base de datos.
        annotated_results (list): Una lista de diccionarios con transcripciones y comentarios.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        for result in annotated_results:
            cursor.execute('''
                INSERT INTO transcriptions (chunk_index, transcription, comment)
                VALUES (?, ?, ?)
            ''', (result["chunk_index"], result["transcription"], result["comment"]))
        
        conn.commit()
        conn.close()
        print("Transcripciones anotadas guardadas en la base de datos.")
    except Exception as e:
        print(f"Error al guardar las transcripciones en la base de datos: {e}")

def fetch_all_transcriptions(db_path: str):
    """
    Recupera todas las transcripciones anotadas de la base de datos.
    
    Args:
        db_path (str): La ruta al archivo de la base de datos.
    
    Returns:
        list: Una lista de diccionarios con las transcripciones y comentarios.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT chunk_index, transcription, comment, created_at FROM transcriptions')
        rows = cursor.fetchall()
        
        transcriptions = []
        for row in rows:
            transcriptions.append({
                "chunk_index": row[0],
                "transcription": row[1],
                "comment": row[2],
                "created_at": row[3]
            })
        
        conn.close()
        return transcriptions
    except Exception as e:
        print(f"Error al recuperar las transcripciones de la base de datos: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    db_file = "database/transcriptions_db.sqlite"  # La ruta a tu archivo de base de datos
    
    # Crear la base de datos y la tabla
    create_database(db_file)
    
    # Guardar transcripciones anotadas (ejemplo)
    annotated_results = [
        {
            "chunk_index": 0,
            "transcription": "Transcripción de ejemplo 1",
            "comment": "Comentario de ejemplo 1"
        },
        {
            "chunk_index": 1,
            "transcription": "Transcripción de ejemplo 2",
            "comment": "Comentario de ejemplo 2"
        }
    ]
    save_annotated_transcriptions_to_db(db_file, annotated_results)
    
    # Recuperar y mostrar todas las transcripciones anotadas
    transcriptions = fetch_all_transcriptions(db_file)
    for transcription in transcriptions:
        print(f"--- Chunk {transcription['chunk_index']} ---")
        print(f"Transcription: {transcription['transcription']}")
        print(f"Comment: {transcription['comment']}")
        print(f"Created At: {transcription['created_at']}\n")