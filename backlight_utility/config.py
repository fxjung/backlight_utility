import dotenv
import os

from enum import Enum
from pathlib import Path

dotenv.load_dotenv()
brightness_path = Path(os.getenv("BRIGHTNESS_PATH"))
max_brightness_path = Path(os.getenv("MAX_BRIGHTNESS_PATH"))
actual_brightness_path = Path(os.getenv("ACTUAL_BRIGHTNESS_PATH"))

min_brightness = 0
max_brightness = int(max_brightness_path.read_text())


class NotificationModes(str, Enum):
    none = "none"
    relative = "relative"
    absolute = "absolute"
