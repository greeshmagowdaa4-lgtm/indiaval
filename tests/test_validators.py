from indiaval import (
    is_valid_mobile,
    is_valid_pincode,
    is_valid_pan,
    is_valid_ifsc,
    is_valid_aadhaar,
)


def test_mobile():
    assert is_valid_mobile("9876543210")
    assert is_valid_mobile("+91 9876543210")
    assert not is_valid_mobile("1234567890")
    assert not is_valid_mobile("98765")


def test_pincode():
    assert is_valid_pincode("560001")
    assert not is_valid_pincode("060001")
    assert not is_valid_pincode("56001")


def test_pan():
    assert is_valid_pan("ABCDE1234F")
    assert not is_valid_pan("ABCD12345F")


def test_ifsc():
    assert is_valid_ifsc("SBIN0001234")
    assert not is_valid_ifsc("SBIN1001234")


def test_aadhaar():
    assert is_valid_aadhaar("234567890124")
    assert is_valid_aadhaar("2345 6789 0124")
    assert not is_valid_aadhaar("234567890125")  # wrong checksum
    assert not is_valid_aadhaar("123456789012")  # starts with 1
    assert not is_valid_aadhaar("23456789")      # too short