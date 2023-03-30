import logging
from backlight_utility import config

log = logging.getLogger(__name__)


def get_current_brightness() -> int:
    return int(config.actual_brightness_path.read_text())


def set_brightness(value: float | int):
    # make sure that the value is in the valid range
    value = int(round(min(max(config.min_brightness, value), config.max_brightness), 0))
    log.info(f"Setting brightness to {value}")
    config.brightness_path.write_text(f"{value}")


def get_fractional_brightness(fraction: float) -> float:
    return (
        config.min_brightness
        + (config.max_brightness - config.min_brightness) * fraction
    )


def get_brightness_fraction(value: int):
    return value / (config.max_brightness - config.min_brightness)


def set_relative_brightness_by_value(value: float):
    set_brightness(get_current_brightness() + value)


def set_relative_brightness_by_fraction(fraction: float):
    set_brightness(
        get_current_brightness()
        + (config.max_brightness - config.min_brightness) * fraction
    )
