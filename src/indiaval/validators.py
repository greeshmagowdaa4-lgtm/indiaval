import re

_MOBILE = re.compile(r"(?:\+91[\-\s]?|91|0)?[6-9]\d{9}")
_PINCODE = re.compile(r"[1-9]\d{5}")
_PAN = re.compile(r"[A-Z]{5}\d{4}[A-Z]")
_IFSC = re.compile(r"[A-Z]{4}0[A-Z0-9]{6}")


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