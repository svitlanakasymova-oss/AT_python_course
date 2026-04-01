"""Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції."""


import logging

logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
logger = logging.getLogger("log_event")


def decorate_errors(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            logger.error(e)
    return wrapper


@decorate_errors
def raise_error():
    raise Exception("This is test error")