from abc import ABC,abstractmethod

from clases import materia
class Interface(ABC):
    @abstractmethod
    def obtener_Calificaciones(self,Objt_estudiante) -> object :
        pass
    @abstractmethod
    def obtener_Docente(self,Objt_estudiante) -> str:
        pass

    @abstractmethod
    def obtener_Facultad(self,Objt_estudiante) -> str:
        pass


class acta(Interface):
    def obtener_Calificaciones(self, Objt_estudiante,Str_materia) :
        calificaciones = {
            "N1":0,
            "N2":0,
            "ex1":0,
            "ex2":0
        }
        actividades = Objt_estudiante.Materias[Str_materia].actividades
        for actividad in actividades:
            if actividad.tipo=="promedio":
                pass
            if actividad.tipo=="promedio":
                pass
            if actividad.tipo=="promedio":
                pass
    def obtener_Docente(self, Objt_estudiante,Str_materia) -> str:
        docente = Objt_estudiante.Materias[Str_materia].docente
        return docente

    def obtener_Facultad(self, Objt_estudiante) -> object:
        pass

