import FileDetails

import MD5_digest

path = 'data/mydata.txt'


def test_checkReturnHex():
    r = MD5_digest.GetMD5Digest(path)
    assert(int(r, 16))


def test_checkFileSize():
    r = FileDetails.getfilesize(path)
    assert (r == 43)


def test_checkNoPath():
    r = FileDetails.getfilename(path)
    assert(r.find('/') == -1)

