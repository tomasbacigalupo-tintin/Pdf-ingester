from pathlib import Path
from fastapi import UploadFile

from .ingestion import save_pdf
from .extraction import extract_text_from_pdf
from .phone import find_phone_numbers


async def process_upload(file: UploadFile) -> list[str]:
    """Save PDF, extract text and return phone numbers found."""
    pdf_path = save_pdf(file)
    text = extract_text_from_pdf(pdf_path)
    return find_phone_numbers(text)
