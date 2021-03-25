import unittest
from FizzBuzz import FizzBuzz

class FizzBuzz_test(unittest.TestCase):

    def test_renvoie_le_nombre_4(self):
        nombre = 4
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(nombre,nombreRendu)