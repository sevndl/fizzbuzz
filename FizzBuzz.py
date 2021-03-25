class FizzBuzz:
    @staticmethod
    def NombreVerificateur(nombre):
        if nombre <= 0:
            raise(ArgumentError())
        if nombre == 3:
            return "Fizz"
        return nombre
    
class ArgumentError(Exception):
    def __init__(self):
        super()