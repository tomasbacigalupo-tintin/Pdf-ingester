import re
from typing import List
import phonenumbers

PHONE_REGEX = re.compile(r"\+?\d[\d\s()-]{7,}\d")


def find_phone_numbers(text: str, region: str = "AR") -> List[str]:
    """Find and normalize phone numbers in given text."""
    numbers = []
    for match in PHONE_REGEX.findall(text):
        try:
            parsed = phonenumbers.parse(match, region)
            if phonenumbers.is_valid_number(parsed):
                numbers.append(phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164))
        except phonenumbers.NumberParseException:
            continue
    return numbers
