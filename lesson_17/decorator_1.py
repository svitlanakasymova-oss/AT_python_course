"""Напишіть декоратор, який логує аргументи та результати викликаної функції."""


import logging

logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
logger = logging.getLogger("log_event")


def decorator_logging(func):
    def wrapper(a, b):
        logger.info(f"Received arguments: {a} and {b}")
        res = func(a, b)
        logger.info(f"Result: {res}")
        return res
    return wrapper


@decorator_logging
def get_sum(a, b):
    return a + b