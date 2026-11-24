# indiaval

![Tests](https://github.com/greeshmagowdaa4-lgtm/indiaval/actions/workflows/tests.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/indiaval)](https://pypi.org/project/indiaval/)
![Python](https://img.shields.io/pypi/pyversions/indiaval)

Simple Python validators for common Indian data formats: mobile numbers, PIN codes, PAN, IFSC codes, Aadhaar numbers, GSTIN and vehicle registration numbers.

## Installation

```bash
pip install indiaval
```

To work on the code locally:

```bash
git clone https://github.com/greeshmagowdaa4-lgtm/indiaval.git
cd indiaval
pip install -e .
```

## Usage

```python
from indiaval import (
    is_valid_mobile,
    is_valid_pincode,
    is_valid_pan,
    is_valid_ifsc,
    is_valid_aadhaar,
    is_valid_gstin,
    is_valid_vehicle_number,
)

is_valid_mobile("+91 9876543210")         # True
is_valid_pincode("560001")                # True
is_valid_pan("ABCDE1234F")                # True
is_valid_ifsc("SBIN0001234")              # True
is_valid_aadhaar("234567890124")          # True
is_valid_gstin("27AAPFU0939F1ZV")         # True
is_valid_vehicle_number("KA01AB1234")     # True

is_valid_pincode("060001")                # False (can't start with 0)
```

## Demo

A runnable example is in [examples/demo.py](examples/demo.py):

```bash
python examples/demo.py
```

## Validators

| Function | Checks |
|----------|--------|
| `is_valid_mobile` | 10-digit number starting with 6-9, optional `+91`, `91` or `0` prefix |
| `is_valid_pincode` | 6 digits, first digit not 0 |
| `is_valid_pan` | 5 letters, 4 digits, 1 letter |
| `is_valid_ifsc` | 4 letters, a zero, then 6 letters or digits |
| `is_valid_aadhaar` | 12 digits, first digit 2-9, valid Verhoeff checksum |
| `is_valid_gstin` | 15-character GSTIN with a valid state code and checksum |
| `is_valid_vehicle_number` | State code, 2 digits, 1-3 letters, 4 digits (e.g. `KA01AB1234`) |

These check the **format** only. They don't confirm that a number or code actually exists.

## Running tests

```bash
pip install pytest
python -m pytest
```

## License

MIT. See [LICENSE](LICENSE).