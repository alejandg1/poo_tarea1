from clases import Notas, estudiante, docente, asignatura, carrera, cabecera, detacta

ingenieria = carrera("ingenieria", "FACI", "UNEMI", "A1")
Mika = estudiante("Milca", "Toledo", ingenieria)
calculo = asignatura("Calculo", 1, 100, "cubano", "pagada", "matutina")
poo = asignatura("poo", 4, 100, "el vera", "pagada", "matutina")
Mika.agregar_Materia(calculo)
Mika.agregar_Materia(poo)
materia = Mika.obtener_Materia("poo")
materia.agregar_notas(10, 10, 10, 10, 10, 10, 10, 10, 70)
print(Mika.obtener_Materia("poo").notas.final)
