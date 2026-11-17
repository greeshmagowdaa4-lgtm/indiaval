from indiaval import (
    is_valid_mobile,
    is_valid_pincode,
    is_valid_pan,
    is_valid_ifsc,
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