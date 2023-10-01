class usuario:
    def __init__(self,Str_nombre,Str_apellido)-> None:
        self.nombre = Str_nombre
        self.apellido = Str_apellido

class estudiante(usuario):
    def __init__(self, Str_nombre, Str_apellido,Str_carrera,Obj_matricula)-> None:
        super().__init__(Str_nombre, Str_apellido)
        self.carrera = Str_carrera
        self.matricula = Obj_matricula

class docente(usuario):
    def __init__(self, Str_nombre, Str_apellido,Str_materia,Lst_aulas)-> None:
        super().__init__(Str_nombre, Str_apellido)
        self.materia = Str_materia
        self.aulas = Lst_aulas

class actividad:
    def __init__(self,Str_nombre,Str_puntaje,Dte_inicio,Dte_fin) -> None:
        self.nombre = Str_nombre
        self.puntaje = Str_puntaje
        self.inicio = Dte_inicio
        self.fin = Dte_fin

class materia:
    def __init__(self,Str_nombre) -> None:
        pass

class carrera:
    pass

class matricula:
    pass
