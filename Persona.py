class Persona:
    listaPersonas = []
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.listaPersonas.append(self)
    
    def imprime(self):
        # print("Nombre: ", self.nombre)
        # print("Apellido: ", self.apellido)
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}")

    @classmethod
    def imprimePersonas(cls) :
        for persona in cls.listaPersonas:
            persona.imprime()