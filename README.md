# Bush Encryption
## Installation
```commandline
pip install Bush
```
## Usage
### Encrypting
```python
from bush import Bush
cipher = Bush(b"Key")
cipher.encrypt(b"Hello, World!")
# Output
"""
b'j11CQjeAKt5EnNh9cBmVmu0ijb9dorK-vie95zhpyRU=JO4YlVWp_HwEjnKbZZp_zg==qojd6BXjI9Zyc_OHySgRkg=='
"""
```
### Decrypting
```python
from bush import Bush
cipher = Bush(b"Key")
cipher.decrypt("b'j11CQjeAKt5EnNh9cBmVmu0ijb9dorK-vie95zhpyRU=JO4YlVWp_HwEjnKbZZp_zg==qojd6BXjI9Zyc_OHySgRkg=='")
# Output
"""
b'Hello, World!'
"""
```
## Algorithm Overview
```
This Algorithm is inspired From Fernet which uses AES
The Encrypted Cipher Text changes every time you run the code
because of change in IV (Initializing Vector) Which is generated from
OS and it is embedded in the cipher text as well!
And It uses Sha256 for making sure that the data is not altered in any manners
And the Sha256 Digest is also embedded in the cipher text as well.
Which Makes This Algorithm A Bit Different From Other Algorithms
```
