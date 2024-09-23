from plates import is_valid

def test_too_many_caracters():
    text = 'abcdefghi'
    assert is_valid(text) ==  False

def test_too_few_caracters():
    text = 'a'
    assert is_valid(text) ==  False

def test_start_2_lethers():
    #All vanity plates must start with at least two letters
    text = 'ab'
    assert is_valid(text) ==  True
    text = '1ac'
    assert is_valid(text) ==  False

def test_number_in_the_middle():
    #Numbers cannot be used in the middle of a plate
    text = 'ac1c'
    assert is_valid(text) ==  False
    text = 'acc2d'
    assert is_valid(text) ==  False
    text = 'acc2'
    assert is_valid(text) ==  True

def test_no_periods_spaces_poctuation():
    #No periods, spaces, or punctuation marks are allowed.
    text = 'ac c'
    assert is_valid(text) ==  False
    text = 'ac,c'
    assert is_valid(text) ==  False
    text = 'ac.c'
    assert is_valid(text) ==  False