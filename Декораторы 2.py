
from inspect import getcallargs
import datetime
import time

def logging_decorator(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res: dict = {}
            res = {"name": func.__name__,
                              "arguments": getcallargs(func, *args, **kwargs),
                              "call_time": datetime.datetime.now(),
                              "result": func(*args, **kwargs)
                     }

            logger.append(res)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

logger = []  # этот словарь будет хранить наш "лог"

@logging_decorator(logger)  # в аргументы фабрики декораторов подается логгер
def test_simple(a, b=2):
    return 127

test_simple(1)  # при вызове функции в список logger должен добавиться словарь с
                # информацией о вызове функции

print(logger)
