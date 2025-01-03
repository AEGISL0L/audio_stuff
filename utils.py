import os
import json
from datetime import datetime
from typing import Dict
from config import TranscriptionConfig

def format_transcription(text: str) -> str:
    """Applies basic formatting rules to a raw transcription.

    A mapping of common markers is replaced for clarity:
        - "  "  -> " / "  (short pauses)
        - "   " -> " // " (long pauses)
        - "[inaudible]" -> "(...)"
        - etc.

    Args:
        text (str): The raw transcription text.

    Returns:
        str: The formatted transcription.
    """
    formatting_rules = {
        "  ": " / ",  # Short pauses
        "   ": " // ", # Long pauses
        "[inaudible]": "(...)",
        "...": "...",
        "[": "[",
        "]": "]"
    }
    
    formatted_text = text
    for pattern, replacement in formatting_rules.items():
        formatted_text = formatted_text.replace(pattern, replacement)
    return formatted_text

def save_metadata(audio_file_path: str, transcription_stats: Dict) -> None:
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

def is_valid_language_code(code: str) -> bool:
    """Validate language code format (e.g. 'en-US', 'es-ES')"""
    parts = code.split('-')
    return (len(parts) == 2 and 
            len(parts[0]) == 2 and
            len(parts[1]) == 2 and
            parts[0].islower() and 
            parts[1].isupper())
