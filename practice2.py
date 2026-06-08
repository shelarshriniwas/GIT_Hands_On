import hashlib

data = "This is data"

hash_value = hashlib.md5(data).hexdigest()

print(hash_value)