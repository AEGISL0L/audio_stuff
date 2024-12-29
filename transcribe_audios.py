import os
import speech_recognition as sr
from typing import Optional, Dict
from datetime import datetime
import json
import yaml
import logging
import concurrent.futures
from dataclasses import dataclass
from pathlib import Path
from tqdm import tqdm

@dataclass
class TranscriptionConfig:
    input_directory: Path
    output_directory: Path
    language: str = "es-ES"
    chunk_size: int = 60
    max_workers: int = 4
    min_confidence: float = 0.8
    cache_enabled: bool = True
    supported_formats: tuple = ('.wav', '.mp3', '.flac')

def load_config(config_path: str = 'config.yaml') -> TranscriptionConfig:
    """Loads configuration from YAML file"""
    if Path(config_path).exists():
        with open(config_path) as f:
            config_data = yaml.safe_load(f)
        return TranscriptionConfig(**config_data)
    return TranscriptionConfig()

class TranscriptionCache:
    """Manages caching of transcriptions"""
    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)
        
    def get(self, audio_file: Path) -> Optional[str]:
        cache_file = self.cache_dir / f"{audio_file.stem}.cache"
        if cache_file.exists():
            return cache_file.read_text(encoding='utf-8')
        return None
        
    def store(self, audio_file: Path, transcription: str) -> None:
        cache_file = self.cache_dir / f"{audio_file.stem}.cache"
        cache_file.write_text(transcription, encoding='utf-8')

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

class TranscriptionProcessor:
    """Handles the transcription processing pipeline"""
    def __init__(self, config: TranscriptionConfig):
        self.config = config
        self.cache = TranscriptionCache(Path(".transcription_cache"))
        self.stats = {'processed': 0, 'cached': 0, 'errors': 0}
        
    def process_file(self, audio_path: Path) -> None:
        if self.config.cache_enabled:
            cached = self.cache.get(audio_path)
            if cached:
                self.stats['cached'] += 1
                return cached
                
        try:
            transcription = transcribe_audio(
                str(audio_path),
                self.config.language,
                self.config.chunk_size
            )
            if transcription:
                self.cache.store(audio_path, transcription)
                self.stats['processed'] += 1
            return transcription
        except Exception as e:
            self.stats['errors'] += 1
            logging.error(f"Failed to process {audio_path}: {e}")
            return None

def transcribe_audio(audio_file_path: str, language: str = "es-ES", chunk_size: int = 60) -> Optional[str]:
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

def main():
    config = load_config()
    processor = TranscriptionProcessor(config)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=config.max_workers) as executor:
        audio_files = list(Path(config.input_directory).glob("*.[wW][aA][vV]"))
        
        with tqdm(total=len(audio_files), desc="Processing audio files") as pbar:
            futures = {
                executor.submit(processor.process_file, audio_file): audio_file
                for audio_file in audio_files
            }
            
            for future in concurrent.futures.as_completed(futures):
                pbar.update(1)
    
    logging.info(f"Processing complete. Stats: {processor.stats}")

if __name__ == "__main__":
    main()


""" Dar sentido al habla en el aula p. 61"""

""" 1. Es el maestro quien hace las preguntas y los alumnos las responden. """
""" 2. El maestro conoce las preguntas """
""" 3. La repetición de preguntas supone respuestas erróneas """

""" Visto así, el punto 1 resulta un tanto sorprendente, sobre todo teniendo en cuenta el punto 2 """
""" Sería lógico suponer que la situación consiste esencialmente en que el maestro lo sabe todo """
""" y los alumnos tienen que aprenderlo todo. """

""" Una estructura natural del discurso, en tales circunstancias, sería que los alumnos hicieran todas las preguntas """
""" y el maestro las respondiera. """

""" Dillon (1982) cita los resultados de Mishler, según los cuales, en el 85% de los intercambios observados en las clases, los
maestros hacían una pregunta más después de haber respondido los alumnos; en el 67%, contestaban la pregunta de un alumno 
haciendo otra otra pregunta. Tradicionalmente, las preguntas se han utilizado para comprobar la atención* de los alumnos y
verificar el aprendizaje rotativo."""

""" * Veáse la incidencia de TDAH en alumnos en el portal de codificación de patologías en España """

""" La enseñanza progresiva da una importancia mayor a las preguntas y las considera vitales para estimular el pensamiento
y la discusión de los alumnos. """

""" Dillon afirma que representan la técnica dominante entre los maestros para iniciar, extender y controlar la conversación 
en clase. Y sugiere que no hay en realidad, pruebas confirmadas por la investigación que demuestren que el uso de preguntas por
parte de los maestros << estimulan el pensamiento y la discusión >>.

De hecho, enfocando otros campos de la interrogación y observando el análisis teórico en sondeos de opinión y encuestas, así como 
el hecho de que se eviten por táctica las preguntas en las entrevistas personales, la psicoterapia y la discusión en grupo,

Dillon ha visto que el único campo en el que se mantiene que las preguntas
estimulan y desarrollan el pensamiento es la educación. """

""" A los entrevistadores, terapeutas, abogados y otros profesionales cuyo trabajo consiste en hacer preguntas se les suele advertir que el hacer
muchas preguntas directas a las seguidas es el modo más seguro de hacer callar al entrevistado. """

""" Los silencios, mlas afirmaciones declarativas y otras instancias menos directas son, al parecer, 
más efectivas para hacer hablar a la gente. El hecho de que prevalezcan las preguntas directas en la charla
del maestro parece en principio, contraproducente para el fin de hacer que los alumnos articulen sus pensamientos. """

""" Es muy probable que las preguntas de los maestros, y las estructuras de discurso IRF en general, sirvan a otros fines menos evidentes. """

""" Naturalmente, con las preguntas que hacen los maestros a los alumnos nos enfrentamos a un fenómeno muy
diferente del que ocurre cuando los alumnos hacen preguntas a los maestros. Mientras los alumnos pueden estar 
buscando información, guía o permiso para hacer algo, el maestro está comprobando que los alumnos saben lo que deben saber, poniendo a prueba
sus conocimeintos, comprobando si prestan atención, definiendo su agenda en cuanto a pensamiento, acción y discusión. """

""" En el sentido más directo, la mayoría de las preguntas que hacen los maestros no buscan información. Forman parte del
armamento discursivo de que disponen los maestros para controlar temas de discusión, dirigir el pensamiento y acción de los 
alumnos y establecer los límites de la atención compartida, de la actividad conjunta y del conocimiento común ( veáanse Edwards
y Furlong, 1978; Hammersley, 1977; Mehan, 1979; MacLure y French, 1980). """
