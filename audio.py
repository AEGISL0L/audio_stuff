import os
from pydub import AudioSegment
from pydub.utils import make_chunks
import speech_recognition as sr

def split_audio_into_chunks(input_audio_path, chunk_length_ms=30000):
    """
    Splits an audio file into chunks of 'chunk_length_ms' milliseconds using pydub.
    Returns a list of file paths for the split audio segments.
    """
    audio = AudioSegment.from_file(input_audio_path)
    chunks = make_chunks(audio, chunk_length_ms)
    
    chunk_paths = []
    base_filename = os.path.splitext(os.path.basename(input_audio_path))[0]
    
    # Create an output directory for the chunks
    output_dir = f"{base_filename}_chunks"
    os.makedirs(output_dir, exist_ok=True)
    
    for i, chunk in enumerate(chunks):
        chunk_name = f"chunk_{i}.wav"
        chunk_path = os.path.join(output_dir, chunk_name)
        chunk.export(chunk_path, format="wav")
        chunk_paths.append(chunk_path)
    
    return chunk_paths

def transcribe_audio_chunk(chunk_path):
    """
    Transcribes a single audio chunk using SpeechRecognition and returns the transcribed text.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(chunk_path) as source:
        audio_data = recognizer.record(source)
    try:
        # Adjust language to match your audio's language (e.g., "en-US", "es-ES", etc.)
        text = recognizer.recognize_google(audio_data, language="es-ES")
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"Error transcribiendo chunk: {str(e)}"

def process_audio_in_chunks(input_audio_path):
    """
    Splits the audio into chunks and transcribes each chunk.
    Returns a list of transcriptions (strings).
    """
    chunk_paths = split_audio_into_chunks(input_audio_path)
    transcription_list = []
    for chunk_path in chunk_paths:
        text = transcribe_audio_chunk(chunk_path)
        transcription_list.append(text)
    return transcription_list

def load_book_text(book_path):
    """
    Loads the entire text of a book. In practice, you’d likely parse 
    chapters or sections for more fine-grained analysis.
    """
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

def annotate_transcription_with_book_context(transcription, book_text):
    """
    Generates a 'comment' or observation for each transcribed chunk, 
    possibly using logic from the book (e.g., searching for related keywords).

    This example simply checks if certain keywords appear in the transcription 
    and references the book. In a real scenario, you might perform more 
    advanced NLP tasks.
    """
    # Example: define some keywords from the book (or load them from a config):
    keywords_of_interest = ["idea", "desarrollo", "perspectiva", "educación"]
    
    # Check if any keywords match, build a comment:
    found_keywords = [kw for kw in keywords_of_interest if kw in transcription.lower()]
    
    if found_keywords:
        comment = (f"Se encontraron los siguientes conceptos: {found_keywords}. "
                   "Estos están relacionados con secciones específicas del libro. "
                   "Ref: Capítulo de 'Desarrollo y Educación'.")
    else:
        comment = "No se hallaron coincidencias específicas con el contenido clave del libro."
    
    return comment

def generate_annotated_transcriptions(input_audio_path, book_path):
    """
    Puts everything together: 
    1. Split and transcribe the audio.
    2. Load the book text.
    3. For each chunk’s transcription, attach a comment/annotation referencing the book.
    """
    # Transcribe audio chunks
    transcriptions = process_audio_in_chunks(input_audio_path)
    
    # Load the book text (could be used for more robust NLP in practice)
    book_content = load_book_text(book_path)
    
    # Pair each transcription with an annotation
    annotated_results = []
    for i, chunk_text in enumerate(transcriptions):
        comment = annotate_transcription_with_book_context(chunk_text, book_content)
        annotated_results.append({
            "chunk_index": i,
            "transcription": chunk_text,
            "comment": comment
        })
    
    return annotated_results

"""
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
"""