from matushell_cli.bin.app import App
from matushell_cli.bin.types import Flag

app = App(name="Matushell CLI", description="CLI application for matushell")


@app.command(name="hello", description="Prints hello", alias="h")
def hello_command():
    print("hello")


@app.command(
    name="print",
    description="Prints text into console",
    alias="p",
    flags=[Flag(name="--text", description="Text", type=str, alias="-t")],
)
def print_text(text: str | None) -> None:
    if text is None:
        raise Exception("Text must be included with --text flag")

    print(text)


def main():
    app.run()
