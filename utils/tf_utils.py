"""Utils for tensorflow models.
"""

import logging, os


def set_tf_loglevel(level) -> None:
    """Sets the logging level for tensorflow.

    Parameters
    ----------
    level : int

    """
    if level >= logging.FATAL:
        os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    if level >= logging.ERROR:
        os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
    if level >= logging.WARNING:
        os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"
    else:
        os.environ["TF_CPP_MIN_LOG_LEVEL"] = "0"
    logging.getLogger("tensorflow").setLevel(level)
