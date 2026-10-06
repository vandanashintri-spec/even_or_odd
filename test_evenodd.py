from evenodd import even_odd

def test_even_no():
    assert even_odd(40) == "Even"

def test_odd_no():
    assert even_odd(1)  == "Odd"