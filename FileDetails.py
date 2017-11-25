import sys
import os


def getfilename(file):
    filename = os.path.basename(file)
    return filename


def getfilesize(file):
    filesize = os.path.getsize(file)
    return filesize