from rich.traceback import install
from src.com1 import url

install(show_locals=True)


def main():
    print("Testing Typer")


if __name__ == "__main__":
    main()
    url("www.femscat.com")
