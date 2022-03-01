class Alumno:
    escuela = "Coding Dojo"
    def __init__(self, nombre, apellido, email): #SELF nos incluye toda la información del objeto individual
        self.nombre = nombre
        self.apellido = apellido
        self.email = "pordefault@email.com"
        self.lineasCodigo = 0
    
    def aumentaLineas(self, lineas):
        self.lineasCodigo += lineas

    def imprimeAlumno(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Correo: {self.email}, LC: {self.lineasCodigo}, Escuela: {self.escuela}")