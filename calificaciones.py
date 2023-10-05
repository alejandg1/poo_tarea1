from clases import Notas, estudiante, docente, asignatura, carrera, cabecera, detacta

ingenieria = carrera("ingenieria", "FACI", "UNEMI", "A1")
Mika = estudiante("Milca", "Toledo", ingenieria)
notas_calculo = Notas(0, 1, 2, 3, 4, 5, 6, 7, 8)
calculo = asignatura("Calculo", 1, 100, "cubano", "pagada", "matutina")
poo = asignatura("poo", 4, 100, "el vera", "pagada", "matutina")
print(poo)
Mika.agregar_Materia(calculo)
Mika.agregar_Materia(poo)
print(Mika.carrera.nombre)
print("###############")
print(Mika.materias[0].nombre)
