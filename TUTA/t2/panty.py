from src.p1 import bann1
from src.w1 import func1
from rich.traceback import install

install(show_locals=True)


def main():
    bann1("Hello, World!")
    func1()


if __name__ == "__main__":
    main()
