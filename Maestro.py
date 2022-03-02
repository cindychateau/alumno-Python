from Persona import Persona

class Maestro(Persona):

    def __init__(self, nombre, apellido, email, curso):
        super().__init__(nombre, apellido)
        self.email = email
        self.curso = curso