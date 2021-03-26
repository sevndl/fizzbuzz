import unittest
from FizzBuzz import FizzBuzz
from FizzBuzz import ArgumentError

class FizzBuzz_test(unittest.TestCase):
    def test_renvoie_le_nombre(self):
        nombre = '7'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(nombre,nombreRendu)

    def test_renvoie_une_erreur_avec_0(self):
        nombre = '0'
        with self.assertRaises(ArgumentError):
            FizzBuzz.NombreVerificateur(nombre)

    def test_renvoie_une_erreur_si_negatif(self):
        nombre = '-10'
        with self.assertRaises(ArgumentError):
            FizzBuzz.NombreVerificateur(nombre)

    def test_renvoie_fizz_avec_multiple_de_3(self):
        nombre = '6'
        valeurAttendue = 'Fizz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_buzz_avec_multiple_de_5(self):
        nombre = '20'
        valeurAttendue = 'Buzz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_fizzbuzz_avec_multiple_de_5_et_de_3(self):
        nombre = '45'
        valeurAttendue = 'FizzBuzz'
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(valeurAttendue,nombreRendu)

    def test_renvoie_une_erreur_si_pas_un_nombre(self):
        nombre = "Texte"
        with self.assertRaises(ArgumentError):
            FizzBuzz.NombreVerificateur(nombre)