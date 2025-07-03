from tasks.palindrome import is_palindrome

def test_short_palindrome():
    assert is_palindrome('Anna') == True
    assert is_palindrome('Okko') == True
    assert is_palindrome('Azza') == True
    assert is_palindrome('OOOO') == True
    assert is_palindrome('TEET') == True
    assert is_palindrome('KIIK') == True


def test_long_palindrome():
    assert is_palindrome('aaaaaazzzaaaaaa') == True
    assert is_palindrome('leeeeeeel') == True
    assert is_palindrome('kiaaaaaaik') == True
    assert is_palindrome('AooooooooooooooooooooooooA') == True
    assert is_palindrome('TEEeeeeeeeeeeeeeeeeeeeeeeeeeT') == True

def test_negative():
    assert is_palindrome('aaaaaazzzaaaa') == False
    assert is_palindrome('leeeeee') == False
    assert is_palindrome('kiaaaaaai') == False
    assert is_palindrome('Aoooooooooooooooooooo') == False
    assert is_palindrome('TEEeeeeeeeeeeeeeeeeeeeeeee') == False
    


