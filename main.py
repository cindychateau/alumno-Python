from Alumno import Alumno #Importando mi archivo Alumno

from Persona import Persona
from Estudiante import Estudiante

jose = Alumno("Jose", "Doe", "jose@codingdojo.com")
vale = Alumno("Valeria", "Perez", "valeria@codingdojo.com")

vale.nombre = "Vale"
vale.escuela = "Universidad CD"
Alumno.escuela = "CD International"

#print(vale.escuela)

vale.aumentaLineas(100)

jose.aumentaLineas(1000)

# vale.imprimeAlumno()
# jose.imprimeAlumno()

john = Persona("John", "Doe")
cynthia = Estudiante("Cynthia", "Castillo", 123, "Python")

Persona.imprimePersonas()
print("------")
Estudiante.imprimeEstudiantes()