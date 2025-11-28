from revision import utils

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