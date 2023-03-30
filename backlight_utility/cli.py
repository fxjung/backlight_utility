"""Console script for backlight_utility."""
import typer
import sys
from backlight_utility import backlight


app = typer.Typer()

@app.command()
def main(value: str = typer.Argument(...)):
    match value[0]:
        case '+':
            if value[-1] == '%':
                backlight.increase_brightness(int(value[1:-1].strip()), percent=True)
            else:
                backlight.increase_brightness(int(value[1:].strip()), percent=False)
        case '-':
            if value[-1] == '%':
                backlight.decrease_brightness(int(value[1:-1].strip()), percent=True)
            else:
                backlight.decrease_brightness(int(value[1:].strip()), percent=False)
        case _:
            backlight.set_brightness(int(value.strip()))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
