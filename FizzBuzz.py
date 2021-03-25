class FizzBuzz:
    @staticmethod
    def NombreVerificateur(nombre):
        if nombre <= 0:
            raise(ArgumentError())
        if nombre % 3 == 0:
            return "Fizz"
        if nombre % 5 == 0:
            return "Buzz"
        if nombre == 15:
            return "FizzBuzz"
        return nombre
    
class ArgumentError(Exception):
    def __init__(self):
        super()