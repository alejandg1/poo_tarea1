class usuario:
    def __init__(self,Str_nombre,Str_apellido)-> None:
        self.nombre = Str_nombre
        self.apellido = Str_apellido

class estudiante(usuario):
    def __init__(self, Str_nombre, Str_apellido,Str_carrera,Lst_Materias)-> None:
        super().__init__(Str_nombre, Str_apellido)
        self.carrera = Str_carrera
        self.__materias= Lst_Materias

        #NOTE: quitar property dependiendo de si es necesario o no
    @property # se puede usar solo con atributos privados
    def materias(self)->list:
        return self.__materias



class docente(usuario):
    def __init__(self, Str_nombre, Str_apellido,Str_materia,Lst_aulas)-> None:
        super().__init__(Str_nombre, Str_apellido)
        self.materia = Str_materia
        self.aulas = Lst_aulas
    def calificar(self,Obj_actividad) -> None:
        Obj_actividad.puntaje=1

class actividad:
    def __init__(self,Str_nombre,Str_puntaje,Dte_inicio,Dte_fin) -> None:
        self.nombre = Str_nombre
        self.puntaje = Str_puntaje
        self.inicio = Dte_inicio
        self.fin = Dte_fin
    def registrar_puntaje(self,Flt_puntaje)-> None:
        self.puntaje = Flt_puntaje

class materia:
    # asistencia, actividades, matricula, docentes, estudiantes
    def __init__(self,Str_nombre,Int_nivel) -> None:
        self.nombre = Str_nombre
        self.nivel = Int_nivel
        self.actividades = []
    def registrar_asistencia(self)->None:
        #calcula el porcentaje de asistencias
        pass
    def nueva_actividad(self,Obj_actividad)-> None:
        self.actividades.append(Obj_actividad)

class carrera:
    #materias
    def __init__(self,Str_nombre,Str_modalidad) -> None:
        self.nombre = Str_nombre
        self.modalidad = Str_modalidad
        self.materias = []
    def nueva_actividad(self,Obj_materia)-> None:
        self.materias.append(Obj_materia)

class matricula:
    def __init__(self,Obj_estudiante,Int_deuda,Str_materia_nombre) -> None:
        pass
