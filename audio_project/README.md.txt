File Descriptions:
audio/: Contains the raw audio files to be processed.
book/: Contains the text files of books or reference materials used for annotation.
scripts/:
preprocessing.py: Script for loading and preprocessing audio files.
tokenization.py: Script for splitting audio into manageable chunks.
transcription.py: Script for transcribing audio chunks into text.
annotation.py: Script for annotating transcriptions with comments from the book's logic.
database.py: Script for handling database operations (creating tables, inserting data).
main.py: Main script to execute the complete workflow from audio processing to annotation and storage.
transcriber.py: Script for reading audio files, transcribing them, and saving metadata.
data/:
chunks/: Stores the audio chunks generated during tokenization.
transcriptions/: Stores the transcriptions of the audio chunks.
annotated/: Stores the annotated transcriptions.
database/: Contains the SQLite database file storing the transcription and annotation data.
requirements.txt: Lists the Python dependencies required for the project.
README.md: Documentation for the project, explaining the purpose, setup, and usage instructions.
