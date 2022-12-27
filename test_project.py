from project import validate_cell


def test_lower():
    assert validate_cell("b3") == True
    assert validate_cell("h8") == True
    assert validate_cell("j10") == True




def test_invalid():
    assert validate_cell("M3") == False
    assert validate_cell("A11") == False
    assert validate_cell("11") == False
    assert validate_cell("Cat") == False
    assert validate_cell("A0") == False

def test_valid():
    assert validate_cell("J7") == True
    assert validate_cell("B8") == True
    assert validate_cell("A1") == True