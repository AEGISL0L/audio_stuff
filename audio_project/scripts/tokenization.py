# tokenization.py

from pydub import AudioSegment
from pydub.utils import make_chunks
import os
from config import TranscriptionConfig

def split_audio_into_chunks(audio: AudioSegment, chunk_length_ms=30000):
    """
    Divide el audio en segmentos de chunk_length_ms milisegundos.
    
    Args:
        audio (AudioSegment): El objeto de audio a dividir.
        chunk_length_ms (int): La longitud de cada segmento en milisegundos.
    
    Returns:
        List[AudioSegment]: Lista de segmentos de audio.
    """
    chunks = make_chunks(audio, chunk_length_ms)
    print(f"Audio dividido en {len(chunks)} segmentos de {chunk_length_ms} ms cada uno.")
    return chunks

def save_chunks_to_files(chunks, output_dir):
    """
    Guarda cada segmento de audio como un archivo .wav separado.
    
    Args:
        chunks (List[AudioSegment]): Lista de segmentos de audio.
        output_dir (str): Directorio donde se guardarán los archivos de segmentos.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, chunk in enumerate(chunks):
        chunk_name = f"chunk_{i}.wav"
        chunk_path = os.path.join(output_dir, chunk_name)
        chunk.export(chunk_path, format="wav")
        print(f"Segmento guardado como {chunk_path}")

def process_audio_file(input_audio_path, chunk_length_ms=30000):
    """
    Procesa el archivo de audio: carga, divide en segmentos y guarda los segmentos.
    
    Args:
        input_audio_path (str): La ruta al archivo de audio.
        chunk_length_ms (int): La longitud de cada segmento en milisegundos.
    """
    # Cargar el audio
    audio = AudioSegment.from_file(input_audio_path)
    
    # Dividir el audio en segmentos
    chunks = split_audio_into_chunks(audio, chunk_length_ms)
    
    # Definir el directorio de salida
    base_filename = os.path.splitext(os.path.basename(input_audio_path))[0]
    output_dir = os.path.join("data", "chunks", base_filename)
    
    # Guardar los segmentos como archivos
    save_chunks_to_files(chunks, output_dir)

# Ejemplo de uso
if __name__ == "__main__":
    config = TranscriptionConfig()
    input_audio_path = config.input_directory + "/mi_audio_importante.wav"  # Reemplaza con la ruta a tu archivo de audio
    chunk_length_ms = 30000  # Longitud de cada segmento en milisegundos (por defecto 30 segundos)
    
    # Procesar el archivo de audio
    process_audio_file(input_audio_path, chunk_length_ms)
    print("Tokenización completada y segmentos guardados.")
