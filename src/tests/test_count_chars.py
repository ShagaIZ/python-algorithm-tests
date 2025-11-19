from tasks.count_chars import count_chars


def test_short_string():
    assert count_chars('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_chars('test') == {'t': 2, 'e': 1, 's': 1}
    assert count_chars('aabbcc') == {'a': 2, 'b': 2, 'c': 2}
    assert count_chars('abc') == {'a': 1, 'b': 1, 'c': 1}
    assert count_chars('') == {}

def test_long_string():
    assert count_chars('abracadabra') == {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
    assert count_chars('mississippi') == {'m': 1, 'i':              4, 's': 4, 'p': 2}
    assert count_chars('thequickbrownfoxjumpsoverthelazydog') == { 't': 2, 'h': 2, 'e': 3, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
    assert count_chars('aaaaaaaaaabbbbbbbbbbcccccccccc') == {'a': 10, 'b': 10, 'c': 10}
    assert count_chars('12345678901234567890') == {'1': 2           , '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '0': 2} 




    


