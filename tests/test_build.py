import sys
sys.path.insert(0, '../src')

import FileDetails
import MD5_digest

path = "../data/mydata.txt"


def test_checkReturnString():
    r = FileDetails.getfilename(path)
    assert (isinstance(r, str))

def test_checkNoPath():
    r = FileDetails.getfilename(path)
    assert(r.find('/') == -1)

def test_checkReturnHex():
    r = MD5_digest.GetMD5Digest(path)
    assert(int(r, 16))

