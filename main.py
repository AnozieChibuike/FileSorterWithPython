from OS import *
import platform
import sys

def main():
    os = platform.system()
    if os == 'Linux':
        linux()
    elif os=='Windows' or os=="Microsoft":
        windows()

if __name__ == "__main__":
    main()