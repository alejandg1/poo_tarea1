from I_acta import acta

class usuario:
    def __init__(self,Str_nombre,Str_apellido)-> None:
        self.nombre = Str_nombre
        self.apellido = Str_apellido

class estudiante(usuario):
    def __init__(self, Str_nombre, Str_apellido,Str_carrera,Lst_Materias)-> None:
        super().__init__(Str_nombre, Str_apellido)
        self.carrera = Str_carrera
        self.__materias = []

    def agregar_Materia(self,Obj_materia)-> None:
        self.__materias.append(Obj_materia)

    @property # se puede usar solo con atributos privados
    def materias(self)->list:
        return self.__materias

class docente(usuario):
    def __init__(self, Str_nombre, Str_apellido)-> None:
        super().__init__(Str_nombre, Str_apellido)


class actividad:
    def __init__(self,Str_nombre,Dte_inicio,Dte_fin,Str_tipo) -> None:
        self.nombre = Str_nombre
        self.inicio = Dte_inicio
        self.fin = Dte_fin
        self.tipo = Str_tipo
        self.__puntaje = 0

    @property
    def puntaje(self)-> int:
        return self.__puntaje

    def calificar(self,Flt_puntaje)-> None:
        self.__puntaje = Flt_puntaje


class materia:
    def __init__(self,Str_nombre,Int_nivel,Int_asistencia,Str_docente,Int_precio,Bool_aprobado) -> None:
        self.nombre = Str_nombre
        self.asistencia = Int_asistencia
        self.nivel = Int_nivel
        self.actividades = []
        self.docente = Str_docente
        self.porPagar = Int_precio
        self.aprobado = Bool_aprobado

    def nueva_actividad(self,Obj_actividad)-> None:
        self.actividades.append(Obj_actividad)

class acta:
    def __init__(self,Obj_estudiante) -> None:
        self.estudiante =  Obj_estudiante.nombre
        self.docente = acta.
#
# class carrera:
#     #materias
#     def __init__(self,Str_nombre,Str_modalidad) -> None:
#         self.nombre = Str_nombre
#         self.modalidad = Str_modalidad
#         self.materias = []
#     def nueva_actividad(self,Obj_materia)-> None:
#         self.materias.append(Obj_materia)
#
# class matricula:
#     def __init__(self,Obj_estudiante,Int_deuda,Str_materia_nombre) -> None:
#         pass
