"""
Utility module providing robust Fernet encryption and OS-level keystore integration for credentials.
"""

import logging
import base64
import keyring
from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)

SERVICE_NAME = "QtDBExplorer"
KEY_ACCOUNT = "fernet_encryption_key"

_cipher_suite = None

def get_or_create_key() -> bytes:
    """
    Retrieves the encryption key from the OS secure keystore.
    If it doesn't exist, generates a new one and stores it.
    """
    try:
        encoded_key = keyring.get_password(SERVICE_NAME, KEY_ACCOUNT)
        if not encoded_key:
            logger.info("No encryption key found in OS keystore. Generating a new secure key.")
            key = Fernet.generate_key()
            encoded_key = key.decode("utf-8")
            keyring.set_password(SERVICE_NAME, KEY_ACCOUNT, encoded_key)
        
        return encoded_key.encode("utf-8")
    except Exception as e:
        logger.error(f"Failed to access OS keystore: {e}")
        # Fallback to a padded 32-byte key if keystore is fundamentally broken
        return base64.urlsafe_b64encode(b"QtDBExplorer_Fallback_Key_123456")

def _get_cipher() -> Fernet:
    global _cipher_suite
    if _cipher_suite is None:
        key = get_or_create_key()
        _cipher_suite = Fernet(key)
    return _cipher_suite

def encrypt_password(plain_text: str) -> str:
    """Encrypts a plaintext string into a safe ascii string using Fernet."""
    if not plain_text:
        return ""
    cipher = _get_cipher()
    encrypted_bytes = cipher.encrypt(plain_text.encode("utf-8"))
    return encrypted_bytes.decode("utf-8")

def decrypt_password(encrypted_text: str) -> str:
    """Decrypts a previously encrypted Fernet string back into plaintext."""
    if not encrypted_text:
        return ""
    cipher = _get_cipher()
    try:
        decrypted_bytes = cipher.decrypt(encrypted_text.encode("utf-8"))
        return decrypted_bytes.decode("utf-8")
    except Exception as e:
        logger.error(f"Failed to decrypt password: {e}")
        return ""
