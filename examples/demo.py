from indiaval import (
    is_valid_pan,
    is_valid_aadhaar,
    is_valid_gstin,
    is_valid_ifsc,
    is_valid_vehicle_number,
)

print("PAN        ABCDE1234F      ->", is_valid_pan("ABCDE1234F"))
print("PAN        ABCD12345F      ->", is_valid_pan("ABCD12345F"))
print("Aadhaar    234567890124    ->", is_valid_aadhaar("234567890124"))
print("Aadhaar    234567890125    ->", is_valid_aadhaar("234567890125"))
print("GSTIN      27AAPFU0939F1ZV ->", is_valid_gstin("27AAPFU0939F1ZV"))
print("IFSC       SBIN0001234     ->", is_valid_ifsc("SBIN0001234"))
print("Vehicle    KA01AB1234      ->", is_valid_vehicle_number("KA01AB1234"))