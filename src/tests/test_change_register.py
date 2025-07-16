from tasks.change_register import to_alternating_case


def test_short_string():
    assert to_alternating_case('Anna') == 'aNNA'
    assert to_alternating_case('IlyaS') == 'iLYAs'
    assert to_alternating_case('PPPP') == 'pppp'
    assert to_alternating_case('CaSe') == 'cAsE'
    assert to_alternating_case('SSStt') == 'sssTT'

def test_long_string():
    assert to_alternating_case('AAAAAAAAAAqq') == 'aaaaaaaaaaQQ'
    assert to_alternating_case('IlyaSS ERTERTRE') == 'iLYAss ertertre'
    assert to_alternating_case('PPPPOOOOPOPOPOPOPOPOP121212') == 'ppppoooopopopopopopop121212'
    assert to_alternating_case('CaSe IN MY HEAD') == 'cAsE in my head'
    assert to_alternating_case('stop DO TRHISA AgaIN') == 'STOP do trhisa aGAin'





    


