from abc import ABC,abstractmethod

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

    # @abstractmethod
    # def obtener_facultad(self, Objt_estudiante) -> str:
    #     pass
    # @abstractmethod
    # def obtener_nivel(self, Objt_estudiante,Str_asignatura) -> str: pass
    # @abstractmethod
    # def obtener_profesor(self, Objt_estudiante,Str_asignatura) -> str:
    #     pass
    # @abstractmethod
    # def obtener_paralelo(self,Objt_estudiante,Str_asignatura)->str:
    #     pass
    # @abstractmethod
    # def obtener_inicio_fin(self,Objt_estudiante)->object:
    #     pass

class acta():
    def obtener_asistencia(self, Objt_estudiante,Str_asignatura) -> int:
        asistencias = 1
        for asignatura in Objt_estudiante.asignaturas:
            if asignatura.nombre == Str_asignatura:
                asistencias =  asignatura.asistencia
        return asistencias
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

    # def obtener_facultad(self, Objt_estudiante) -> str:
    #     return Objt_estudiante.carrera.facultad
    # def obtener_nivel(self, Objt_estudiante,Str_asignatura) -> str:
    #     nivel = "error"
    #     for asignatura in Objt_estudiante.asignaturas:
    #         if asignatura.nombre == Str_asignatura:
    #             nivel =  asignatura.nivel
    #     return nivel
    # def obtener_profesor(self, Objt_estudiante,Str_asignatura) -> str:
    #     docente = "error"
    #     for asignatura in Objt_estudiante.asignaturas:
    #         if asignatura.nombre == Str_asignatura:
    #             docente =  asignatura.docente
    #     return docente
    # def obtener_paralelo(self,Objt_estudiante,Str_asignatura)->str:
    #     paralelo = "error"
    #     for asignatura in Objt_estudiante.asignaturas:
    #         if asignatura.nombre == Str_asignatura:
    #             paralelo =  asignatura.paralelo
    #     return paralelo
    # def obtener_inicio_fin(self,Objt_estudiante)->object:
    #     inicio_fin = {
    #         "inicio":Objt_estudiante.carrrera.inicio,
    #         "inicio":Objt_estudiante.carrrera.fin,
    #     }
    #     return inicio_fin

