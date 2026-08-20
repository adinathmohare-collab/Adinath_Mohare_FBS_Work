import hashlib
import secrets


def hash_pin(pin):
    salt = secrets.token_bytes(16)
    pin_hash = hashlib.pbkdf2_hmac(
        "sha256",
        pin.encode(),
        salt,
        100000
    )
    return pin_hash.hex(), salt.hex()


def verify_pin(pin, stored_hash, stored_salt):
    salt = bytes.fromhex(stored_salt)
    pin_hash = hashlib.pbkdf2_hmac(
        "sha256",
        pin.encode(),
        salt,
        100000
    )
    return secrets.compare_digest(
        pin_hash.hex(),
        stored_hash
    )