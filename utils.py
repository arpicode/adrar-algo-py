import sys


def stdout_equals(str) -> bool:
    sys.stdout.seek(0)
    return sys.stdout.read(len(str)) == str
