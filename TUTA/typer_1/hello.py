# Main function for typer here

from rich.console import Console
from rich.panel import Panel
from rich import print as rprint  # For rprinting
import requests as rq
import typer as ty
from selectolax.parser import HTMLParser
from src.ban1 import banner

app = ty.Typer()


@app.command()
def url(url: str):
    rprint("Hello PantyBoy!")
    rez1 = rq.get(url)
    rprint(rez1.headers)
    rprint(rez1.status_code)

    with open("output.txt", "w") as f:
        f.write(rez1.text)


@app.command()
def banr():
    """print panty banner"""
    banner("Fuc")


if __name__ == "__main__":
    app()
