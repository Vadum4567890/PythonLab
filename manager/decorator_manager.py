# pylint: disable=too-many-arguments
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=import-error
# pylint: disable=line-too-long
import functools
import logging
import re
import time
import os


class RedundantChargeException(Exception):
    pass


class InvalidModeException(Exception):
    pass


class DecoratorManager:
    """
    The DecoratorManager class provides various decorators that
    can be used to add additional functionality to methods.
    Each decorator performs a specific task, such as printing method information,
    measuring execution time, logging method calls, handling exceptions, and more.
    """

    @staticmethod
    def validate_method_name(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            if not re.match(r'^[a-z_][a-z0-9_]*$', method_name):
                raise ValueError(
                    f"Invalid method name: {method_name}. Method name should follow Python code convention (snake_case).")
            return func(*args, **kwargs)

        return wrapper

    @staticmethod
    def method_history_decorator(func):
        """
        Decorator that logs the history of method invocations.
        """
        file_name = "method_history.txt"

        def wrapper(*args, **kwargs):
            """
            Wrapper function that logs the method name and time of invocation,
            calls the original method, and returns the result.
            """
            with open(file_name, "a", encoding="utf-8") as file:
                file.write("Method name: " + func.__name__ + ", Time: " + str(time.time()) + "\n")
            result = func(*args, **kwargs)
            return result

        return wrapper

    @staticmethod
    def logged(mode):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    error_message = str(e)
                    if mode == 'console':
                        logging.error(error_message)
                    elif mode == 'file':
                        log_file = 'log.txt'
                        if not os.path.exists(log_file):
                            open(log_file, 'a').close()
                        with open(log_file, 'a') as file:
                            file.write(error_message + '\n')
                    else:
                        raise InvalidModeException(f"Invalid mode: {mode}")

            return wrapper

        return decorator
