"""Console script for backlight_utility."""
import typer
import sys
import logging
from backlight_utility import backlight
from backlight_utility.config import NotificationModes
from backlight_utility.notifications import send_notification

log = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def set(
    value: float = typer.Argument(...),
    percent: bool = typer.Option(True, "--percent/--value"),
    relative: bool = typer.Option(False, "--relative/--absolute"),
    notification: NotificationModes = typer.Option(
        NotificationModes.none, case_sensitive=False
    ),
):
    if percent:
        if relative:
            backlight.set_relative_brightness_by_fraction(value / 100)
        else:
            backlight.set_brightness(backlight.get_fractional_brightness(value / 100))
    if not percent:
        if relative:
            backlight.set_relative_brightness_by_value(value)
        else:
            backlight.set_brightness(value)

    if notification == NotificationModes.relative:
        send_notification(
            f"Set brightness to {round(backlight.get_brightness_fraction(backlight.get_current_brightness()) * 100, 0):g} %"
        )
    elif notification == NotificationModes.absolute:
        send_notification(f"Set brightness to {backlight.get_current_brightness():g}")


@app.command()
def get(
    percent: bool = typer.Option(True, "--percent/--value"),
):
    if percent:
        print(
            f"{round(backlight.get_brightness_fraction(backlight.get_current_brightness()) * 100, 0):g} %"
        )
    else:
        print(backlight.get_current_brightness())


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
