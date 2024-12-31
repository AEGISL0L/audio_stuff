import concurrent.futures
from pathlib import Path
from tqdm import tqdm
import logging
from config import load_config
from processor import TranscriptionProcessor

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
