import re

_MOBILE = re.compile(r"(?:\+91[\-\s]?|91|0)?[6-9]\d{9}")
_PINCODE = re.compile(r"[1-9]\d{5}")
_PAN = re.compile(r"[A-Z]{5}\d{4}[A-Z]")
_IFSC = re.compile(r"[A-Z]{4}0[A-Z0-9]{6}")
_AADHAAR = re.compile(r"[2-9]\d{11}")
_GSTIN = re.compile(r"(0[1-9]|[1-2]\d|3[0-8])[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]")
_GSTIN_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_VEHICLE = re.compile(r"[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}")

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


def is_valid_gstin(value: str) -> bool:
    """15-character GSTIN with a valid checksum character."""
    gstin = value.strip().upper()
    if not _GSTIN.fullmatch(gstin):
        return False
    total = 0
    for i, ch in enumerate(gstin[:14]):
        v = _GSTIN_CHARS.index(ch) * (1 if i % 2 == 0 else 2)
        total += v // 36 + v % 36
    return _GSTIN_CHARS[(36 - total % 36) % 36] == gstin[14]


def is_valid_vehicle_number(value: str) -> bool:
    """Vehicle registration like KA01AB1234 (spaces and hyphens allowed)."""
    number = value.upper().replace(" ", "").replace("-", "")
    return bool(_VEHICLE.fullmatch(number))