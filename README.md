Este proyecto permite la transcripción automática de audio en tiempo real utilizando tecnologías de reconocimiento de voz. Es ideal para aplicaciones como subtitulado automático, reuniones, educación y accesibilidad. El sistema captura audio del micrófono, lo procesa en tiempo real y muestra la transcripción en la interfaz de usuario.

Además, este proyecto se integra con Tor para mantener la privacidad y anonimato de los usuarios al realizar solicitudes a través de la red Tor.

## IA - mi Sequoia personal

En general, las IA se enfocan en la seguridad y la inteligencia, pueden utilizar técnicas de aprendizaje automático para identificar patrones y tendencias en los datos, pero tambien pueden requerir de supervisión y ajustes humanos para asegurarse de que estén funcionando correctamente y no estén produciendo resultados erróneos.

Algunas de las técnicas de aprendizaje automático que la IA de Sequoia puede utilizar incluyen:

- Aprendizaje supervisado: la IA aprende a partir de datos etiquetados y supervisados por humanos.
- Aprendizaje no supervisado: la IA aprende a partir de datos no etiquetados y sin supervisión humana.
- Aprendizaje por refuerzo: la IA apende a partir de la interacción con un entorno y recibe recompensas o castigos por sus acciones.

# IA - no-DRM Sequoia

Sequoia desarrolla análisis de datos que permiten a las fuerzas de seguridad y la inteligencia analizar, procesar grandes cantidades de datos para identificar patrones y tendencias.

Implica entonces, Sequoia desarrolla sistemas de vigilancia y monitoreo que permiten a las fuerzas de seguridad y la inteligencia monitorear y analizar imágenes y videos en tiempo real utilizando técnicas intrusivas.

Sequoia utiliza la inteligencia artificial para desarrollar soluciones de seguridad y análisis de datos que permiten a las fuerzas de seguridad y la inteligencia tomar decisiones informadas en tiempo real.


## El conocimiento compartido

Este proyecto es una herramienta útil para mejorar la accesibilidad y la eficiencia en diversas aplicaciones; basado en mi lectura de Temas de educación Paidós/MEC; La investigación que en él se describe no trata del lenguaje en la clase como tal, por lo que no se le puede llamar investigación lingüística. Tampoco trata del carácter y funcionamiento del sistema de enseñanza, como podría ser el caso del trabajo de investigación sociológica. El código representa el trabajo de investigación psicológica.

Lo que se pretende investigar aquí son los modos en que el conocimiento se representa, se recibe, se comparte, se controla, se discute, se comprende o se comprende mal en el contexto de la educación. Nos interesa saber cómo se aprende, cómo se enseña, cómo se evalúa y cómo se evalúa el aprendizaje.





🚀 Características

    Transcripción en tiempo real: Captura el audio y lo convierte a texto de manera inmediata.
    Reconocimiento de múltiples idiomas: Detecta y transcribe varios idiomas automáticamente.
    Interfaz intuitiva: Muestra el texto transcrito en tiempo real, con una interfaz amigable.
    Exportación de transcripciones: Permite guardar las transcripciones en formatos como .txt o .docx.
    Detección de pausas y silencios: Mejora la precisión de la transcripción al ignorar pausas largas.
    Opcional: Integración con APIs de voz (Google, Azure, IBM): Mejora la precisión utilizando modelos preentrenados.
    Soporte de palabras clave personalizadas: Configura palabras clave específicas para mejorar la precisión en dominios especializados.

🛠️ Tecnologías utilizadas

    Python 3.x
    Flask: Framework para el backend de la aplicación.
    WebSockets: Para transmisión de audio en tiempo real.
    SpeechRecognition: Biblioteca de Python para el reconocimiento de voz.
    PyAudio: Captura de audio desde el micrófono.
    HTML5 & JavaScript: Interfaz web para visualización en tiempo real.
    

## 🛠️ Tech Stack

- Python 3.x
- Flask (Backend)
- WebSockets
- SpeechRecognition
- PyAudio
- HTML5 & JavaScript

## 📦 Installation

1. Clone the repository:

git clone <repository-url>
cd <project-directory>


2. Instala las dependencias:

pip install -r requirements.txt

3. Ejecuta la aplicación:

python app.py

4. Accede a la aplicación desde tu navegador:

      http://localhost:5000

🗣️ Transcripción en tiempo real

La transcripción en tiempo real permite convertir audio hablado en texto al instante. El proceso sigue estos pasos:

      Captura de audio: La aplicación utiliza PyAudio para capturar el audio del micrófono.
      Procesamiento del audio: El audio se envía al backend para su procesamiento.
      Reconocimiento de voz: Utiliza la biblioteca SpeechRecognition para convertir el audio en texto.
      Mostrar transcripción: El texto transcrito se muestra en la interfaz web en tiempo real.

📋 Ejemplo de uso

      Ejecuta la aplicación y permite el acceso al micrófono en tu navegador.
      Habla cerca del micrófono y observa cómo el texto aparece en tiempo real.
      Puedes pausar o detener la transcripción en cualquier momento.



🔒 Implementación de Transcripción en Tiempo Real con Tor
🛠️ Requisitos adicionales

    Instalar Tor: Necesitas tener el servicio de Tor instalado y ejecutándose en tu sistema.

En openSUSE, puedes instalar Tor con:

sudo zypper install tor

    Configurar Tor: Asegúrate de que el servicio de Tor esté habilitado y ejecutándose:

sudo systemctl enable tor
sudo systemctl start tor

    Instalar requests[socks]: Para realizar solicitudes HTTP a través de Tor, necesitamos instalar la librería requests con soporte para proxies SOCKS.

pip install requests[socks]

📦 Estructura del proyecto

Asegúrate de tener el siguiente archivo en tu proyecto Flask:

proyecto-transcripcion/
├── app.py
├── tor_config.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
├── requirements.txt
└── README.md

🔧 Configuración del archivo tor_config.py

Este archivo se encargará de manejar las solicitudes a través de Tor.

import requests

# Configuración del proxy de Tor
PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def get(url, params=None):
    """
    Realiza una solicitud GET a través de Tor.
    """
    try:
        response = requests.get(url, params=params, proxies=PROXIES, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error al conectar a través de Tor: {e}")
        return None

📝 Modificaciones en app.py

Integra la configuración de Tor en tu archivo principal de Flask.

from flask import Flask, render_template, request, jsonify
import tor_config
import speech_recognition as sr

app = Flask(__name__)
recognizer = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No se ha encontrado el archivo de audio"}), 400

    audio_file = request.files['audio']
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        # Realizar la transcripción utilizando una API de terceros a través de Tor
        result = tor_config.get(
            "https://api.speech-to-text.com/transcribe",
            params={"audio_data": audio.get_wav_data()}
        )
        if result:
            return jsonify(result)
        else:
            return jsonify({"error": "Error al procesar la transcripción"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

🌐 Modificaciones en index.html

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transcripción en Tiempo Real con Tor</title>
</head>
<body>
    <h1>Transcripción en Tiempo Real</h1>
    <form id="transcriptionForm">
        <input type="file" id="audioFile" accept="audio/*" required>
        <button type="submit">Transcribir</button>
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('transcriptionForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const audioFile = document.getElementById('audioFile').files[0];
            const formData = new FormData();
            formData.append('audio', audioFile);

            try {
                const response = await fetch('/transcribe', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                document.getElementById('result').innerText = data.text || data.error;
            } catch (error) {
                console.error('Error en la solicitud:', error);
            }
        });
    </script>
</body>
</html>

📄 Actualización del requirements.txt

Agrega las nuevas dependencias:

Flask
requests[socks]
SpeechRecognition
PyAudio

🛠️ Prueba del proyecto

    Ejecuta el servidor Flask:

python app.py

Accede a la aplicación en tu navegador:

    http://localhost:5000

    Sube un archivo de audio para probar la transcripción. La solicitud se enviará a través de la red Tor, manteniendo tu conexión anónima.

⚠️ Notas importantes

    Rendimiento: Usar Tor puede aumentar la latencia, lo que podría afectar la velocidad de la transcripción en tiempo real.
    Privacidad: Tor proporciona anonimato, pero no garantiza privacidad absoluta. Ten cuidado al manejar datos sensibles.
    Firewall: Asegúrate de que tu firewall permita el tráfico a través del puerto 9050 (puerto predeterminado de Tor).


