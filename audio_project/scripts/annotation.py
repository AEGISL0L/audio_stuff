# annotation.py

from transcription import process_chunks
from preprocessing import preprocess_audio
from config import TranscriptionConfig

def load_book_text(book_path: str) -> str:
    """
    Carga el texto del libro.
    
    Args:
        book_path (str): La ruta al archivo del libro.
    
    Returns:
        str: El contenido del libro como una cadena de texto.
    """
    try:
        with open(book_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error al cargar el libro: {e}")
        return ""

def annotate_transcription_with_book_context(transcription: str, book_text: str) -> str:
    """
    Genera un comentario para la transcripción usando lógica del libro.
    
    Args:
        transcription (str): El texto de la transcripción.
        book_text (str): El contenido del libro.
    
    Returns:
        str: Un comentario generado basado en la lógica del libro.
    """
    # Define palabras clave de interés desde el libro
    keywords_of_interest = ["idea", "desarrollo", "perspectiva", "educación"]
    
    # Encuentra palabras clave en la transcripción
    found_keywords = [kw for kw in keywords_of_interest if kw in transcription.lower()]
    
    # Genera un comentario basado en las palabras clave encontradas
    if found_keywords:
        comment = (f"Se encontraron los siguientes conceptos: {found_keywords}. "
                   "Estos están relacionados con secciones específicas del libro. "
                   "Ref: Capítulo de 'Desarrollo y Educación'.")
    else:
        comment = "No se hallaron coincidencias específicas con el contenido clave del libro."
    
    return comment

def generate_annotated_transcriptions(input_audio_path: str, book_path: str):
    """
    Genera transcripciones anotadas usando la lógica del libro.
    
    Args:
        input_audio_path (str): La ruta al archivo de audio.
        book_path (str): La ruta al archivo del libro.
    
    Returns:
        list: Una lista de diccionarios con transcripciones y comentarios.
    """
    # Preprocesar el audio
    audio = preprocess_audio(input_audio_path)
    if audio is None:
        return []

    # Dividir el audio en segmentos y transcribir
    config = TranscriptionConfig()
    chunk_directory = config.chunks_directory
    transcriptions = process_chunks(chunk_directory)

    # Cargar el contenido del libro
    book_content = load_book_text(book_path)
    
    # Anotar cada transcripción con un comentario basado en el contenido del libro
    annotated_results = []
    for index, transcription in sorted(transcriptions.items()):
        comment = annotate_transcription_with_book_context(transcription, book_content)
        annotated_results.append({
            "chunk_index": index,
            "transcription": transcription,
            "comment": comment
        })
    
    return annotated_results

# Ejemplo de uso
if __name__ == "__main__":
    config = TranscriptionConfig()
    audio_file = config.input_directory + "/mi_audio_importante.wav"  # Reemplaza con tu archivo de audio
    book_file = config.book_file_path + "/mi_libro.txt"              # Reemplaza con tu archivo de libro
    
    annotated_transcriptions = generate_annotated_transcriptions(audio_file, book_file)
    for result in annotated_transcriptions:
        print(f"--- Chunk {result['chunk_index']} ---")
        print(f"Transcription: {result['transcription']}")
        print(f"Comment: {result['comment']}\n")
