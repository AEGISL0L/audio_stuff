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

""" Como sea que la mayoría de las preguntas del maestro son preguntas cuyo conocimiento en la respuesta por parte del maestro suponen todos,
el status de cualquier resupuesta que dé un alumno se ve también afectado por el carácter del intercambio.
Se entiende que el maestro está en situación de evaluar cualquier respuesta de este tipo (la parte de feedback del IRF) por lo que
el siguiente movimiento del maestro se considerará como evaluativo. De modo que, si lo que hace el maestro es plantear de nuevo 
la misma pregunta, ello implica que, sea cual sea la respuesta recibida, se ha considerado incorrecta y puede implicar lo mismo;
la pregunta anterior sigue << sobre la mesa >>. Si el maestro hecha por el alumno, el lógica la interpretación opuesta: la pregunta
no consta en la agenda. Dicho de otro modo, el maestro está en situación de controlar el discurso, de definir de qué cosas hay que hablar,
y puede actuar como árbrito de la validez de los conocimientos. """

""" Saltamos al capitulo 7 desde página 62; resumen:

Tradicionalmente, en el aula el maestro hace las preguntas y los alumnos responden. Esto parece contradictorio, ya que el maestro supuestamente lo sabe todo y los alumnos deben aprender.
Según estudios citados, en la mayoría de los intercambios en clase, los maestros hacen más preguntas después de que los alumnos respondan, o responden a las preguntas de los alumnos con otras preguntas. Esto sugiere que las preguntas se usan más para comprobar la atención y el aprendizaje de los alumnos, que para estimular el pensamiento y la discusión.
Otros campos como entrevistas, terapia y discusiones de grupo evitan hacer muchas preguntas directas, ya que se considera que inhiben la expresión de las personas. Sin embargo, en educación se mantiene la creencia de que las preguntas estimulan el pensamiento.
Las preguntas de los maestros parecen servir más para controlar los temas de discusión, dirigir el pensamiento y acción de los alumnos, y establecer los límites de lo que se considera conocimiento compartido, que para obtener información.
Cuando el maestro hace una pregunta cuya respuesta se supone que él conoce, la respuesta del alumno queda sujeta a la evaluación del maestro, lo que afecta el status de dicha respuesta.
"""


def process_classroom_tasks(transcription: str) -> Dict:
    """Analyzes classroom discourse patterns in transcriptions"""
    tasks = {
        'teacher_questions': 0,
        'student_responses': 0, 
        'follow_up_questions': 0,
        'student_initiated_questions': 0
    }
    
    # Split transcription into dialogue segments
    segments = transcription.split(" / ")
    
    for segment in segments:
        if "?" in segment:
            if "[teacher]" in segment.lower():
                tasks['teacher_questions'] += 1
            elif "[student]" in segment.lower():
                tasks['student_initiated_questions'] += 1
        
        if "[student]" in segment.lower() and not "?" in segment:
            tasks['student_responses'] += 1
            
        if "[teacher]" in segment.lower() and "?" in segment and tasks['student_responses'] > 0:
            tasks['follow_up_questions'] += 1
            
    return tasks

def generate_discourse_report(tasks: Dict) -> str:
    """Generates a report analyzing classroom interaction patterns"""
    report = [
        "Classroom Discourse Analysis",
        "-" * 30,
        f"Teacher Questions: {tasks['teacher_questions']}", 
        f"Student Responses: {tasks['student_responses']}",
        f"Follow-up Questions: {tasks['follow_up_questions']}",
        f"Student-Initiated Questions: {tasks['student_initiated_questions']}",
        f"Question-Response Ratio: {tasks['teacher_questions']/max(tasks['student_responses'], 1):.2f}"
    ]
    return "\n".join(report)


""" 7. COMUNICACIÓN Y CONTROL """

""" En el capítulo anterior (6) observávamos algunos de los modos en que las comprensiones
rituales o de procedimiento, más que la de principios, pueden verse
fomentadas por ciertos tipos de comunicación en clase. Nuestro examen
de estas comunicaciones estaba organizado teniendo en cuenta los principios
de experimentación científica que se barajaban en las lecciones
más que los procesos de comunicación identificables. Vamos a examinar
ahora el mismo tipo de fenómenos, pero esta vez nos centraremos en los tipos de comunicaciones
involucradas. Estudiaremos como ciertos tipos de comunicación pueden 
fomentar u obstaculizas el desarrollo del conocimiento compartido en clase.
Aunque nuestro foco de atención pasa del contenido del conocimiento a los
procesos del pensamiento, por lo que dicen y hablan las personas más
que por su capacidad para la discusión racional. Del mismo modo, no nos 
ocupamos de los esquemas de comunicación o estructuras de discurso en sí 
mismas: del abanico y los tipos de señales no verbales, por ejemplo, o de la estructuración
de los IRF en el habla en el aula (que ya hemos mencionado en el capítulo 2).

Nuestro objetivo principal es el modo en que maestros y alumnos establecen comprensiones
compartidas del contenido del currículum, por lo que nuestro examen de diversos tipos de comunicación
en clase está orientado hacia el modo en que se expresan la información, los argumentos, las ideas
o los análisis.

Así, cuando hablábamos en el capítulo 6 de algunas contradicciones espontáneas ofrecidas por 
los alumnos, se trataba de ocasiones en que los alumnos ofrecían sus propias ideas o explicaciones
más que simplemente de ocasiones en que los alumnos ofrecín sus propias ideas o explicaciones más que simplemente
de ocasiones en que los alumnos se tomaban un turno de habla sin haber sido invitados a ello.

La misma preocupación por el contenido del conocimiento compartido limitará lo que vamos a investigar aquí.

"""

"""
Nuestra exposición en el capítulo 4 de las reglas básicas de la comprensión conjunta apuntaban a la importancia de la forma
y el contenido del discurso hablado y escrito, al señalas las ocasiones adecuadas para que tuviesen lugar cierto tipo de
comprensiones. Las reglas básicas de la práctica en la enseñanza y de la comprensión mutua se apoyan generalmente 
en la capacidad de los participantes para reconocer que algunos tipos de comunicación - el uso de ciertas palabras o 
tipos de preguntas en contextos reconocidos - indican la adecuación de unas estrategias cognitivas concretas relacionadas entre sí.

El reconocimiento de preguntas desvinculadas, problemas matemáticos pseudonarrativos, preguntas a prueba incluidas en la secuencia
IRF, etc., depende principalmente de lo familiarizado que se esté con el modo en que funciona el discurso educacional en cuanto
a encarnar, cuestionar y probable conocimiento educacional. 

"""

class CommunicationAnalyzer:
    def __init__(self):
        self.patterns = {
            'knowledge_sharing': [],
            'control_mechanisms': [],
            'student_initiatives': [],
            'teacher_responses': []
        }
        self.metrics = {
            'knowledge_exchanges': 0,
            'control_instances': 0,
            'student_contributions': 0,
            'shared_understanding_markers': 0
        }
    
    def analyze_discourse(self, transcription: str) -> Dict:
        segments = transcription.split('\n')
        
        for segment in segments:
            if '[teacher]' in segment.lower():
                if '?' in segment:
                    self.metrics['control_instances'] += 1
                if any(term in segment.lower() for term in ['explain', 'understand', 'mean']):
                    self.metrics['knowledge_exchanges'] += 1
                    
            if '[student]' in segment.lower():
                self.metrics['student_contributions'] += 1
                if any(term in segment.lower() for term in ['i think', 'because', 'therefore']):
                    self.metrics['shared_understanding_markers'] += 1
                    
            self.patterns['knowledge_sharing'].append(segment)
            
        return self.metrics
    
    def generate_communication_report(self, metrics: Dict) -> str:
        report_sections = [
            "Classroom Communication Analysis",
            "=" * 30,
            f"Knowledge Exchange Events: {metrics['knowledge_exchanges']}",
            f"Control Mechanisms Used: {metrics['control_instances']}",
            f"Student Contributions: {metrics['student_contributions']}",
            f"Shared Understanding Indicators: {metrics['shared_understanding_markers']}",
            "-" * 30,
            "Pattern Analysis:",
            f"Knowledge Exchange Ratio: {metrics['knowledge_exchanges']/max(metrics['control_instances'], 1):.2f}",
            f"Student Engagement Level: {metrics['student_contributions']/max(len(self.patterns['knowledge_sharing']), 1):.2f}"
        ]
        
        return "\n".join(report_sections)

""" Como sea que nuestros datos son básicamente transcripciones del diálogo en clase, inevitablemente estaremos buscando
estos procesos en la comunicación hablada dentro de la clase. Nuestro objetivo en este capítulo es examinar cómo tipos
concretos de discurso en clase transmiten un conocimiento educacional.
"""

"""
Nuestra primera impresión de las lecciones era que se trataba de tipos de pedagogía relativamente informal, progresiva y
centrada y centrada en el alumno, como el que defiende el informe Plowden (veáse capítulo 3).
Como consecuencia imprevista de un examen más de cerca de los datos, nos ocupamos aquí en gran medida de los procesos
de control, es decir, de los modos en que la maestra mantenía una definición estricta de lo que llegaban a ser versiones conjuntas de acontecimientos
y comprensiones conjuntas del contenido del currículum.
"""

"""
Como hemos visto, el proceso problemático. Resulta que hay una serie de propiedades y limitaciónes bajo las cuales funciona el proceso
de enseñanza, que no siempre son armónicas y que hacen que el proceso sea problemático. Entre éstas están:

1. el supuesto por parte del maestro de que el fracaso educacional en el caso de individuos concretos puede atribuirse a factores
individuales, y principalmente a la capacidad innata;

2. un modo de ver la educación que supone la existencia de un proceso de aprendizaje inductivo, basado en la experiencia a través de la 
actividad práctica y que se actualiza por sí mismo;

3. la función socializadora de la educación, en la que el maestro ejerce una gran medida de control sobre lo que se hace, dice y comprende;

4. la separación de la educación formal de los contextos de la experiencia y del aprendizajje cotidianos extraescolares;

5. la base, en gran medida implícita, de gran perte de la actividad y del discurso en clase.
"""

"""
Las nociones de <<andamiaje>> (Bruner) y de <<zona de desarrollo próximo>>
(Vygotsky) resultan apropiadas para la descripción de la educación en clase,
pero se ven a menudo comprometidas por el carácter un tanto inconsciente de las 
propiedades mencionadas. Aunque los maestrods llevan a cabo una gran cantidad
de enseñanza especializada, instando y ayudando a los alumnos a desarrollar su comprensión
de los temas de estudio, sus propias concepciones de lo que hacen pueden estar reñidas
con este proceso. El éxito y el fracaso se conciben en gran medida en términos
de las propiedades inherentes de los alumnos más que como un resultado del proceso
comunicativo de la educación en sí, y de las comprensiones por parte de los alumnos
se consideran esencialmente como en sus propias experiencias.

El hecho de que haya que enseñar un programa de estudios concreto, o al meno, que haya
que cubrir una serie planificada de los conceptios y actividades, lleva al tipo del
<< dilema del maestro >> del que  hablábamos al término del capítulo anterior: 
cómo hacer que los alumnos aprendan por sí mismos lo que se ha planificado por 
anticipado para ellos.

Mantenemos que estos dilemas y compromisos pueden tener un efecto destructivo sobra la
efectividad de la educación ya que dan al traste con el objetivo esencial del proceso
vygotskyano: es decir, el proceso queda a menudo incompleto, sin un traspaso final 
de conocimiento y control de los alumnos.

Los alumnos se ven con frecuencia inmersos en rituales y procedimientos sin haber
captado el objetivo general de lo que han hecho, inlcuidos los principios y conceptos
generales que las actividades de una lección en particular estaban destinadas a inculcarles.

Al buscar la manera de organizar nuestra forma de tratar estos procesos de comunicación
hemos escogido lo que representan el eje del habla en el aula, la medida de control por parte del maestro
sobre el discurso y, a través de éste, sobre el contenido del conocimiento.
La siguiente list de comunicaciones en clase se ofrece como una escala del control dle maestro
sobre el carácter, contenido y codificación del conocimiento, en la que la medida de control
aumenta según vamos bajando en el orden de la lista.

No es una lista exhaustiva, y el carácter cualitativo de su contenido excluye toda noción 
precisa de jerarquía u orden. Es, sin embargo útil en la medida en que nos ayuda a en el 
establecimiento de comprensiones compartidas. Mantenemos que se debe esencialmente a los 
profundos fenómenos de control del maestro sobre la expresión del conocimiento el que la comprensión
de las cosas por parte de los alumnos sea con frecuencia de procedimiento más que de principios:
decir y hacer lo que parece preciso en lugar de elaborar una comprensión de principios de cómo
y por qué son apropiadas o correctas ciertas acciones, expresiones o procedimientos.
La siguiente lista de aspectos del discurso en clase está hecha teniendo en cuenta el rol del maestro en los mismos.

Obtención de contribuciones de los alumnos. 
Indicadores de la importancia, por ejemplo, enunciación especial, frases tipo fórmulas, omisión de las contribuciones de los alumnos.
Indicadores de conocimiento conjunto, por ejemplo, habla simultánea, plurales <<superiores>>, formas repetidas de discurso.
Obtención de contribuciones de los alumnos mediante claves.
Interpretaciones parafrásicas de contribuciones de los alumnos.
Recapitulaciones iterativas.
Conocimiento implícito y conocimiento presupuesto.

Las siguientes secciones de este capítulo tratarán de cada uno de estos fenómenos, 
aproximadamente en el orden que se ha dado. Se han omitido de la lista las contribuciones de los alumnos
<<no sonsacadas>>  (de las que hablaremos más adelante en el contexto de las sonsacadas) y la enseñanza
directa a modo de lectura por parte de los maestros, en la que se pedía a los alumnos ( o éstos ofrecían)
poca contribución. En las lecciones sobre el péndulo, este tipo de enseñanza era mínima.

El discurso estaba en su mayor parte baasado en diálogos de tipo IRF, y la enseñanza directa se limitaba
a explicaciones o definiciones ocasionales e palabras (<< esto se le llama esfera>>, lavantándola para que la vean los alumnos)
o la narración de historias relevantes en cuanto a la lección (observaciones de Galileo sobre el balanceo de los incensarios de las iglesia, y el motín de Mary Rose).

Aunque estos tipos de enseñanza son interesantes en sí mismos, y, de hecjo, establecen importantes supuestos
de <<conocimeinto común>>  sobre la experiencia compartida y los tipos de cosas que interesan e informan a los alumnos,
vamos a concentrarnos aquí en el discurso en clase de tipo más abiertamente interactivo.

"""

"""
Contribuciones espontáneas y sonsacadas

"""

"""
Las contribuciones espontáneas ofrecidas por los laumnos eran por definición menos  influidas
por el control de la maestra. Pero había control. Era la maestra quien había confeccionado la agenda, definido el tema
de discusión y establecido por anticipado los criterios de relevancia y la adecuación de cualquier contribución
que pudiesen presentar los alumnos. La maestra mantenía generalmente el control del destino último de tales contribuciones:
sobre si se actuaba según ellas, se tomaban y se incorporaban al desarrollo de ideas en el discurso posterior de la clase,
o si eran desalentadas, desaprobadas o ignoradas. Aparte de estas consideraciones, también es muy posible que los pensamientos
expresados tuvieran en última instancia su origen en otra lección (como remarcábamos al hablar de la <<continueidad>> en el capítulo 5).
En el capítulo anterior hacíamos un examen de algunas contribuciones espontáneas, y quedaba claro que la maestra mantenía el control sobre el destino de éstas;
podía desalentar o no hacer caso de cualquier desarrollo de la idea de los mecanismos de compensación que actúan en el movimiento
del péndulo, definir la variación de la sustancia del cordel como marginal y no concluyente, y proporcionaba en general el marco de actividad
y discurso dentro del cual tenían lugar todas estas contribuciones de los alumnos.

Empecemos, pues, por hacer una definición de las contribuciones espontáneas de los alumnos.
Se trataba de ocasiones en que los alumnos, sin invitación explícita por parte de la maestra, ofrecían información, sugerencias o vistas,
no habían sido enseñadas ni demostradas por la maestra. Incluiríamos, pues, aquí la observación de Jonathan respecto a la acción de las bolas de billar,
así como la sugerencia de David sobre una relación compensatoria entre velocidad y distancia (secuencias 6.1 y 6.2). Sin embargo, la mayor parte de las
contribuciones al discurso en clase ofrecidas por los alumnos se veían limitadas de manera directa por las preguntas de los maestros y por los requisitos normales
en toda respuesta a una pregunta: que sea relevante, apropiada, informativa, etc. (Grice, 1975).

"""
"""
La importancia de los IRF en el establecimiento de la comprensión conjunta radica en el modo en que se expresan la complentariedad del conocimiento
del maestro y del alumno. Como veíamos en capítulo 4, las preguntas de los maestros son de un tipo especial, en el sentido de que no contienen el presupuesto
habitual de que el hablante no conoce la respuesta a la pregunta.

En el capítulo 5 mostrábamos que funcionan como mecanismos de discurso a través de los cuales el maestro puede mantener un control constante sobre la 
comprensión de los alumnos, asegurarse de que los diversos conceptos, información o términos de referencia son comprendidos de manera conjunta para 
de intersubjetividad en desarrollo. Las estructuras IRF tienen también la función de definir y controlar cómo van a ser este conocimiento y esta comprensión.
Forman parte de una serie de mecanismos de comunicación por los cuales el maestro actúa como una especie de filtro o compuerta a través de la cual debe pasar todo el conocimiento
parq su inclusión en la lección como contribución válida o útil.

Esto puede verse de manera especial en ejemplos de los que podríamos llamar << obtención restrospectiva >>, en la que el maestro invita al alumno
a responder cuando éste ya lo ha hecho (SECUENCIA 7.1).
"""
"""
Secuencia 7.1 Obtenciones retrospectivas
""" 
"""
M: ... Bien, problemas hasta aquí,
cualquier pregunta que queráis hacer,
cualquier idea.                         Sharon mueve la cabeza.
                                        Sharon señala a lo alto del pendulo
Sharon: Creo que yo [ y Karen vamos ¿Que crees]
  a (&) 

M: 
  Sharon? 

Sharon: (&) medir por arriba.
M: Vais a medir por arriba para buscar 
   el ángulo. ¿Es eso/ Karen? 
   De acuerdo...                         M se vuelve hacia Karen.

"""