import logging
from backlight_utility import config

log = logging.getLogger(__name__)


def get_current_brightness() -> int:
    """
    Get absolute value of the current brightness

    Returns
    -------
    brightness
    """
    return int(config.actual_brightness_path.read_text())


def set_brightness(value: float | int):
    """
    Set absolute brightness value. Value gets adjusted so that
    min_brightness < value < max_brightness is fulfilled.

    Parameters
    ----------
    value
        Absolute brightness value
    """
    # make sure that the value is in the valid range
    value = int(round(min(max(config.min_brightness, value), config.max_brightness), 0))

    log.info(f"Setting brightness to {value}")
    config.brightness_path.write_text(f"{value}")


def get_fractional_brightness(fraction: float) -> float:
    """
    Get the absolute brightness value for the given fraction.

    Parameters
    ----------
    fraction
        Fraction of the brightness from 0 to 1.

    Returns
    -------
    absolute brightness
    """
    return (
        config.min_brightness
        + (config.max_brightness - config.min_brightness) * fraction
    )


def get_brightness_fraction(value: int):
    """
    Get the fraction of the brightness for the given absolute value.
    Parameters
    ----------
    value
        Absolute brightness value

    Returns
    -------
    brightness fraction from 0 to 1
    """
    return value / (config.max_brightness - config.min_brightness)


def set_relative_brightness_by_value(value: float):
    """
    Increase or decrease the brightness by an absolute value delta.

    Parameters
    ----------
    value
        Value to add to the current absolute brightness (may be negative)
    """
    set_brightness(get_current_brightness() + value)


def set_relative_brightness_by_fraction(fraction: float):
    """
    Increase or decrease the brightness by a fractional value delta.

    Parameters
    ----------
    fraction
        Fraction of the total brightness range to add to the
        current brightness (may be negative)
    """
    set_brightness(
        get_current_brightness()
        + (config.max_brightness - config.min_brightness) * fraction
    )
