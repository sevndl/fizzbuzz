class FizzBuzz:
    @staticmethod
    def NombreVerificateur(nombre):
        if nombre == 0 or nombre == -1:
            raise(ArgumentError())
        elif nombre < 0:
            raise(ArgumentError())
        return nombre
    
class ArgumentError(Exception):
    def __init__(self):
        super()