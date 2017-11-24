import hashlib
from pathlib import Path


def GetMD5Digest(file):
    data = Path(file).read_text()
    hash = hashlib.md5()
    hash.update(data.encode('utf-8'))
    return hash.hexdigest()
