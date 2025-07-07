from pathlib import Path
from fastapi import UploadFile


def save_pdf(file: UploadFile, directory: Path = Path("uploads")) -> Path:
    """Save uploaded PDF to disk and return the saved path."""
    directory.mkdir(parents=True, exist_ok=True)
    file_path = directory / file.filename
    with file_path.open("wb") as f:
        f.write(file.file.read())
    return file_path
