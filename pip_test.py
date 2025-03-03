from os import system
import subprocess


def pip_test():
    result = subprocess.run("pip -V", shell=True, capture_output=True, text=True)

    if "'pip' is not recognized" in result.stdout:
        system("python -m ensurepip --upgrade")
