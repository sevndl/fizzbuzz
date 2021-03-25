class FizzBuzz:
    @staticmethod
    def NombreVerificateur(nombre):
        if nombre == 0:
            raise(ArgumentError())
        elif nombre == -1:
            raise(ArgumentError())
        return nombre
    
class ArgumentError(Exception):
    def __init__(self):
        super()