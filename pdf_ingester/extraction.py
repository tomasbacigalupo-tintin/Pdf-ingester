from pathlib import Path
from io import StringIO
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Return the extracted text from a PDF file."""
    return extract_text(str(pdf_path))
