from datetime import datetime

# print
# print(print)
# print(id(print))
#
# some = print
# print(some)
# print(id(some))
#
#
# n = 666666666666
# print(id(n), n)
# some(88888888888888)
#
# print(id(55))



# ==============================================================================================
# from typing import Callable
#
#
# def foo() -> int:
#     return 10
#
#
# def foo2(number) -> int:
#     return number + 10
#
#
# def foo3(number, number2) -> int:
#     return number + number2
#
#
# functions = {
#     'foo': foo,
#     'foo2': foo2,
# }
#
# functions_list = [foo, foo2]
#
#
# def call_callable_function_and_mult_100(function: Callable, *args, **kwargs) -> int:
#     print(args)
#     print(kwargs)
#     print(function)
#     result = function(*args, **kwargs)
#     final_result = result * 100
#     print(f'{final_result=}')
#
#     # print(int(0x000002E7A8911D00))
#     # print(0x000002E7A8911D00)
#     # print(int("000002E7A8911D00", 16))
#     return final_result
#
#
# # call_callable_function(functions['foo'])
# # call_callable_function(functions_list[0])
#
# call_callable_function_and_mult_100(foo)
# call_callable_function_and_mult_100(foo2, number=2)
# call_callable_function_and_mult_100(foo3, 2, number2=6)
# ==============================================================================================

from typing import Callable
from functools import wraps

convert_to_dict = False


def converting_to_dict_optional(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        print('before call converting_to_dict_optional')

        result = func(*args, **kwargs)
        print('after call converting_to_dict_optional')
        if convert_to_dict:
            result = {"result": result, "status": "OK"}
        return result

    return inner


def log_decorator(filename = "log.csv") -> Callable:
    def log_decorator2(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            print('before call log_decorator')
            result = func(*args, **kwargs)

            with open(filename, mode='a') as log_file:
                log_file.write(f"{datetime.now()};{func.__name__};{args};{kwargs=};{result}\n")

            print('after call log_decorator')
            return result
        return inner
    return log_decorator2


@log_decorator('foo.log')
@converting_to_dict_optional
# foo = converting_to_dict_optional(foo)
def foo() -> int:
    """bla bla"""
    print(555555555555555555555555555555555555)
    return 10


@converting_to_dict_optional
@log_decorator()
def foo2(number) -> int:
    return number + 10

# print(foo)
print(foo.__name__, 88888888)
print(foo.__doc__)
#
# foo.number = 55
# print(foo.__dict__)


# foo = call_callable(func=foo)
# foo2 = call_callable(func=foo2)
#
# result = foo()
# print(result)
#
# result = foo2(666666666)
# print(result)

r = foo()
print(r)
r2 = foo2(55555)
r2 = foo2(number=2222)
r2 = foo2(55555)
print(r2)