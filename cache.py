
class TranscriptionCache:
    """Manages caching of transcriptions to avoid reprocessing.
    
    Attributes:
        cache_dir (Path): The directory where cached transcriptions will be stored.
    """
    
    def __init__(self, cache_dir: Path):
        """Initializes the TranscriptionCache with the given cache directory.
        
        Args:
            cache_dir (Path): Directory to store cache files.
        """
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)