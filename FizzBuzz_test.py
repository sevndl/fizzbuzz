import unittest
from FizzBuzz import FizzBuzz
from FizzBuzz import ArgumentError
class FizzBuzz_test(unittest.TestCase):

    def test_renvoie_le_nombre_4(self):
        nombre = 4
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(nombre,nombreRendu)

    def test_renvoie_le_nombre(self):
        nombre = 6
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