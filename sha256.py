import hashlib
def create_hash(msg):
    sha256_hash = hashlib.sha256(msg.encode('utf-8')).digest()
    return sha256_hash

msg = "This is a secret message"
print("SHA-256 Hash:", create_hash(msg=msg).hex())