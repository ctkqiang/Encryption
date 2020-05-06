#!/usr/bin/env python
# AES Symmetric Encryption
import base64
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend as _default_backend
from cryptography.hazmat.primitives import hashes as _hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as _PBKDF2HMAC

class __AES_Algorithm:
      __salt = b'salt_'
      __key = Fernet.generate_key()
      __user_input = bytes(input("[Input]: "), "utf8")

      @staticmethod
      def main():
            if __user_input.find("b'"):
                  __decryption()
            else:
                  __encryption()

      @staticmethod
      def __decryption():
            print("aa")

      @staticmethod
      def __encryption():
            _KDF = _PBKDF2HMAC(
                  algorithm = _hashes.SHA256(),
                  length = 32,
                  salt = __salt,
                  iteration = 100000,
                  backend = _default_backend()
            )
            __encrypted_String = __user_input.encode() # Convert to `bytes[]`
            __key = base64.urlsafe_b64decode(_KDF.derive(__encrypted_String))
            __file = open("exported_keys/_crypto_key.key", "wb")
            __file.write("Key:", __key, "\n", "User Input: ", __user_input, "\n", "Encrypted: ", __encrypted_String)
            __file.close()

if __name__ == "__main__":
      __AES_Algorithm.main()