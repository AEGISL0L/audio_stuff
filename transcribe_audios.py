"""This module handles audio transcription and classroom discourse analysis.

This function processes a transcription of classroom interactions and extracts various metrics related to the question-response patterns, knowledge exchanges, and reasoning indicators. The metrics are returned as a dictionary.

Args:
    transcription (str): The transcription of the classroom interactions.

Returns:
    Dict: A dictionary containing the following metrics:
        - teacher_questions (int): The number of questions asked by the teacher.
        - student_responses (int): The number of responses given by students.
        - follow_up_questions (int): The number of follow-up questions asked by the teacher.
        - student_initiated_questions (int): The number of questions initiated by students.
        - knowledge_exchanges (int): The number of knowledge exchange instances.
        - reasoning_indicators (int): The number of instances where students used reasoning indicators.
"""
"""Analyzes classroom discourse patterns focusing on question-response dynamics.

This function processes a transcription of classroom interactions and extracts various metrics related to the question-response patterns, knowledge exchanges, and reasoning indicators. The metrics are returned as a dictionary.

Args:
    transcription (str): The transcription of the classroom interactions.

Returns:
    Dict: A dictionary containing the following metrics:
        - teacher_questions (int): The number of questions asked by the teacher.
        - student_responses (int): The number of responses given by students.
        - follow_up_questions (int): The number of follow-up questions asked by the teacher.
        - student_initiated_questions (int): The number of questions initiated by students.
        - knowledge_exchanges (int): The number of knowledge exchange instances.
        - reasoning_indicators (int): The number of instances where students used reasoning indicators.
"""

"""
Provides an analysis of classroom interaction patterns, including teacher control, student responses, and retrospective elicitations.

The ClassroomInteraction class tracks various interaction patterns observed in a classroom transcript, such as:
- Teacher control patterns, including questions asked by the teacher
- Student responses, including the student who responded and the content of the response
- Retrospective elicitations, where the teacher prompts students for responses they had already provided

The analyze_sequence method takes a transcript of classroom dialogue and extracts these interaction patterns, storing them in the corresponding lists within the class.
"""
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

def format_transcription(text: str) -> str:
    """Applies formatting rules to transcription text with enhanced markers.
    
    Formatting rules:
        - Pauses: "  " -> " / " (short), "   " -> " // " (long) 
        - Inaudible: "[inaudible]" -> "(...)"
        - Emphasis: "*word*" -> "«word»"
        - Overlapping: "[overlap]" -> "⟨overlap⟩"
        - Actions: "{action}" -> "【action】"
    """
    formatting_rules = {
        "  ": " / ",  # Short pause
        "   ": " // ",  # Long pause
        "[inaudible]": "(...)",
        "*": "«»",  # Emphasis markers
        "[overlap]": "⟨⟩",  # Overlapping speech
        "{": "【",  # Action start
        "}": "】"   # Action end
    }
    
    formatted_text = text
    for pattern, replacement in formatting_rules.items():
        if len(replacement) == 2:  # Handle paired markers
            parts = formatted_text.split(pattern)
            formatted_text = replacement[0].join(parts[::2]) + \
                           replacement[1].join(parts[1::2])
        else:
            formatted_text = formatted_text.replace(pattern, replacement)
            
    return formatted_text

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
def save_metadata(audio_file_path: str, transcription_stats: Dict) -> None:
    """Saves comprehensive transcription metadata in JSON format.

    Args:
        audio_file_path (str): Path to the original audio file
        transcription_stats (Dict): Statistics about the transcription process

    Metadata includes:
        - File information (name, path, format)
        - Processing details (duration, segments, timestamp)
        - Technical specs (sample rate, channels, bit depth)
        - Recognition stats (confidence scores, language)
    """
    metadata = {
        'file_info': {
            'original_file': os.path.basename(audio_file_path),
            'full_path': os.path.abspath(audio_file_path),
            'format': os.path.splitext(audio_file_path)[1],
            'size_bytes': os.path.getsize(audio_file_path)
        },
        'processing': {
            'transcription_date': datetime.now().isoformat(),
            'duration_seconds': transcription_stats['duration'],
            'segments_count': transcription_stats['segments'],
            'processing_time': transcription_stats.get('processing_time', 0)
        },
        'recognition': {
            'language': 'es-ES',
            'confidence_avg': transcription_stats.get('confidence_avg', 0),
            'segments_success_rate': transcription_stats.get('success_rate', 0)
        }
    }
    
    metadata_path = f"{os.path.splitext(audio_file_path)[0]}_metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

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
class ClassroomInteraction:
    def __init__(self):
        self.interaction_patterns = {
            'teacher_control': [],
            'student_responses': [],
            'retrospective_elicitations': [],
            'knowledge_exchanges': [],
            'shared_understanding': []
        }
        self.current_topic = None
        self.sequence_counter = 0
        
    def analyze_sequence(self, transcript: str):
        lines = transcript.split('\n')
        current_sequence = []
        
        for line in lines:
            # Track teacher control patterns with context
            if line.startswith('M:'):
                if '?' in line:
                    self.sequence_counter += 1
                    pattern = {
                        'id': self.sequence_counter,
                        'type': 'question',
                        'content': line,
                        'context': self._get_context(line),
                        'knowledge_type': self._classify_question(line)
                    }
                    self.interaction_patterns['teacher_control'].append(pattern)
                    
    def _get_context(self, line: str) -> str:
        """Extracts pedagogical context from teacher utterances"""
        contexts = {
            'explain': 'conceptual',
            'what if': 'hypothetical',
            'why': 'reasoning',
            'how': 'procedural'
        }
        return next((v for k, v in contexts.items() if k in line.lower()), 'general')
        
    def _classify_question(self, line: str) -> str:
        """Classifies the type of knowledge being elicited"""
        if any(term in line.lower() for term in ['because', 'why', 'explain']):
            return 'deep_knowledge'
        if any(term in line.lower() for term in ['what', 'when', 'where']):
            return 'factual_knowledge'
        return 'procedural_knowledge'

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
class IRFAnalyzer:
    """Analyzes Initiation-Response-Feedback patterns in classroom discourse.
    
    Tracks teacher-student interactions focusing on:
    - Teacher initiations (questions, prompts)
    - Student responses 
    - Teacher feedback/evaluation
    - Retrospective elicitation patterns
    """
    
    def __init__(self):
        self.interactions = []
        self.retrospective_patterns = []
        self.knowledge_validation = {
            'accepted': [],
            'redirected': [],
            'elaborated': []
        }

    def analyze_sequence(self, transcript: str) -> Dict[str, Any]:
        sequences = []
        current_irf = []
        
        for line in transcript.split('\n'):
            # Track teacher initiations
            if '[teacher]' in line.lower() and '?' in line:
                current_irf = ['initiation', line]
                
            # Track student responses
            elif '[student]' in line.lower():
                if len(current_irf) == 2:
                    current_irf.append(line)
                    
            # Track teacher feedback
            elif '[teacher]' in line.lower() and len(current_irf) == 3:
                current_irf.append(line)
                sequences.append(tuple(current_irf))
                current_irf = []
                
        return self._analyze_patterns(sequences)
    
    def _analyze_patterns(self, sequences: List[Tuple]) -> Dict[str, Any]:
        metrics = {
            'total_irf': len(sequences),
            'retrospective_elicitations': 0,
            'knowledge_validation': {
                'accepted': 0,
                'redirected': 0,
                'elaborated': 0
            }
        }
        
        for seq in sequences:
            # Identify retrospective elicitations
            if self._is_retrospective(seq):
                metrics['retrospective_elicitations'] += 1
                
            # Analyze feedback patterns
            feedback_type = self._classify_feedback(seq[3])
            metrics['knowledge_validation'][feedback_type] += 1
            
        return metrics
    
    def _is_retrospective(self, sequence: Tuple) -> bool:
        """Identifies if a sequence contains retrospective elicitation."""
        initiation, response = sequence[0], sequence[2]
        return response.lower() in initiation.lower()
    
    def _classify_feedback(self, feedback: str) -> str:
        """Classifies teacher feedback into validation categories."""
        if any(term in feedback.lower() for term in ['yes', 'correct', 'exactly']):
            return 'accepted'
        elif '?' in feedback:
            return 'redirected'
        return 'elaborated'


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

class ClassroomInteraction:
    def __init__(self):
        self.interaction_patterns = {
            'teacher_control': [],
            'student_responses': [],
            'retrospective_elicitations': []
        }
    
    def analyze_sequence(self, transcript: str):
        lines = transcript.split('\n')
        current_sequence = []
        
        for line in lines:
            # Track teacher control patterns
            if line.startswith('M:'):
                if '?' in line:
                    self.interaction_patterns['teacher_control'].append({
                        'type': 'question',
                        'content': line
                    })
                    
            # Track student responses
            elif any(student in line for student in ['Sharon:', 'Karen:']):
                self.interaction_patterns['student_responses'].append({
                    'student': line.split(':')[0],
                    'response': line.split(':')[1]
                })
                
            # Identify retrospective elicitations
            if len(current_sequence) > 0 and line.startswith('M:'):
                if any(prev['response'] in line for prev in self.interaction_patterns['student_responses'][-3:]):
                    self.interaction_patterns['retrospective_elicitations'].append({
                        'original': current_sequence[-1],
                        'elicitation': line
                    })
            
            current_sequence.append(line)
            
        return self.interaction_patterns

# Example usage
analyzer = ClassroomInteraction()
sample_transcript = """
M: ... Bien, problemas hasta aquí,
cualquier pregunta que queráis hacer,
cualquier idea.
Sharon: Creo que yo y Karen vamos a medir por arriba.
M: Sharon?
Sharon: medir por arriba.
M: Vais a medir por arriba para buscar el ángulo. ¿Es eso Karen?
"""

patterns = analyzer.analyze_sequence(sample_transcript)

Sesión 2 sobre el pendulo

"""
M: ... ¿Que es lo que/ hace que el
   péndulo se balancee hacia abajo/
   por ejemplo hasta que llega aquí?          Da un golpecito con el lápiz
M: Jonathan? [La gravedad. Mirad./ ¿Qué es,   indicando <<aquí>> al pie
Jonathan: La gravedad.                        del péndulo. Jonathan levanta la mano al hablar.
M: Si./ Bueno, mencionamos la gravedad
   cuando estábamos haciendo los
   experimentos pero no hablamos mucho
   de ella. Cuando la esfera tira hacia
   abajp, eso es la gravedad. De acuerdo.
   ¿Qué es lo que hace que vuelva a subir
   por el otro lado?                          M suelta la esfera
Antony: El cordel/ hace subir el cordel/      Entonación llana: Antony aún no ha terminado de hablar.
   al bajar
M: Aumenta la velocidad al bajar./
   ¿Sabe alguien la palabra cuando
   se aumenta la velocidad/ como 
   cuando se pisa el pedal de un coche?
Jonathan: Acelerar
Antony: Impulso
M: Se gana impulso/
   ¿Jonathan?
Jonathan: Acelera
M: Acelerar al bajar, ¿es eso?

This code excerpt provides examples of the teacher's interaction patterns in the classroom, specifically:

- The teacher solicits responses from students (Sharon and Jonathan) and then repeats and highlights the appropriate responses for the whole class to hear.
- The teacher uses a retrospective elicitation technique, where she prompts the students to hypothesize about the effect of shortening the pendulum's string on its period of oscillation.

These examples illustrate the teacher's strategies for guiding the classroom discussion and ensuring the students' understanding of the key concepts related to the pendulum experiment.
Las respuestas de Sharon y Jonathan en las secuencias 7.1 fueron solicitadas por la maestra,
para que fueran repetidas y destacadas, remarcadas para que todos oyeran las respuestas adecuadas.
Parte de la secuencia 6.4 es un interesante ejemplo de obtención retrospectiva, en el que la maestra
sonsaca hipótesis ejemplo de obtención retrospectiva, en el que la maestra sonsaca hipótesis
sobre el efecto que el acortar el cordel podía tener sobre el período de balanceo:

Sharon: Iría más despacio
m: ¿Qué calculas tú/
Jontahan: Mucho más rápido.
Sharon: Más despacio./
   rápido. Creo que iría más rápido.

Sharon ofrecía primero la hipótesis <<iría más despacio>>. La maestra definía luego la
contribución de Sharon como válida y adecuada, invitándola explícitamente. Entonces,
Sharon vacilaba y cambiaba de idea. Dos cosas pudieron influir en ella. En primer lugar,
Jonathan estaba sugiriendo simultáneamente que la esfera iría más de prisa.

En segundo lugar, lo que no es menos importante, pudiera ser que estuviera actuando aquí
otra regla básica. Es posible que Sharon interpretase que la maestra estaba repitiendo la pregunta
, haciendo la misma pregunta después de haber obtenido una respuesta, en lugar de estar
haciendo una invitación retrospectiva. Como observábamos en el capítulo 4,
esto indica generalmente que la primera respuesta es equivocada, y que se espera una respuesta
alternativa. Nos encontramos probablemente con un conflicto entre dos reglas básicas de
discurso alternativas. Mientras la maestra estaba procurando obtener retrospectivamente la s
respuesta de Sharon, ésta veía sus palabras como una repetición de la pregunta e inmediatamente
cambiaba de idea.

Hemos visto también en el capítulo 6 el destino de respuestas menos bien acogidas. La maestra
no hizo caso, o simplemente se limitó a no alentar o desarrollar varios intentos de introducir ideas que no 
formaban parte del curso de la lección planificada, tales como la noción de efectos compensatorios
recíprocos de velocidad y ángulo de balanceo, así como la sugerencia de que podría estar bien alterar la variable de la sustancia
del cordel ( secuencias 6.1, 6.2 y 6.7); del mismo modo, no mostró interés por la insistencia de David y Antony
en que hbían medido un efecto importante debido al cambio de la sustancia del corden ( secuencia 6.3 ). 

La maestra no sólo comprobó y expuso en aquel momento sus observaciones sobre las comprensiones conjuntas, sino que
consiguió también tener bien sujetos la introducción y el establecimiento de lo que debía representar un conocimeinto compartido importante.
Controlaba, tanto de manera prospectiva como retrospectiva, el contenido de lo que se introducía, incluía, validaba y destacaba.

Podía desalentar o no hacer caso de las contribuciones de los alumnos, instarlas o darlas por válidas, destacando algunas, y, en general, controlar su orden, carácter e importancia.

"""
Caracterizar el conocimiento como algo significativo y conjunto

Aparte del fenómeno constante de invitar a los alumnos a ofrecer sus contribuciones, y a veces de no hacerles caso,
había mecanismos de discurso tales como la enunciación especial y el uso de frases del tipo fórmula de daban una preeminencia 
especial al conocimiento expresado. Los cambios de entonación servían a funciones pedagógicas, destacando la información importante y 
señalando otros comentarios como << apartes >>, o bien como poseedores de otra función. Aparte del uso convencional de mecanismos tales
como las pausas y la subida en la entonación para señalar las preguntas, los cambios, especialmente en la cantidad y volumen del habla,
tenían lugar generalmente en los límites de los cambios de importancia pedagógica, más que en los cambios de función coloquial.

Las palabras en cursiva de la secuencia 7.2 son las palabras a que se refieren los comentarios contextuales sobre la entonación.
La entonación sobre estas palabras les da una importancia especial en relación con el resto de lo que se dice. La elección
de una enunciación lenta y deliberada, o de palabras más rápidas y en voz más baja, estaba claramente determinada por el contenido
de lo que se decía y por su función pedagógica. El contenido importante orientado hacia el plan de estudios era destacado con una enunciación 
cuidadosa y clara, mientras que los << apartes >> sobre la visión de la maestra y el control sobre la continuidad de la comprensión estaban
marcados por un descenso en el volumen y un repentino aumento en la cantidad de palabras.

También en otro punto se reflejaba la condición pedagógica de lo que se decía en el discurso: en el uso de frases fórmula repetidas.
Estas actuaban como fórmulas fácilmente recordables a través de las cuales se daba preeminencia a ciertas obsevaciones y conclusiones, que se repetían 
y establecían como expresiones de comprensión compartida.

Surgían, durante las lecciones, del diálogo entre maestra y alumnos, iniciado a veces por éstos, pero eran, adoptadas y alentadas por la maestra como algo
correcto y apropiado. La secuencia 7.3 muestraa el desarrollo de un verso rimado. << The shorter the string, the faster the swing >> 
( cuanto más corto el cordel, más veloz en el vaivén), que acabó sirviendo como eenvoltura mnemotécnica dle principal hallazgo empírico de la lección.

La fórmula de la longitud del cordel fue inventada esencialmente por la maestra a modo de envoltura del principio establecido en el primer caso en dos partes, es decir, 
la pregunta de la mestra y la repsuesta de Antony. Más tarde, la rima se recordaba y recitaba conjuntamente, como alggo que 
<< hemos inventado >>. La lectura que la maestra daba a estos hechos era una lectura de aprendizaje inductivo conjunto;
<< nosotros >> habíamos inventado conjuntamente una fórmula verbal en cuyos términos podía expresarse y recordarse.
De manera similar. Sharon v Karen acabaron describiendo repetidamente sus resultados, los efectos de variar el ángulo del balanceo, como 
<< lo mismo exactamente>> o bien << lo mismo en resumidas cuentas >>. Al igual que en la secuencia 7.3., las frases acabaron siendo recitadas al unísono, 
como fórmulas reconocidas conjuntamente:

Secuencia 7.4 La fórmula de la equivalencia


Lección 2 sobre el péndulo: M recapitula sobre los resultados de la lección 1.

En el último segmento de la secuencia 7.4, tomada de la lección 2, la maestra estaba intentando hacer que los alumnos describieran sus gráficos, y en este caso
quería con toda probabilidad que Sharon lo describiese casi como una línea recta ( éstas fueron de hecho las palabras que se adoptarían más tarde).
Sin embargo, Sharon recordaba de la lección 1 como describir sus resultados: eran << todos iguales >> . No era sólo la maestra quien llamaba
la atención acerca de ello, daba claves para su repetición y las definía generalmente como importantes. La sugerencia hecha por Lucy en la secuencia 7.5, según 
la cual, al variar el peso de la esfera del péndulo, << aunque fuera una tonelada >> no cambiaría nada, fue adopatada, repetida y alentada por la maestra, y luego
recordaba como una frase-fórmula que servía de envoltura al resultado empírico esencial de los experimentos sobre la variación del peso.

def analyze_discourse(self, transcription: str) -> Dict:
    """Scans the given transcription and updates the discourse metrics.

    Uses IRF-based logic (Initiation-Response-Feedback) to identify teacher vs.
    student control and spots key language markers for knowledge exchange.

    Args:
        transcription (str): The classroom transcription under analysis.

    Returns:
        Dict: A dictionary with updated metrics on teacher control and student involvement.
    """
    segments = transcription.split('\n')
    current_irf = []
    
    for segment in segments:
        # Teacher control patterns
        if '[teacher]' in segment.lower():
            if '?' in segment:
                self.metrics['control_instances'] += 1
            if any(term in segment.lower() for term in ['explain', 'understand', 'mean']):
                self.metrics['knowledge_exchanges'] += 1
                self.discourse_patterns['teacher_control']['knowledge_definition'].append(segment)
        
        # Student participation
        if '[student]' in segment.lower():
            self.metrics['student_contributions'] += 1
            if any(term in segment.lower() for term in ['i think', 'because', 'therefore']):
                self.metrics['shared_understanding_markers'] += 1
                self.discourse_patterns['student_participation']['reasoning_markers'].append(segment)
        
        # Track IRF sequences
        if len(current_irf) < 3:
            current_irf.append(segment)
        if len(current_irf) == 3:
            self.metrics['irf_sequences'] += 1
            self.discourse_patterns['interaction_structures']['irf_sequences'].append(current_irf)
            current_irf =

            """

Secuencia 7.5 La fórmula << ni siquiera con una tonelada >>




¿Tienen estas frases fórmula una función pedagógica, y , en tal caso, cuál es? Parecen funcionar como envolturas de los hallazgos empíricos importantes
que han sido comprendidos conjuntamente y que los alumnos han sido llevados a descubrir en el curso de la actividad y el discurso de las lecciones.
La frase de Lucy, << ni siquiera con una tonelada >> , constituye una genralización poderosa, aunque no exactamente la expresión de un principio general,
respecto a los efectos que la variación de la masa de la esfera tiene sobre el período de balanceo. La frase << lo mismo exactamente >> representa, del mismo modo, la 
la equivalencia esencial de los resultados producidos por la variación del ángulo de balanceo. La rima << cuanto más corto el cordel, más veloz es el vaivén >>
es un principio explícito que capta el único hallazgo positivo.
Al ser guiados atentamente en el modo de interpretar y dar la importancia adecuada a sus experiencias, se ofrece a los alumnos en el proceso un lenguaje común
a través del cual puedan expresarse estas comprensiones comunes.

La condición de ciertas comprensiones, lograda en el curso de las lecciones, de << conocimiento compartido >> estaba a menudo marcada abiertamente en el discurso por el
desarrollo y el uso repetitivo de ese tipo de frases fórmula, junto con otros mecanismos tales como el habla simultánea ( que hemos visto especialmente en las secuencias 7.6 y 7.4)
, y en el uso por parte de la maestra de << nosotros >> al atribuirse también lo que se había hecho, dicho, y comprendido,
como cuando se recordaba a Antony y David la fórmula << más veloz es el vaivén >> (secuencia 7.3). Estos no eran casos aislados.
En la secuencia 6.12, cuando la mestra estaba alentando a los alumnos a ver las pequeñas diferencias como carentes de importancia, el uso de << nosotros >> implicaba una comprensión
conjunta en la que no había ninguna diferencia entree la intenciones e interpretaciones de la maestra y las de los alumnos: << Bueno, eso se acerca bastante, ¿no? 
Nueve setenta y tres se acerca bastante a diez. Ahora/ ¿qué hacemos? ¿Lo redondeamos en diez?>> y, en otro caso: << Bueno, lo que creo es que hemos de ponerle centésimas, ¿no?
Siete dos tres cinco, ¿cómo llamnaremos a esto? >> El cambio de << yo >> al << plural superior >> ( si podemos utilizar este término ) era una expresión abierta del propósito comunicativo
de la maestra de establecer ciertas observaciones e interpretaciones como conjuntas.

El hablar al unísono era asimismo un claro indicador de conocimiento compartido, en el que la maestra y los alumnos ensayaban su comprensión común a través de un lenguaje común y una
enunciación simultánea. Es importante dejar clara una distinción entre, por un lado, el habla simultánea en la que las personas hablan al mismo tiempo, quizás interrumpiendo o evitando
<< ceder el terreno >> a un interruptor, y , por otro lado, el hablar al unísono, donde las personas articulan conjuntamente las mismas palabras o singificados. 
Observamos en las secuencias de diálogo presentadas en los capítulos 6 y 7 (veánse por ejemplo las secuencias 6.12, 6.14, 7.2, 7.3 y 7.4) que este segundo tipo de habla simultánea tenía lugar
precisamente en aquellos puntos en que había importantes cuestiones de comprensión conjunta; en los puntos en que la maestra se esforzaba por asegurarse de que prevalecían sus propias Interpretaciones
de las << mediciones equivalentes >> (secuencias 6.12, 6.14, y 7.4) , y de que el principal hallazgo empírico, la ley << cordel más corto, balanceo más corto>>, era comprendido (7.2 y 7.3). 
El conocimiento común se basa, pues, en el establecimiento de las comprensiones del maestro como comprensiones conjuntas representadas en un discurso común - en este caso, de una manera muy sencilla y directa-.

Obtención mediante pistas

El proceso de obtencion mediante pistas estaba presente en nuestras transcripciones de datos. Vimos ejemplos del mismo en nuestra anterior discusión del contexto físico y gestual del discurso en clase ( capítulo 5 )
y en nuestra discusión de cómo la maestra obtenía de los alumnos de las diferentes hipótesis para probarlas en los experimentos sobre el péndulo ( capítulo 6 por ejemplo, secuencia 6.6). Las obtenciones mediante pistas son un discurso de tipo IRF,
en el que el maestro hace preguntas mientras proporciona simultáneamente postas eficaces paraa la información necesaria. Este fluir simultáneao de información puede conseguirse simplemente por el modo de articular
la pregunta, pero a menudo se logra mediante algún otro canal de comunicación, como, por ejemplo, la entonación, las pausas, los gestos o las demostraciones físicas.
Puede hacerse también de manera implícita, apelandi sin mencionarlo al conocimiento compartido. La secuencia 7.6. es un claro ejemplo.

Secuencia 7.6 Obtención mediante pistas: El pulso de Galileo



La obtención mediante pistas es un proceso importante por dos razones al menos:

1. Demuestra un punto general del método y la teoría: que, si queremos dar el sentido adecuado al proceso de educación en clasem necesitamos registros detallados de gestos y actividad así como transcripciones detalladas del discurso en clase;
que éstos deben estar ampliamente integrados; y que no hay que cometer el error de intentar explicar los procesos educacionales  sólo en términos de la charla en clase y de las estructuras de discurso.

2. Se trata de un proceso de comunicación de un interés intrínseco sustancial. Las preguntas y respuestas dentro de la clase tienen características peculiares, como hemos observado en el capítulo 4; la maestra, que conoce las respuestas, hace la mayor parte de las preguntas,
hace preguntas cuyas respuestas ya conoce, y , además , puede hacer preguntas mientras hace al mismo tiempo lo posible por proporcionar las respuestas a través de un canal alternativo.
Tenemos que buscar una comprensión de la función pedagógica de este hecho.

La mejor interpretación que podemos hacer de la función pedagógica de la obtención mediante pistas es que representa un proceso en el que los alumnos no son ni objeto de una extracción, en el sentido del e-ducare, ni tampoco se les enseña directamente, en el sentido de la << transmisión >> .
Por el contrario, se les está introduciendo en lo que para ellos se convierte en un discurso compartido con el maestro ( discurso en el sentido más amplio, que incluye los conceptos y la terminología así como el diálogo). Como tal, encaja perfectamente en el tipo de proceso educativo definido por la 
<< zona de desarrollo próximo >> de Vygotsky, en el que el conocimiento de los alumnos es ayudado y << apuntalado >> por las preguntas, pistas e instancias de la maestra para conseguir profundizaciones de las que los alumnos por sí solos parecían incapaces.
Es un mecanismo que exige que los alumnos participen activamente en la creación de un conocimiento compartido, en lugar de limitarse a estar sentados y escuchar cómo habla la maestra.
La obtención mediante pistas es también un proceso que constituye una solución a lo que hemos llamado dilema del maestro - un  necesario compromiso entre dos requisitos de conflicto, que la lección debe alcanzar-. Estos requisitos eran que los alumnos debían ( al menos aparentemente ) generar su propia comprensión
de las cosas a través de su propio pensamiento y experiencia, y que debían llegar a hacer y comprender actividades y conceptos específicos planificados al inicio: probar tres hipótesis
específicas, encontrar que sólo una de las variables era efectiva, calcular el promedio de los tiempos de veinte balanceos y hacer matrices y dibujar gráficos con los resultados. Naturalmente, éste es el conflicto observado por Rosalind Driver (1983) en su análisis de las limitaciones de la enseñanza inductiva de las ciencias
, del que hablábamos en el capítulo 6. La secuncia 7.7 muestra cómo la maestra consiguió que los alumnos aceptaran realizar los veinte balanceos previamente planificados.

Secuencia 7.7 Aceptación de veinte balanceos


Lucy, Karen, Jonathan y David parecían en el primer caso estar preparados y dispuestos a aceptar los cinco balanceos como un buen número. A través de una serie de pausas e instancias, acertaron eventualmente con el número requerido - << veinte >> - , justificado por la maestra en base a un concepto indefinido llamado << el margen de error>>.
Es aquí donde podemos ver claramente el carácter problemático de la obtención mediante pistas. Es difícil no tener la impresión de que los alumnos estaban esencialmente intentando leer todas las señales disponibles en un juego de adivinanzas en el que tenían que averiguar, mediante la habilidad comunicativa más que por la aplicación de algún principio de medición conocido, qué era
lo que la maestra intentaba que dijiesen. No había ninuna indicación de que los alumnos comprendieran lo que significaba el término de << margen de error >>,
aunque la sugerencia de Antony, << Por que lo reduce más >>, parecía prometedoramente profunda. Finalmente, los alumnos se habían visto llevados a aceptar los veinte balanceos
como un buen número, pero parecían ( por su mirada huidiza ) inseguros en cuanto a las razones. Les preguntamos en las entrevistas cuál les parecía que 
era la razón para hacer veinte balanceos. Sólo Jonathan parecía haber captado la importancia de la precisión y de la reducción del error, aunque no utilizó
la noción de << margen de error >> . Sharon contestó:

Bueno/ por que es como no demasiado rápido/ no demasiado lento y [la maestra] dijo bueno/ no estábamos seguros de lo que quería que hiciésemos.
Bueno dijo que probablemente lo mejor sería hacer lo que hacían los otros/ veinte balanceos/ así que hicimos todos lo mismo.

La respuesta de Sharon era enteramente de procedimiento, y hablaba en términos de hacer lo que la maestra quería que hiciesen. La respuesta de David
era también de procedimiento y carente de una comprensión de principios:

Por que era uno de los mejores para dividir... Creo que la primera vez que lo hicimos era con cinco cuando estábamos en eso y entonces pensamos bueno
hemos hecho diez y eso es casi lo mismo que cinco, así que hicimos veinte. Primero íbamos a hacer quince pero entonces decidimos hacerlo veinte veces.

La reconstrucción que hace David del procesi por el cual llegaron al número veinte es toda ella en términos de lo que << nosotros >> decidimos hacer, en forma
de una reconstrucción narrativa del curso que había tomado el diálogo en aquella ocasión. El rol de la maestra en cuanto a sus instancias no se ve representado en esta narración, i tampoco se menciona para nada el principio
de reducción del margen de error. Lucy sí invocó el término de << margen de error >>, aunque no está claro que comprendiese su significado:

Porque hay menos margen de error/ creo que era eso y tiene que ser más exacto que si sólo se hacen cinco... por que tienes más posibilidades de comparar/ algo así.

De nuevo, la expresión << creo que era eso >> sugiere un esfuerzo por recordar las palabras de la maestra, aunque tampoco está claro que Lucy comprendiese el principio.

Lo importante no es qué alumnos comprendían el principio y cuáles no, sino el hecho de que el discurso y la actividad de la lección no promovieran esta comprensión.

El peligro de la obtención mediante pistas radica en que, hasta ser examinada de cerca , puede dar una falsa impresión (probablemente a los participantes tanto como a los observadores) de la medida en que los alumnos comprenden,
y son en última instancia responsables, de lo que dicen y hacen. Puede ocultar, más que salvar, la brecha existente entre el maestro y el niño y que constituye la base del proceso desarrollista
de Vygotsky, y puede llevar por tanto a los tipos de comprensión de procedimiento, << ritual >>, identificados en el capítulo 6.

""" """" """" """ 

Reconstrucciones, supuestos y previos y paráfrasis

Bajando nuestra lista escanolada de procesos de comunicación, llegamos a continuación a una sere de mecanismos discursivos a través de los cuales la maestra
podía mantener un estricto control sobre el contenido del conocimiento compartido. Parafraseando lo que los alumnos decían y reconstruyendo lo que ocurría en la lección al hacer una recapitulación posterior, 7
podía volver a definir esas cosas de forma mucho más nítida, más limpia y más cercana a la intención del plan para la lección. Del mismo modo, dando ciertas cosas por
conocidas o las interpretaciones que se diesen a la experiencia. La paráfrasis eran a menudo aparentemente pequeñas y accidentales, como cuando en la lección 2 sobre
el péndulo, Lucy no recordaba bien uno de los tiempos cronometrados obtenidos en la lección 1, cuando ella y Jonathan habían variado el peso de la esfera del péndulo:

Secuencia 7.8 Parafraseando a Lucy

La maestra utilizaba también la paráfrasis de manera más directa como método de enseñanza, como en la secuencia 7.9, donde intentaba obtener lo más posible de la explicación de los alumnos y luego remodelar la explicación
ofrecida por Antony en una forma más de su agrado ( y de hecho, más precisa):


Secuencia 7.9 Parafraseando a Antony


Estas paráfrasis retrospectivas demuestran otra función de la etapa feedback de las secuencias IRF; proporcionan a la maestra una oportunidad no sólo de confirmar lo que dicen los alumnos,
sino de remodelarlo en una forma más aceptable, tal vez más explícita, o simplemente arropada en una terminología más de su agrado.
Las reconstrucciones más amplias tuvieron lugar durante la segunda de las lecciones sobre el péndulo, en que la maestra estaba recapitulando ( a través de las estructuras IRF de tipo conocido)
sobre eel material cubierto en la lección 1. Tanto la maestra como los alumnos estaban en el proceso de recordar uno a uno sus principales hallazgos empíricos.
Aquí tenemos la versión de Jonathan:

Secuencia 7.10 Recapitulación de los principales hallazgos empíricos            

La reconstrucción más notable de la secuencia 7.10 es la declaración de Jonathan de que él y su compañera han variado sólo el peso, que han cambiaado el número de arandelas
<< y lo hemos hecho a la misma altura [ es decir, ángulo ] todas las veces >>. Como observábamos en el capitulo 6. Jonathan y Lucy alternaron en realidad el ángulo además de la altura, hecho que la maestra
prefirió claramente ignorar, y no pudo establecerse si habían hecho uso o no de los controles adecuados al alterar las dos variables.

Cuando llegamos a la lección 2 ya se había captado la importancia de alterar las variables de una en una, y los alumnos y la maestra estaban preparados para iniciar una clara revisión
de lo que había ocurrido en realidad. Del mismo modo, la respuesta afirmativa de Jonathan a la sugerencia a la sugerencia de que el resultado lo hubiese sorprendido estaba en directa contradicción con su declaración
de la lección 1 (veáse secuencia 7.5), según la cual el resultado era exactamente el que él esperaba. De hecho, en la lección 2, poco después de la secuencia 7.10, articula la hipótesis reconstruida:
<< Creía que iba a ir más rápido porque el peso es diferente.>> Sea cual fuere la verdad de la cuestión, los hallazgos experimentales han quedado comprendidos conjuntamente como resultados que desmentían una hipótesis.
Quizá Jonathan no estuviese en un principio dispuesto a admitir lo que podía parecer entonces un error de juicio, el que hubiere hecho una predicción falsa.

En todo caso, en la lección 2 opta por confirmar lo que sugiere la maestra (<< Eso te ha soprendido, ¿verdad? >>), que el resultado fuese inesperado. Desde luego, es mucho
más aceptable que una hipótesis sea desmentida científicamente que haber cometido simplemente un error de juicio.

Otra notable recapitulación reconstruciva tuvo lugar en la lección 2, cuando la maestra y los alumnos estaban recordando el experimento de variación del ángulo de balanceo:

Secuencia 7.11 Reconstrucción de un principio de intervalos iguales


La secuencia 7.11 parece indicar que SHaron y Karen han escogido ángulos con la misma distancia de separación, 15º, como procedimiento científico adecuado. De hecho, como demuestra con toda claridad la secuencia 7.12 ( de la lección 1 ),
los cuatro ángulos fueron primero señalados sin medición en la alto del péndulo, y sólo luego, una vez terminado el experimento, se estimó, bajo indicación de la maestra, que eran equidistantes a intervalos de 15º. De hecho, Sharon y Karen habían determinado ya antes sus ángulos
de balanceo probando y descartando, sin calibrar, limitadas por los ángulos en los que el cordel tropezaba con el montante del péndulo.

Secuencia 7.12 Cómo se midieron los intervalos iguales

La idea de que se utilizaran cuatro intervalos equidistantes para medir los ángulos de balanceo fue construida durante la primera lección a partir de la 
posición casual de las señales en el péndulo y de la instancias de la maestra, y fue luego reconstruida en el discurso de la lección 2 como un principio
científico que limitaba la conducción adecuada de los experimentos. El modo en que se llegó en realidad a los intervalos no fue articulado en ningún momento.
Sería, evidentemente, falso dar demasiado énfasis a la importancia de lo que aprenden los alumnos a aprtir de simplemente de su propia actividad y experiencia, aun 
trabajando en parejas o en grupos. Lo que realmente importa es la interpretación que se da a esa experiencia, las palabras. Y es principalmente la maestra quien proporciona estas palabras.
Y es principalmente la maestra quien proporcuina estas palabras al tiempo que elimina otras del vocabulario común, y quien gobierna el proceso discursivo en que se establecen descripciones 
y versiones particulares de acontecimientos como base de la comprensión conjunta.

Uno de los medios más poderosos que poseía la maestra para imponer su definición de cómo deben interpretarse las cosas era utilizando la implicación y el supuesto previo.
Suponiendo simplemente que determinada interpretación era correcta, no planteándola como una cuestión abierta, podía mantener una limitación estricta sobre
el curso del pensamiento de los alumnos. Por ejemplo, Antony y David fueron los alumnos que alteraron la única variable efectiva, el largo del cordel.

Contrástense las preguntas de la maestra a Sharon y Karen (<< ¿Cómo va? ¿Algún resultado?, Sharon?>>) con la pregunta a Antony y David: << Bueno, ¿es el cordel más corto el que va más rápido o el más largo?>>
Mientras que a Sharon se le ofrecía la posibilidad de negar que hubiese encontrado algún resultado, en el caso de Antony y David había el supuesto previode que los cordeles
van más rápido o más despacio según la longitud, y la pregunta era qué longitud porducía una mayor velocidad. La respuesta de David fue clara: << No, el corto va más rápido >>

Remarcábamos en el capítulo 5 que un rasgo esencial del discurso educacional, y, de hecho, del discurso en general, es que éste siempre se basa en algún tipo de supuestos contextuales.
En las clases escolares, estos supuestos contextuales constituyen el cuerpo del conocimiento y pensamiento compartido que se va creando según desarrollan las lecciones. Pero los 
supuestos contextuales no tienen por qué implicar una informaci´´on o unas ideas que hayan sido previamente comunicadas de manera explícita. La información puede introducirse en una conversación a través de su rol
como contexto implícito para lo que se declara explícitamente. La parte implícita de un mensaje puede recuperarse del contexto situacional y de lo que explícitamente se dice,
y esto constituye también un rasgo normal del discurso cotidiano. Si alguien nos pide en la calle la dirección de la oficina de correos más próxima, tendremos motivos razonables para suponer que quiere ir allí
, que no sabe el camino, etc. El indicar un supuesto previo de contextos de enseñanza tiene una función pedagógica por encima de su uso en muchos otros ( aunque es evidente que gran parte de la retórica persuasiva,
la propaganda, la publicidad, etc., funciona de manera similar). Sirve para introducir ciertos puntos de conocimiento y suposición como algo que hay que aceptar sin reservas,
algocuerdo, y, por lo tanto, en un sentido más general, está a disposición del maestro como piedra de toque o como instrumento de control sobre lo que se conoce y comprendre.

Un caso particular de enseñanza implícita tuvo lugar cuando la maestra introdujo una terminología más de su agrado, palabras de la jerga científica tales como << masa >> e << impulso >>. A veces, estos términos
se introducían a través de ki que podriamos llamar << enseñanza directa >>, en la que la maestra introducía explícitamente las palabras, las definía y alentaba a los alumnos A
la obtención, con o sin pistas, como en el caso de los términos << impulso >> y << aceleración >> de la lección 2 (<<¿sabe alguien cuál es la palabra cuando se aumenta la velocidad/ como cuando se pisa el pedal de un coche?>>)
. La secuencia 7.13 muestra cómo se introdujeron varios términos mediante el simple uso de los mismos por parte de la maestra en un contexto comprendido,
como vocabulario alternativo, e implícitamente mejor.

Secuencia 7.13 Adquisición de un vocabulario compartido: utilización por la maestra


Mientras los alumnos han utilizado términos cotidianos tales como << peso >> y << colgar recto para abajo de un dedo>>, la mestra no sólo ha utilizado estos términos sino que ha introducido también jerga más técnica,
<< masa >>, << suspendido >> y << de un punto fijo >> (veáse secuencia 7.1, en la que la maestra obtiene el término << acelerar >> en sustitución de la expresión de Antony << hace subir el cordel/ al bajar>>). Después de haber establecido los diversos atributos que componen un péndulo, la maestra los recapitula con los alumnos.

Secuencia 7.14 Adquisición de un vocabulario compartido: utilización por los alumnos



Los alumnos han captado rápidamente la nueva terminología introducida por la maestra y han empezado a utilizarla ellos también. No está claro que comprendieran inmediatamente y del todo su significado.
El término de << masa >>, sugerido por David, es ambiguo por el hecho de que éste no comprende que << masa >> significa aquí algo equivalente a << peso >> y por su sensación de que la maestra simplemente prefiere ese término, lo que hace que valga la pena mencionarlo.
A pesar de la ausencia de enseñanza directa -la maestra no ha enseñado de manera explícita estos términos ni ha pedido o alentado abiertamente a los alumnos adoptarlos-, se ha convertido en términos comunes de referencia para señalar una comprensión común. Simplemente utilizando los términos en un contexto en que podían entenderse, en este caso comom alternativa a las palabras cotidianas utilizadas por los alumnos,
la maestra ha conseguido inducir a los alumnos a un discurso científico compartido, un marco compartido de referencia y concepción que se puede hacer del carácter de la enseñanza y aprendizaje del tipo examinado en los tres últimos capítulos.

Se trata de la inducción de los niños al mundo académico de conocimiento y de discurso en que se mueve la maestra.
Es un proceso de socialización cognitiva a través del discurso, un proceso tan afín al menos a la socialización cognitiva a través del discurso, un proceso tan afín que lemos a la socialización general ideológica y de conducta como a las nociones psicológicas cognitivas de crecimiento y desarrollo mentales.

Discurso y conocimiento en clase 

En las clases << tradicionales >> de Gran Bretaña, los alumnos recibían pasivamente el saber comunicado por la maestra. Se les ppedía que permanecieran práctiamente mudo hasta que se les invitaba a hablar, que hablaran sólo al maestro y que aprendieran rotativamente una larga serie de datos de cultura - desde las fechas de sucesión de los reyes y reinas de Inglaterra a deletrear correctamente las palabras, cuántos quintales tiene una tonelada y las tablas de multiplicar-.
Bajo la influencia de la teoría y la investigación psicológicas (principalmente de Piaget), junto con los cambios de la ideología de la educacióm, la enseñanza primaria de Gran Bretaña ha sufrido una gran transformación de tipo << progresivo >>. 
Está claro que el aprendizaje rotativo no equivale a alcanzar la comprensión, y que los niños aprenden mejor si participan activamente en la materia inmersos pasivamente en la charla del maestro.

Aunque, a nuestro modo de ver, esto constituye una importante mejora con respecto a los métodos tradicionales de enseñanza, sigue dando a pie problemas propios, << algunos de los cuales hemos intentado describir en los dos últimos capítulos>>.

Un resultado general que nos sorprendió fue la medida de control ejercido por la maestra, incluso en clases caracterizadas por una enseñanza de tipo más progresivo. En las lecciones sobre el péndulo, por ejemplo, los niñoas trabajaban en pequeños grupos subdivididos en parejas de alumnos con un péndulo para cada una, Y
descubrían a través de sus propias actividades los principios que gobiernan el movimiento del péndulo. A simple vista, el rol de la maestra era esencialmente facilitador, ya que modelaba la dirección general de la lección,
pero se apoyaba en gran medida en que los mismos alumnos planteasen hipótesis, procedimientos y criterios para hacer pruebas, realiaar ellos mismos los experimentos y también las observaciones de medición.

Al hacer un examen más detenido se vio con mayor claridad la medida de control de la maestra. Como hemos demostrado en este capítulo, la libertad de los alumnos para introducir sus propias ideas
era en gran medida ilusoria; la maestra mantenía un estricto control sobre lo que se decía y hacía, las decisiones a las que se llegaba y las interpretaciones que se daban a la experiencia.

Naturalmente, nos cuidaremos de generalizar una pequeña muestra de discurso en clase y convertirla en un análisis del estado general de la enseñanza primaria británica. 
No es éste nuestro propósito, y por eso no hemos codificado ni contado los diversos tipos de fenómenos identificados. Semejante procedimiento sse prestaría al tipo de comparaciones
estadísticas entre clases y escuelas diferentes que no eran la finalidad de nuestra investigación. Por el contrario, hemos optado por someter pequeñas muestras de discurso y activiadad en clase a un detenido análisis cuantitativo, con la esperanza de descubrir en ese discurso claves sobre cómo se construye y comparte, en realidad, el conocimeinto entre maestro y alumno.

Sin embargo, no es nuevo el descubrimiento de una abrumadora sensación de control por parte de la maestra: en la confección de la agenda, en la determinación antes de la lección de cuáles deben ser los resultados, y, en general,
en la expresión del rol social autoritario de la maestra en cuanto al control tanto epistemológico como de conducta. Edwards y Furlong (1978), por ejemplo, basan también su análisis del discurso en clase como lo hemos hecho nosotros. Otros utilizan índices lingüísticos más específicos y cuantificados.

Feldman y Werstch (1976), por ejemplo, midieron la frecuencia con que los maestros norteamericanos utilizaban una serie de verbos auxiliares que expresan difereentes grados de inseguridad. 
Comprobaron que éstos se utilizaban más en la sala de profesores que en clase; la charla en clase se juzgaba autoritaria, segura de los hechos y << cerrada >>, en comparación con la charla más abierta
, hipotética, e insegura entre los maestros.

Nuestros  hallazgos segieren las siguientes conclusiones sobre los procesos educacionales observados:

1. El aprendizaje basado en la experiencia y control por parte del maestro. A pesar del  ehcho de que las lecciones estaban organizadas en términos de acciones prácticas y actividad conjunta en grupos reducidos entre los
alumnos, el tipo de aprendizaje que tenía lugar no era esencialmente una cuestión de aprendizaje basado en la experienciaa ni en la comunicación entre los alumnos.
El rol de la maestra era en todo momento crucial, tanto en el modelado de la estructura y contenido generales de la lección como en la matizada definición de lo que se hacía, decía y comprendía.
Los alumnos no tenían , pues, la oportunidad de crearse sus propia comprensiones e interpretaciones.

2. Ritual y principios. Sin dejar de mantener un estrecho control sobre la actividad y el discurso, la maestra prefería e intentaba actuar según el principio educacional del aprendizaje basado en la experiencia y centrado en el alumno,
así como en la importancia de la participación de los alumnos en la actividad y el descubrimiento prácticos. Esto hacía que la idea que se formaban los alumnos de ciertos conceptos importantes fuese esencialmente << ritual >>, una cuestión de qué había que hacer o decir, más que <<de principios>>,
es decirm basada en una comprensión conceptual. Entre los tipos de particulares de discurso en clase que servían de base a la creación de este conocimiento << de procedimiento >> estaba la gran confianza en la << obtención mediante pistas >> junto
con un abrumado interés por llevar las lecciones a base de pasar por toda la serie planificada de actividades, en lugar, por ejemplo, de asegurarse de que todos entendían una serie planificada de conceptos.

La medida misma del control de la maestra sobre la actividad, el discurso y la interpretación, probablemente había contribuido al hecho de que la comprensión de las lecciones por parte de los alumnos llegara a menudo a consistir en saber lo que se hacía (o, al menos, su versión reconstruida oficial) y lo que había que decir.


3. El lenguaje y la socialización de la cognición. Nos hemos centrado en el << contenido >> del conocimiento y el discurso, en lo que se hacía y decía, las palabras utilizadas,
los conceptos en cuestión, las acciones realizadas. Ha habido quien ha observado atentamente la forma del discurso en clase, bien sus estructuras sociolingüíticas (por ejemplo Sinclair y Coulthard, 1975; Mehan, 1979) o su relación con propiedades formales del pensamiento tales como la capacidad de razonamiento lógico (Walkerdine, 1984).
La conclusión que se deriva de nuestros estudios ees la de que el discurso en clase actúa estableciendo comprensiones conjuntas entre maestro y alumno, marcos compartidosde referencia y concepción, en las que el proceso básico (incluidos los aspectos problemáticos de este proceso) consiste en introducir a los alumnos en el mundo conceptual de la maestra,
y, a través de ella, de la comunidad educativa. En la medida en que puede observarse que el proceso de eduación tiene lugar en el discurso situado de la clase se trata, esencialmente, según nuestras pruebas, de un proceso de socialización cognitiva a través del lenguaje.

La relación del poder y el control con la creación de comprensiones conjuntas a la vez problemática y de gran importancia. Según Habermas (1970, pág. 143), la <<intersubjetividad pura>> se consigue sólo en condiciones de <<completa simetría en la distribución de evaluación y controversia, revelación y ocultación, prescripción y seguimiento,
entre los participantes en la comunicación>>. Pero el interés inherente de la eduacación es el de introducir a los niños y a los adultosen una cultura preexistente de pensamiento y lenguaje. Por muy activo que sea el papel que se permite desempeñar a los alumnos en su aprendizaje, no debemos suponer que puedan simplemente reinventar esa cultura a través de su propia actividad y experiencia.
Se trata forzosamente de un proceso social y de comunicación, de un proceso que tiene como parte inherente una asimetría de roles entre maestro y alumno. El aprendizaje cultural preescolar, y en especial el aprendizaje de la primera lengua, ha sido descrito por Lock (1979) como un proceso de << reinvención dirigida >>. En las escuelas, la asimetría del poder es más marcada. La escolarización es algo obligatorio,
separado de la vida en el hogar, más formal y con un programa más arbritario. Muchos niños van de mala gana a la escuela. Los maestros se ven a menudo principalmente como fuentes de castigo (Hood, McDermott y Cole, 1980). 
Si no se quiere que el proceso educacional llegue a su término comprometido por la asimetría entre maestro y alumno , debemos desarrollar una comprensión del proceso que reconozca y aliente esta asimetría de un modo que fomente el aprendizaje en vez de obstaculizarlo.

Para los alumnos, parte del problema consiste en que el proceso es siempre en gran medida, un misterio para ellos. Aunque sea de una manera cordial y poco formal, se les pide a menudo que hagan cosas, aprendan cosas y comprendan cosas, sin otra razón aparente que el hecho de que esto es lo que es maestro quiere que hagan. las metas y objetivos de la lección permanecen ocultos. 
Y de hecho, lo mismo ocurre a menudo con los conceptos que estaba destinada a << cubrir >> la lección. En el ethos del aprendizaje inductivo centrado en el alumno no es aceptable decir a éste lo que debía descubrir por sí mismo, ni siquiera una vez terminadas las diversas actividades de aprendizaje. Recuérdense de las entrevistas del capítulo 4 con los niños que habían hecho el simulacro de la << isla desierta >>;
en aquellas entrevistas les preguntamos de qué creían que había tratado la lección y lo que creían que debían aprender de ella. Sus respuestas mostraban que, para la mayoría de ellos, se trataba de un ejercicio de supervivencia, algo que podía serles de utilidad práctica si algín día se hallaban en una situación parecida. Una lección que había sido pensada para ayudar a los alumnos a conceptualizar aspectos de la sociedad en que vivirían en una isla desierta o en Africa.

Los principales componentes del proceso de aprendizaje maestro alumno que hemos presentado aparecen en la concepción que Vygotsky tiene del mismo.
La asimetría entre maestro y alumno es esencial para la << zona de desarrollo próximo >>, como también los es la noción de control. Los niños no adquieren simplemente conocimientos y vocabulario. Adquieren al mismo tiempo la capacidad para la autorregulación. Del mismo modo que el pensamiento verbal se origina como discurso social, la conducta autoregulada empieza con la regulación de la propia conducta por parte de otras personas. El éxito del proceso implicaun traspaso gradual de control del maestro
al alumno a medida que el alumno va siendo capaz de hacer por sí mismo lo que antes sólo podía hacer con ayuda. En la educación formal, esta parte del proceso rara vez se realiza. Para la mayoría de alumnos, la educación es un misterio que  a su control más que un recurso de conocimientos y aptitudes que pueden manejar libremente. Como han señalado Bruner (1985) y otros, hay un gran contraste entre la escolarización formal y el aprendizaje de la primera lengua.
En el siguiente ejemplo se contrasta la educación formal con el aprendizaje del juego del peekaboo:

La madre empieza representando ella misma todo el guión y el niño va tomando un rol cada vez más activo, hasta que llega a recitaar todos los papeles que primero recitaba la madre. El contraste entre estos entornos de aprendizaje es enorme. En las lecciones escolares, los maestros dan instrucciones y los niños las ejecutan de manera no verbal; los maeestros hacen preguntas y los niños las responden, a menudo sólo con una palabra o una frase.
Y, lo que es más importante, estos roles no se invierten... Los niños nunca dan instrucciones a los maestros y son raras las preguntas que se hacen a los maestros, excepto para pedir permiso (Forman y Cazden , 1985, pág. 344).

Un proceso educacional logrado es el que transfiere competencia al alumno. Parece casi como si la educación formal, para la mayorían de los alumnos, estuviese destinada a evitar que esto ocurra.


"""

"""

8. CONCLUSIONES Y CONTENIDOS IMPLICITOS

Empezaremos este último capítulo haciendo un resumen de los principales puntos que hemos tratado en el libro hasta ahora.

1. Hemos adoptado una perspectiva sobre el pensamiento y la comprensión humanas que hace hincapié en su base en la comunicación y en las relaciones humanas.
El saber y el pensamiento no tienen sólo que ver con cómo piensan los individuos, sino que son intrínsicamente sociales y culturales. Nos hemos centrado, por tanto, en
lo que llamamos << conocimiento compartido >>, observando cómo éste se construye a través de la actividad y el discurso conjuntos.

2. Mediante el discurso y la acción conjunta, dos o más personas construyen un cuerpo de conocimiento común que se convierte en la base contextual para la comunicación posterior.
Los mensajes abiertos, las cosas que realmente dicen, son sólo una pequeña parte del conjunto de la comunicación. Son sólo la punta del iceberg, en el que la gran masa oculta de debajo
es esencial para el carácter de lo que está abiertamente visible por encima del agua. Por eso el contexto y la continuidad son consideraciones esenciales en el análisis del discurso.

3. El << contexto >> es básicamente un fenómeno mental. Las cosas de << ahí fuera >> se hacen contextuales sólo cuando son invocadas, es decir, cuando se hace referencia a ellas, se suponen o se
insinúan en la comunicación. El mismo acto de nombrar las cosas, o de suponer comprensiones compartidas de las mismas, convierte, para los comunicantes, su realidad en una realidad social y conceptual más que de simple
existencia física en el mundo de alrededor. El contexto es el conocimiento común de los hablantes invocado por el discurso. Es problemático tanto para los participantes como para cualquier observador.
El concepto que tienen los participantes de los contextos mentales de los demás puede estar equivocado o, lo que es más probable, ser acertado sólo en parte.
Del mismo modo, los investigadores se encuentran con el problema de determinar qué es contextual. Cualquier serie física de circuntancias podría prestarse a una infinidad de posibles concepciones y relevancias compartidas,
y,  en todo caso, los contextos mentales de la comunicación coloquial no están en modo alguno limitados a las circunstancias físicasde los actos del habla. La <<continuidad>> es asimismo problemática porque también es mental (o, 
para ser más precisos, inter-mental). La continueidad es una característica del contexto, y es también contexto al desarrollarse en el curso del tiempo en el proceso de la charla y la acción conjuntas.
Existe en tanto que memoria e intención compartidas, las concepcioness y supuestos que mantienen los participantes acerca de lo que han hecho y dicho, de su importancia, de lo que significa la interacción y a dónde va.

4. Hay una importante función de la educación que podemos describir como socialización  cognitiva. La investigación que podemos describir como socialización cognitiva. La investigación en concreto de la que hemos hablado examina algunos
aspectos de este proceso dentro de un marco cultural particular, el de algunas clases de enseñanza inglesas. Dentro de una sociedad, el sistema de enseñanza tiene su propia cultura epistemológica. Esta cultura, y el marco institucional dentro del cual
se educa a los niños, son lo que se distingue a la enseñanza de otros tipos de enseñanza cultural.

Los maestris tienen la misión de proporcionar << andamiaje >> a los primeros pasos del niño para dirigirlo e introducirlo en esta cultura, de supervisar su entrada en el universo del discurso educacional. Esto se hace
creando, a través de la acción y el habla con el niño, un marco contextual para las actividades educativas. Uno de los principales objetivos de la enseñanza es, pues, el desarrollo de un conocimiento compartido. Este es un proceso problemático, 
no sólo por que la creación de un discurso logrado es ya en sí problemática (representa el desarrollo de un contexto y una continuidad adecuados), sino también por que la seneñanza es forzosamente ideológica y se basa en relaciones sociales en las que el poder y el control tienen una gran importancia.
Una medida de la efectividad del proceso educacional es el grado en que el conocimiento educacional se vuelve << compartido >> a través del discurso en clase.
La importancia de una asimetría de poder entre maestro y niño hace que sea también problemático uno de los principales objetivos de la educación: el eventualmente
<<traspaso>> del control sobre el conocimiento y el aprendizaje del maestro al niño, a través del cual el alumno alcanza autonomía.

5. El discurso <<educado>> no es una habla <<desvinculada>> del contexto y diferente de formas menos elevadas del discurso por el hecho de ser más explícita. Por el contrario, es un habla que se apoya, para ser inteligible, en el acceso de los hablantes a marcos contextuales particulares e implícitos.
El discurso de las personas <<educadas>> que conversan acerca de su especialidad .matemáticas, filosofía, crítica literaria o cualquier otra cosa- sólo es explícito para los iniciados.

6. Una parte importante de la base contextual del discurso en clase ka forman un bloque de normas de que definen las actividades educativas necesarias para el éxito de la participación en el discurso educacional. Estas reglas educacionales básicas tienen funciones tanto sociales como cognitivas. Representan una serie
de convenciones sociales para presentar el conocimiento en la escuela y también una serie (o series) de procedimientos cognitivos para definir y solucionar problemas. Estas reglas son problemáticas tanto para los maestros como para los alumnos, por razones derivadas del hecho de que son normalmente implícitas. 
Forman parte de la <<agenda oculta>> del trabajo escolar, que rara vez, en todo caso, puede ser discutida e investigada por maestros y alumnos juntos.
Eso quiere decir que son tácticamente contextuales, y los