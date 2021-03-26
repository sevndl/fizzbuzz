class FizzBuzz:
    @staticmethod
    def NombreVerificateur(nombre):
        if nombre.isalpha():
            raise(ArgumentError('PAS DE LETTRES'))
        else:
            nombre = int(nombre)
        if nombre <= 0:
            raise(ArgumentError('Le nombre doit être positif.')) 
        if nombre % 5 == 0 and nombre % 3 == 0:
            return 'FizzBuzz'
        if nombre % 3 == 0:
            return "Fizz"
        if nombre % 5 == 0:
            return "Buzz"
        return nombre
    
class ArgumentError(Exception):
    def __init__(self, message):
        super()
        self.message = message