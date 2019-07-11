import logging

logger = logging.getLogger(__name__)

def some_f():
    logger.debug("Debug from module root logger")


def raised():
    try:
        raise IOError("Some error")
    except IOError:
        # if you log exception like this then you shall not re-raise it. It causes multiple error messages in log
        logging.exception("shit happened here %s %s ", 42, "hello")
