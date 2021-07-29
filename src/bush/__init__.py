# Author: Patan Musthakheem Khan
# Licence : Apache 2.0
# Version : 0.3 Beta
import os
import sys
from base64 import urlsafe_b64encode, urlsafe_b64decode

from hashlib import sha256
try:
    from Crypto.Cipher import AES
except ImportError:
    AES = None
    print("Pycryptodome Is Not Installed [pip install pycryptodome]")
    sys.exit(1)
new = AES.new


class Bush:
    def __init__(self, key):
        if not isinstance(key, bytes):
            raise ValueError("Key Must Be Bytes")
        key = sha256(key).digest()
        self.__encryption_key = key[:16]
        self.__signing_key = key[16:]

    @classmethod
    def generate_key(cls):
        """
        Generates a random 32 Byte Key
        :return: bytes
        """
        return os.urandom(32)

    def encrypt(self,
                data: bytes):
        """
        Encrypt Data
        :param data: Data Which Want to be encrypted
        :return: Bytes Of Encrypted Data
        """
        if not isinstance(data, bytes):
            raise ValueError("Data Must Be Bytes")
        return self.__encryptor(self.__encryption_key, data)

    def __encryptor(self, key, data):
        self.iv = os.urandom(16)
        cipher = new(
            key=key,
            mode=2,
            iv=self.iv
        )
        padder = self.__padder
        padded_data = padder(data)
        return self.__sign(cipher.encrypt(padded_data))

    def __sign(self, data):
        signed = sha256(data + self.__signing_key).digest()
        return self.__finalize(signed, data, self.iv)

    @staticmethod
    def __finalize(signed_data, cipher_text, iv):
        signed = urlsafe_b64encode(signed_data)
        ciphered = urlsafe_b64encode(cipher_text)
        IV = urlsafe_b64encode(iv)
        final = signed + ciphered + IV
        return final

    def decrypt(self, data):
        if not isinstance(data, bytes):
            raise ValueError("Data Must Be Bytes")
        return self.__decryptor(data)

    def __decryptor(self, data):
        signed = data[:44]
        iv = data[-24:]
        cipher_text = data[44:-24]
        self.__check_signature(cipher_text, signed, self.__signing_key)
        cipher = new(
            key=self.__encryption_key,
            mode=2,
            iv=urlsafe_b64decode(iv)
        )
        unpadder = self.__unpadder
        return unpadder(cipher.decrypt(urlsafe_b64decode(cipher_text)))

    @staticmethod
    def __padder(data: bytes):
        while len(data) % 16 != 0:
            data += b'0'
        return data

    @staticmethod
    def __unpadder(data: bytes):
        return data.rstrip(b'0')

    @staticmethod
    def __check_signature(data: bytes, prev_key: bytes, key) -> bytes:
        sign = sha256(urlsafe_b64decode(data) + key).digest()
        prev_key = urlsafe_b64decode(prev_key)
        assert sign == prev_key, "Cipher-Text is Altered"
        return
