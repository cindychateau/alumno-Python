from Persona import Persona

class Estudiante(Persona):
    listaEstudiantes = []
    def __init__(self, nombre, apellido, id, curso):
        super().__init__(nombre, apellido)
        self.id = id
        self.curso = curso
        Estudiante.listaEstudiantes.append(self)
    
    @classmethod
    def imprimeEstudiantes(cls):
        for estudiante in cls.listaEstudiantes:
            estudiante.imprime()
    
    #Sobreescribir
    def imprime(self):
        super().imprime()
        print(f"ID: {self.id}, Curso: {self.id}")