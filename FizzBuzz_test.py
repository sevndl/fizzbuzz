import unittest
from FizzBuzz import FizzBuzz
from FizzBuzz import ArgumentError
class FizzBuzz_test(unittest.TestCase):

    def test_renvoie_le_nombre_4(self):
        nombre = 4
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(nombre,nombreRendu)

    def test_renvoie_le_nombre(self):
        nombre = 7
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(nombre,nombreRendu)

    def test_renvoie_une_erreur_avec_0(self):
        nombre = 0
        with self.assertRaises(ArgumentError):
            FizzBuzz.NombreVerificateur(nombre)

    def test_renvoie_une_erreur_avec_moins1(self):
        nombre = -1
        with self.assertRaises(ArgumentError):
            FizzBuzz.NombreVerificateur(nombre)

    def test_renvoie_une_erreur_si_negatif(self):
        nombre = -10
        with self.assertRaises(ArgumentError):
            FizzBuzz.NombreVerificateur(nombre)

    def test_renvoie_fizz_avec_3(self):
        nombre = 3
        valeurAttendue = 'Fizz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_fizz_avec_multiple_de_3(self):
        nombre = 6
        valeurAttendue = 'Fizz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_buzz_avec_5(self):
        nombre = 5
        valeurAttendue = 'Buzz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_buzz_avec_10(self):
        nombre = 10
        valeurAttendue = 'Buzz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_buzz_avec_multiple_de_5(self):
        nombre = 20
        valeurAttendue = 'Buzz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)
    
    def test_renvoie_FizzBuzz_renvoie_avec_15(self):
        nombre = 15
        valeurAttendue = 'FizzBuzz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_FizzBuzz_renvoie_avec_30(self):
        nombre = 30
        valeurAttendue = 'FizzBuzz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)