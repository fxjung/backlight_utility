from backlight_utility import config


def get_current_brightness() -> int:
    return int(config.brightness_path.read_text())


def set_brightness(value: int):
    # TODO incorporate max/min values
    value = min(max(config.min_brightness, value), config.max_brightness)
    config.brightness_path.write_text(f'{value}')


def increase_brightness(value: int, percent:bool = False):
    value = abs(value)
    if percent:
        set_brightness(get_current_brightness() * (1+value // 100))
    else:
        set_brightness(get_current_brightness() + value)


def decrease_brightness(value: int, percent:bool = False):
    value = abs(value)
    if percent:
        set_brightness(get_current_brightness() * (1-value // 100))
    else:
        set_brightness(get_current_brightness() - value)

