import unittest

class FizzBuzz_test(unittest.TestCase):

    def test_renvoie_le_nombre(self):
        nombre = 4
        nombreRendu = FizzBuzz.NombreVerificateur(nombre)
        self.assertEqual(nombre,nombreRendu)