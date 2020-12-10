import hashlib
salt = "dsfdsfsdfvdsvdsv"
def get_hash(text):
    result = hashlib.md5(text.encode())
    return result.hexdigest()

