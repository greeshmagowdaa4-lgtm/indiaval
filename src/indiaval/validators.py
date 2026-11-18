import re

_MOBILE = re.compile(r"(?:\+91[\-\s]?|91|0)?[6-9]\d{9}")
_PINCODE = re.compile(r"[1-9]\d{5}")
_PAN = re.compile(r"[A-Z]{5}\d{4}[A-Z]")
_IFSC = re.compile(r"[A-Z]{4}0[A-Z0-9]{6}")
_AADHAAR = re.compile(r"[2-9]\d{11}")

_D = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
    (2, 3, 4, 0, 1, 7, 8, 9, 5, 6), (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
    (4, 0, 1, 2, 3, 9, 5, 6, 7, 8), (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
    (6, 5, 9, 8, 7, 1, 0, 4, 3, 2), (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
    (8, 7, 6, 5, 9, 3, 2, 1, 0, 4), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
)
_P = (
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
    (5, 8, 0, 3, 7, 9, 6, 1, 4, 2), (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
    (9, 4, 5, 3, 1, 2, 6, 8, 7, 0), (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
    (2, 7, 9, 3, 8, 0, 6, 4, 1, 5), (7, 0, 4, 6, 9, 1, 3, 2, 5, 8),
)


def is_valid_mobile(value: str) -> bool:
    """Indian mobile number, with optional +91, 91 or 0 prefix."""
    return bool(_MOBILE.fullmatch(value.strip()))


def is_valid_pincode(value: str) -> bool:
    """6-digit PIN code that doesn't start with 0."""
    return bool(_PINCODE.fullmatch(value.strip()))


def is_valid_pan(value: str) -> bool:
    """PAN format: 5 letters, 4 digits, 1 letter (e.g. ABCDE1234F)."""
    return bool(_PAN.fullmatch(value.strip().upper()))


def is_valid_ifsc(value: str) -> bool:
    """IFSC format: 4 letters, a zero, 6 letters or digits (e.g. SBIN0001234)."""
    return bool(_IFSC.fullmatch(value.strip().upper()))


def is_valid_aadhaar(value: str) -> bool:
    """12-digit Aadhaar number (spaces allowed) with a valid Verhoeff checksum."""
    number = value.replace(" ", "")
    if not _AADHAAR.fullmatch(number):
        return False
    c = 0
    for i, ch in enumerate(reversed(number)):
        c = _D[c][_P[i % 8][int(ch)]]
    return c == 0