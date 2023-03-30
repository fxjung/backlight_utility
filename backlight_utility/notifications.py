import subprocess
import logging


log = logging.getLogger(__name__)


def send_notification(msg: str):
    cmd = ["notify-send", "--expire-time=500", msg]
    subprocess.run(cmd)
    log.debug(f'Sent notification "{msg}"')
