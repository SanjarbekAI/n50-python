"""
Lesson 4: Exception and practice
    Exceptions
    Custom exceptions
    Exception handling best practices
    Logging
"""
from app import FunctionExecutionError
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="app.log")

logger = logging.getLogger(__name__)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            message = f"Function: {func.__name__} args: {args} kwargs: {kwargs} result: {result}"
            logger.info(message)

            return result
        except Exception as e:
            message = f"Function: {func.__name__} args: {args} kwargs: {kwargs} exception: {e}"
            logger.error(message)
            raise FunctionExecutionError(message=message)
    return wrapper
