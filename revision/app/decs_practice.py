from functools import wraps

def round_result(ndigits: int):
    def decorator(func):
        @wraps(func)
        def round_number(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == any([int, float]):
                return round(result, ndigits)
            return result
        return round_number
    return decorator

@round_result(3)
def round_func_result(num1, num2):
    return num1/num2

@round_result(3)
def get_list():
    return [2,4,6,7]

print(round_func_result(10, 3))
print(get_list())


