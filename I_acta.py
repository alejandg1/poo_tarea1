from abc import ABC,abstractmethod

from clases import asignatura

class Interface(ABC):
    @abstractmethod
    def obtener_asistencia(self,Objt_estudiante,Str_asignatura) -> object :
        pass


    @abstractmethod
    def obtener_estado(self,Objt_estudiante,Str_asignatura) -> str:
        pass

    @abstractmethod
    def obtener_notas(self,Objt_estudiante,Str_asignatura) -> str:
        pass

class acta(Interface):
    def obtener_asistencia(self, Objt_estudiante,Str_asignatura) -> object:
        for asignatura in Objt_estudiante.asignaturas:
            if asignatura.nombre == Str_asignatura:
                return asignatura.asistencia
    def obtener_estado(self, Objt_estudiante,Str_asignatura) -> str:
        estado = "error"
        for asignatura in Objt_estudiante.asignaturas:
            if asignatura.nombre == Str_asignatura:
                estado = asignatura.estado
        return estado

    def obtener_notas(self, Objt_estudiante,Str_asignatura) -> object:
        for asignatura in Objt_estudiante.asignaturas:
            if asignatura.nombre == Str_asignatura:
                return asignatura.notas
