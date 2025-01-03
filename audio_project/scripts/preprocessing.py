# preprocessing.py

from pydub import AudioSegment
from config import TranscriptionConfig

def load_audio(file_path: str) -> AudioSegment:
    """
    Carga el archivo de audio y retorna un objeto AudioSegment.
    
    Args:
        file_path (str): La ruta al archivo de audio.
    
    Returns:
        AudioSegment: El objeto de audio cargado.
    """
    try:
        audio = AudioSegment.from_file(file_path)
        print(f"Audio cargado correctamente desde {file_path}")
        return audio
    except Exception as e:
        print(f"Error al cargar el audio: {e}")
        return None

def normalize_audio(audio: AudioSegment) -> AudioSegment:
    """
    Normaliza el volumen del audio a un nivel estándar.
    
    Args:
        audio (AudioSegment): El objeto de audio a normalizar.
    
    Returns:
        AudioSegment: El objeto de audio normalizado.
    """
    normalized_audio = audio.apply_gain(-audio.max_dBFS)
    print("Audio normalizado.")
    return normalized_audio

def remove_silence(audio: AudioSegment, silence_thresh=-50.0, chunk_size=10) -> AudioSegment:
    """
    Elimina los silencios del audio.
    
    Args:
        audio (AudioSegment): El objeto de audio del cual eliminar silencios.
        silence_thresh (float): El umbral de silencio en dB.
        chunk_size (int): El tamaño del chunk en milisegundos para analizar el silencio.
    
    Returns:
        AudioSegment: El objeto de audio sin silencios.
    """
    from pydub.silence import detect_nonsilent

    non_silent_ranges = detect_nonsilent(audio, min_silence_len=chunk_size, silence_thresh=silence_thresh)
    non_silent_audio = AudioSegment.empty()
    
    for start, end in non_silent_ranges:
        non_silent_audio += audio[start:end]
    
    print("Silencios eliminados del audio.")
    return non_silent_audio

def preprocess_audio(file_path: str) -> AudioSegment:
    """
    Realiza el preprocesamiento completo del archivo de audio: carga, normaliza y elimina silencios.
    
    Args:
        file_path (str): La ruta al archivo de audio.
    
    Returns:
        AudioSegment: El objeto de audio preprocesado.
    """
    audio = load_audio(file_path)
    if audio is None:
        return None
    
    audio = normalize_audio(audio)
    audio = remove_silence(audio)
    
    return audio

# Ejemplo de uso
if __name__ == "__main__":
    config = TranscriptionConfig()
    audio_file_path = config.input_directory + "/mi_audio_importante.wav"  # Reemplaza con la ruta a tu archivo de audio
    processed_audio = preprocess_audio(audio_file_path)
    
    if processed_audio:
        # Guarda el audio preprocesado
        processed_audio.export(config.output_directory + "/mi_audio_importante_preprocessed.wav", format="wav")
        print(f"Audio preprocesado guardado como '{config.output_directory}/mi_audio_importante_preprocessed.wav'")
