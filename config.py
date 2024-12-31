from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple
import yaml

@dataclass
class TranscriptionConfig:
    input_directory: Path
    output_directory: Path
    language: str = "es-ES"
    chunk_size: int = field(default=60)
    max_workers: int = field(default=4)
    min_confidence: float = field(default=0.8)
    cache_enabled: bool = field(default=True)
    supported_formats: Tuple[str, ...] = ('.wav', '.mp3', '.flac')

    def __post_init__(self):
        if not self.input_directory.exists():
            raise ValueError(f"Input directory {self.input_directory} does not exist")
        self.output_directory.mkdir(parents=True, exist_ok=True)

        if self.chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if self.max_workers <= 0:
            raise ValueError("max_workers must be positive")
        if not 0 <= self.min_confidence <= 1:
            raise ValueError("min_confidence must be between 0 and 1")

        if not self._is_valid_language_code(self.language):
            raise ValueError(f"Invalid language code format: {self.language}")

    @staticmethod
    def _is_valid_language_code(code: str) -> bool:
        parts = code.split('-')
        return (len(parts) == 2 and 
                len(parts[0]) == 2 and
                len(parts[1]) == 2 and
                parts[0].islower() and 
                parts[1].isupper())
def load_config(config_path: str = 'config.yaml') -> TranscriptionConfig:
    if Path(config_path).exists():
        with open(config_path) as f:
            config_data = yaml.safe_load(f)
        return TranscriptionConfig(**config_data)
    return TranscriptionConfig()
