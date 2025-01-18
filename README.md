

---

# 📘 API Documentation

Welcome to the **ErApi**! This library allows you to easily interact with the API using both **synchronous** and **asynchronous** options.

## Installation
To get started, make sure you have the library installed:
```bash
pip3 install ApiNyaEr
```

## Usage
- **Synchronous usage**: Import the library with:
```python
from ApiNyaEr.sync import apinya
```
- **Asynchronous usage**: Import the library with:
```python
from ApiNyaEr import apinya
```

Below, we’ll cover each function, providing examples and expected results so you can get started quickly! Let’s dive in 🚀

## Status

| Function           | Status |
|--------------------|--------|
| [1. Apainier](#1-apainier) | ❌


## 🎓 How to Use Each Function

### 1. Apainier

**Description**:
Decode the Base64 encoded bytes-like object or ASCII string s.

**Description**:
Optional altchars must be a bytes-like object or ASCII string of length 2 which specifies the alternative alphabet used instead of the '+' and '/' characters.

**Description**:
The result is returned as a bytes object.  A binascii.Error is raised if s is incorrectly padded.

**Description**:
If validate is False (the default), characters that are neither in the normal base-64 alphabet nor the alternative alphabet are discarded prior to the padding check.  If validate is True, these non-alphabet characters in the input result in a binascii.Error. For more information about the strict base64 check, see:

**Description**:
https://docs.python.org/3.11/library/binascii.html#binascii.a2b_base64

```python
from ApiNyaEr import apinya

result = await apinya.apainier(s='Tidur', altchars=None, validate=False)
print(result)
```

#### Expected Output

```text
Invalid base64-encoded string: number of data characters (5) cannot be 1 more than a multiple of 4
```


This Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)