from tasks.get_character_from_ascii_value import get_char


def test_get_char_basic():    
    assert get_char(97) == 'a'
    assert get_char(109) == 'm'
    assert get_char(122) == 'z'

    assert get_char(65) == 'A'
    assert get_char(77) == 'M'
    assert get_char(90) == 'Z'

    assert get_char(48) == '0'
    assert get_char(53) == '5'
    assert get_char(57) == '9'

    assert get_char(32) == ' '
    assert get_char(33) == '!'
    assert get_char(46) == '.'
    assert get_char(63) == '?'

def test_get_char_extended():
    assert get_char(128) != ''
    assert get_char(255) != ''

def test_get_char_edge_cases():
    assert get_char(0) != ''
    assert get_char(31) != ''





    


