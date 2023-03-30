import dotenv
import os

from pathlib import Path

dotenv.load_dotenv()
brightness_path = Path(os.getenv("BRIGHTNESS_PATH"))
max_brightness_path = Path(os.getenv("MAX_BRIGHTNESS_PATH"))

min_brightness = 0
max_brightness = int(max_brightness_path.read_text())
