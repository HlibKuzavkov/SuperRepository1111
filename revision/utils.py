def is_safe(password: str) -> bool:
    has_digit = False
    has_lower = False
    has_upper = False

    for l in password:
        if l.isdigit():
            has_digit = True
        if l.islower():
            has_lower = True
        if l.isupper():
            has_upper = True
    if len(password)>=8 and has_digit and has_lower and has_upper:
        return True
    else:
        return False


def has_duplicate(your_list: list[int | float | str | bool]) -> bool:
    if not len(your_list) == len(set(your_list)):
        return True
    else:
        return False


def is_warm(temperature: int):
    if temperature > 20:
        return True
    else:
        return False