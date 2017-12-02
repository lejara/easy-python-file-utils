import hashlib
from pathlib import Path


def GetSHA1Digest(file):
    data = Path(file).read_text()
    hash = hashlib.sha1()
    hash.update(data.encode('utf-8'))
    return hash.hexdigest()
