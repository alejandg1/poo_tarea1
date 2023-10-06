from I_acta import acta
from clases import estudiante, docente, asignatura, carrera, cabecera

ingenieria = carrera("ingenieria", "FACI", "UNEMI", "A1")

Mika = estudiante("Milca", "Toledo", ingenieria)
Samuel = estudiante("Samuel", "Briones", ingenieria)
Fiore = estudiante("Fiorella", "Franco", ingenieria)
Ariana_pendeja = estudiante("Arianna", "Pendeja", ingenieria)
William = estudiante("William", "Gei", ingenieria)
Adre = estudiante("Alejandro", "Gómez", ingenieria)

calculo = asignatura("Calculo", 1, 100, "cubano", "pagada", "matutina")
poo = asignatura("poo", 4, 100, "el vera", "pagada", "matutina")

cubano = docente("cubano", "nose")

Mika.agregar_Materia(calculo)
Samuel.agregar_Materia(calculo)
Fiore.agregar_Materia(calculo)
Ariana_pendeja.agregar_Materia(calculo)
William.agregar_Materia(calculo)
Adre.agregar_Materia(calculo)

Mika.agregar_Materia(poo)
Samuel.agregar_Materia(poo)
Fiore.agregar_Materia(poo)
Ariana_pendeja.agregar_Materia(poo)
William.agregar_Materia(poo)
Adre.agregar_Materia(poo)


Mika.obtener_Materia("poo").agregar_notas(10, 10, 10, 10, 10, 101, 10)
Adre.obtener_Materia("poo").agregar_notas(10, 10, 10, 10, 10, 101, 10)
Samuel.obtener_Materia("poo").agregar_notas(10, 10, 10, 10, 10, 101, 10)
Fiore.obtener_Materia("poo").agregar_notas(10, 10, 10, 10, 10, 101, 10)
Ariana_pendeja.obtener_Materia("poo").agregar_notas(
    10, 10, 10, 10, 10, 101, 10)
William.obtener_Materia("poo").agregar_notas(10, 10, 10, 10, 10, 101, 10)

calificaciones = cabecera(ingenieria, "Acta", poo, "nose", "nose")
calificaciones.agregar_detalle(Mika,"poo")
calificaciones.agregar_detalle(Adre,"poo")
calificaciones.agregar_detalle(William,"poo")
calificaciones.agregar_detalle(Ariana_pendeja,"poo")
calificaciones.agregar_detalle(Fiore,"poo")
calificaciones.imprimir()
