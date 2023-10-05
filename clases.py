from I_acta import acta

class usuario:
    def __init__(self,Str_nombre,Str_apellido)-> None:
        self.nombre = Str_nombre
        self.apellido = Str_apellido

class estudiante(usuario):
    def __init__(self, Str_nombre, Str_apellido,Obj_carrera)-> None:
        super().__init__(Str_nombre, Str_apellido)
        self.carrera = Obj_carrera
        self.__materias = []

    def agregar_Materia(self,Obj_materia)-> None:
        self.__materias.append(Obj_materia)

    @property # se puede usar solo con atributos privados
    def materias(self)->list:
        return self.__materias

class docente(usuario):
    def __init__(self, Str_nombre, Str_apellido)-> None:
        super().__init__(Str_nombre, Str_apellido)

class carrera:
    def __init__(self,Str_nombre,Str_facultad,Str_universidad,Dte_inicio,Dte_fin,Str_paralelo) -> None:
        self.nombre = Str_nombre
        self.facultad = Str_facultad
        self.universidad = Str_universidad
        self.inicio = Dte_inicio
        self.fin = Dte_fin
        self.paralelo = Str_paralelo

class asignatura:
<<<<<<< HEAD
    def __init__(self,Str_nombre,Int_nivel,Int_asistencia,Str_docente_name,Obj_notas) -> None:
=======

    def __init__(self,Str_nombre,Int_nivel,Int_asistencia,Obj_docente,Obj_notas,Str_matricula,Str_seccion) -> None:
>>>>>>> e1941f6c3fc880659bd06b7dc3cff60851f6091a
        self.nombre = Str_nombre
        self.asistencia = Int_asistencia
        self.nivel = Int_nivel
        self.notas = Obj_notas
<<<<<<< HEAD
        self.docente = Str_docente_name
=======

        self.docente = Obj_docente
        self.matricula = Str_matricula
        self.seccion = Str_seccion
>>>>>>> e1941f6c3fc880659bd06b7dc3cff60851f6091a
        self.estado = "aprobado" if self.notas.final>70 else "reprobado" 
    def agregar_notas(self,Flt_n1,Flt_n2,Flt_p1,Flt_ex1,Flt_n3,Flt_n4,Flt_p2,Flt_ex2,Flt_final)-> None:
        self.notas = Notas(Flt_n1,Flt_n2,Flt_p1,Flt_ex1,Flt_n3,Flt_n4,Flt_p2,Flt_ex2,Flt_final)

class Notas:
    def __init__(self,Flt_n1,Flt_n2,Flt_ex1,Flt_p1,Flt_n3,Flt_n4,Flt_ex2,Flt_p2,Flt_final) -> None:
        self.N1 = Flt_n1
        self.N2 = Flt_n2
        self.EX1 = Flt_ex1
        self.P1 = Flt_p1
        self.N3 = Flt_n3
        self.N4 = Flt_n4
        self.P2 = Flt_p2
        self.EX2 = Flt_ex2
        self.final = Flt_final

class detacta:
    def __init__(self,Obj_estudiante,Obj_notas,Str_estado,Int_asistencia,Str_asignatura) -> None:
        self.estudiante_nombre = Obj_estudiante.nombre
        self.estudiante_apellido = Obj_estudiante.apellido
        self.notas = Obj_notas
        self.asistencia = Int_asistencia
        self.estado = Str_estado  
<<<<<<< HEAD
class cabeceraActa:
    def __init__(self,Str_nombre,Objt_estudiante,Str_asignatura_name,Str_seccion_asignatura) -> None:
        funciones = acta()
=======
class cabecera:

    def __init__(self,Str_nombre,Str_profesor_name,Str_asignatura_name,Str_nivel_asignatura,Str_seccion_asignatura,Str_carrera_nombre,Str_paralelo,Obj_fechas,Str_facultad) -> None:
>>>>>>> e1941f6c3fc880659bd06b7dc3cff60851f6091a
        self.nombre = Str_nombre
        self.profesor = funciones.obtener_profesor(Objt_estudiante,Str_asignatura_name)
        self.asignatura = Str_asignatura_name
        self.nivel = funciones.obtener_nivel(Objt_estudiante,Str_asignatura_name)
        self.seccion = Str_seccion_asignatura
        self.carrera = Objt_estudiante.carrera.nombre
        self.paralelo = funciones.obtener_paralelo(Objt_estudiante,Str_asignatura_name)
        self.fechas = funciones.obtener_inicio_fin(Objt_estudiante)
        self.facultad = funciones.obtener_facultad(Objt_estudiante)
        self.detalles = []

    def agregar_detalle(self,Objt_estudiante,Str_asignatura):
        funciones = acta()
        Obj_notas = funciones.obtener_notas(Objt_estudiante,Str_asignatura)
        Str_estado = funciones.obtener_estado(Objt_estudiante,Str_asignatura)
        Int_asistencia = funciones.obtener_asistencia(Objt_estudiante,Str_asignatura)
        detalle = detacta(Objt_estudiante,Obj_notas,Str_estado,Int_asistencia,Str_asignatura)
        self.detalles.append(detalle)
    def imprimir(self):
        print(self.nombre.center(20))
        print()

        for detalle in self.detalles:
            #completar esto
            print(detalle)







