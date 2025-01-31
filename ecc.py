from ecdsa import SigningKey, NIST256p, VerifyingKey
from ecdsa.util import sigencode_der, sigdecode_der
import hashlib

# Private Key Generation
def generate_private_key():
    private_key = SigningKey.generate(curve=NIST256p)
    return private_key

# Public Key Generation
def generate_public_key(private_key):
    public_key = private_key.get_verifying_key()
    return public_key

# SHA-256 Hashing
def create_hash(message):
    sha256_hash = hashlib.sha256(message.encode('utf-8')).digest()
    return sha256_hash

# Message Signing
def sign_message(private_key, message):
    hash_message = create_hash(message)
    signature = private_key.sign(hash_message, sigencode=sigencode_der)
    return signature

# Signature Verification
def verify_signature(public_key, message, signature):
    hash_message = create_hash(message)
    is_valid = public_key.verify(signature, hash_message, sigdecode=sigdecode_der)
    return is_valid

# Main Code
def main():
    message = "This is a secret message."

    # Generate private and public keys
    private_key = generate_private_key()
    public_key = generate_public_key(private_key)

    print("Private Key (Hex):", private_key.to_string().hex())
    print("Public Key (Hex):", public_key.to_string().hex())

    # Sign the message
    signature = sign_message(private_key, message)
    print("\nSignature (DER format):", signature.hex())

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print("\nSignature valid:", is_valid)

if __name__ == "__main__":
    main()
