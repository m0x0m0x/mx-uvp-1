# Main function for typer here

import requests as rq
from selectolax.parser import HTMLParser

app = typer.Typer()


@app.command
def test(name: str):
    print(f"Hello {name}!")
