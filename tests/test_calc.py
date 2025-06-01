import pytest
from kalkulator import dodaj, dziel

def test_dodaj():
    assert dodaj(2, 3) == 5

def test_dziel():
    assert dziel(10, 2) == 5

def test_dziel_przez_zero():
    with pytest.raises(ZeroDivisionError):
        dziel(10, 0)
