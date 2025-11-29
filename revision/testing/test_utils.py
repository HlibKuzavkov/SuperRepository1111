from revision import utils
import pytest

def test_is_valid_email():
    expected = True
    real = utils.is_valid_email('example@mail.com')
    assert expected == real

def test_has_several_at():
    expected = False
    real = utils.is_valid_email('example@@mail.com')
    assert expected == real

def test_has_no_point():
    expected = False
    real = utils.is_valid_email('example@mailcom')
    assert expected == real

def test_no_value():
    expected = False
    real = utils.is_valid_email('')
    assert expected == real

def test_avg_normal_list():
    assert utils.avg([1, 2, 3, 4]) == 2.5

def test_avg_single_element():
    assert utils.avg([10]) == 10

def test_avg_negative_numbers():
    assert utils.avg([-1, -2, -3]) == -2

def test_avg_empty_list():
    with pytest.raises(ValueError):
        utils.avg([])

def test_normal_currency_check():
    assert utils.uah_to_usd(100, 41) == 2.44

def test_wrong_currency():
    with pytest.raises(ValueError):
        utils.uah_to_usd(100, -41)

def test_wrong_currency2():
    with pytest.raises(ValueError):
        utils.uah_to_usd(-100, 41)

def test_large_numbers():
    assert utils.uah_to_usd(1500000, 150) == 10000