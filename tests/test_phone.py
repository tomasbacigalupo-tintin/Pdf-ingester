import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pdf_ingester.phone import find_phone_numbers


def test_find_phone_numbers():
    text = "Contacto: +54 11 1234-5678 y 011 4321-8765"
    numbers = find_phone_numbers(text, region="AR")
    assert "+541112345678" in numbers
    assert "+541143218765" in numbers
