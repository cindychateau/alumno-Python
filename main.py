from Alumno import Alumno #Importando mi archivo Alumno

jose = Alumno("Jose", "Doe", "jose@codingdojo.com")
vale = Alumno("Valeria", "Perez", "valeria@codingdojo.com")

vale.nombre = "Vale"
vale.escuela = "Universidad CD"
Alumno.escuela = "CD International"

print(vale.escuela)

vale.aumentaLineas(100)

jose.aumentaLineas(1000)

vale.imprimeAlumno()
jose.imprimeAlumno()