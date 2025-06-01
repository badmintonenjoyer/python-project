from kalkulator import dodaj, dziel

def test_dodaj_i_dziel():
    suma = dodaj(4, 6)
    wynik = dziel(suma, 2)
    assert wynik == 5
