from I_acta import acta
from clases import estudiante, docente, asignatura, carrera, cabecera

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


ingenieria = carrera("SOFTWARE 2019", "FACULTAD DE CIENCIAS E INGENIERÍAS", "UNEMI", "A1")

Mika = estudiante("Milca", "Toledo", ingenieria)
Samuel = estudiante("Samuel", "Briones", ingenieria)
Fiore = estudiante("Fiorella", "Franco", ingenieria)
Ariana = estudiante("Arianna", "Zuñiga", ingenieria)
William = estudiante("William", "Macias", ingenieria)
Adre = estudiante("Alejandro", "Gómez", ingenieria)

calculo = asignatura("Calculo", 1, 100, "cubano", "pagada", "Matutina", "24/04/2023", "20/08/2023", "ABRIL - AGOSTO 2023")
poo = asignatura("POO", 4, 100, "DANIEL ALEXANDER VERA PAREDES", "pagada", "MATUTINA", "24/04/2023", "20/08/2023", "ABRIL - AGOSTO 2023")

cubano = docente("cubano", "nose")

Mika.agregar_Materia(calculo)
Samuel.agregar_Materia(calculo)
Fiore.agregar_Materia(calculo)
Ariana.agregar_Materia(calculo)
William.agregar_Materia(calculo)
Adre.agregar_Materia(calculo)

Mika.agregar_Materia(poo)
Samuel.agregar_Materia(poo)
Fiore.agregar_Materia(poo)
Ariana.agregar_Materia(poo)
William.agregar_Materia(poo)
Adre.agregar_Materia(poo)


Mika.obtener_Materia("POO").agregar_notas(10, 10, 20, 10, 10, 20, 10)
Adre.obtener_Materia("POO").agregar_notas(10, 10, 20, 10, 10, 20, 10)
Samuel.obtener_Materia("POO").agregar_notas(10, 10, 20, 10, 10, 20, 10)
Fiore.obtener_Materia("POO").agregar_notas(10, 10, 20, 10, 10, 20, 10)
Ariana.obtener_Materia("POO").agregar_notas(10, 10, 20, 10, 10, 20, 10)
William.obtener_Materia("POO").agregar_notas(10, 10, 20, 10, 10, 20, 10)

calificaciones = cabecera(ingenieria, "ACTA DE CALIFICACIONES", poo)
calificaciones.agregar_detalle(Mika,"POO")
calificaciones.agregar_detalle(Adre,"POO")
calificaciones.agregar_detalle(William,"POO")
calificaciones.agregar_detalle(Ariana,"POO")
calificaciones.agregar_detalle(Fiore,"POO")
calificaciones.imprimir()
