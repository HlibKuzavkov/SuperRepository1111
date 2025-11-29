from os import abort


def is_valid_email(value: str) -> bool:

    if  value.startswith('@') or value.startswith('.') or \
        value.endswith('@') or value.endswith('.'):
        return False

    if value.count('@') != 1:
        return False

    before_at, after_at = value.split('@')

    if not before_at:
        return False

    if '.' not in after_at:
        return False

    sld, tld, *rest = after_at.split('.', 2)

    if not sld or not tld:
        return False
    return True

def avg(values: list[float]) -> float:
    if not values:
        raise ValueError('list can not be empty')
    return round((sum(values)/len(values)), 2)

def uah_to_usd(amount: float, rate: float) -> float:
    """
    Конвертує гривні у долари.
    Якщо сума або курс <= 0 — підіймає ValueError.
    """
    if amount<=0 or rate <=0:
        raise ValueError('values cant be negative or 0')
    return round((amount/rate), 2)