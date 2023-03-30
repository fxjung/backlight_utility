import subprocess
import logging


log = logging.getLogger(__name__)


def send_notification(msg: str):
    """
    Send notification using `notify-send`.

    Parameters
    ----------
    msg
        Message to send.
    """
    cmd = ["notify-send", "--expire-time=500", msg]
    subprocess.run(cmd)
    log.debug(f'Sent notification "{msg}"')
