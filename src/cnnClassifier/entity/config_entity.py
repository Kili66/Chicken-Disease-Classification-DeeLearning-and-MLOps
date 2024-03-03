from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    #returns types and get par from yaml 
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path