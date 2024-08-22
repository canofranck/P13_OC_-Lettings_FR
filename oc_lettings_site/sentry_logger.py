import logging


def sentry_log(error_type: str = "", error_message: str = ""):
    """log to sentry"""

    if error_type == "exception":
        logging.exception(error_message)
    else:
        logging.error(error_message)
