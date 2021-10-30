import sys


def stdout_equals(str) -> str:
    sys.stdout.seek(0)
    return sys.stdout.read(len(str)) == str
