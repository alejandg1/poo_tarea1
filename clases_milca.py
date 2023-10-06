class Carrera:
    def __init__(self, nombre:str, facultad:str, universidad:str, paralelo:str) -> None:
        self.nombre = nombre
        self.facultad = facultad
        self.universidad = universidad
        self.paralelo = paralelo

class Asignatura:
    def __init__(self,nombre:str, nivel:str, asistencia:int, docente_name:str, matricula:str, seccion:str, notas=[]) -> None:
        self.nombre = nombre
        self.nivel = nivel self.asistencia = asistencia self.notas = notas
        self.docente = docente_name
        self.matricula = matricula
        self.seccion = seccion 

class Notas:
    def __init__(self, n1:float, n2:float, ex1: float, p1:float, n3:float, n4:float, ex2:float, p2:float, rec:float, final:float) -> None:
        self.N1 = n1
        self.N2 = n2
        self.EX1 = ex1
        self.P1 = p1
        self.N3 = n3
        self.N4 = n4
        self.EX2 = ex2
        self.P2 = p2
        self.REC = rec
        self.FINAL = final
        
    def mostrar_notas(self):
        list_notas = {
            "N1": self.N1,
            "N2": self.N2,
            "EX1": self.EX1,
            "P1": self.P1,
            "N3": self.N3,
            "N4": self.N4,
            "EX2": self.EX2,
            "P2": self.P2,
            "REC": self.REC,
            "FINAL": self.FINAL
        }
        return list_notas

class Usuario:
    def __init__(self, nombre:str, apellido:str):
        self.Nombres = nombre
        self.Apellidos = apellido

class Profesor(Usuario):
    def __init__(self,nombre:str, apellido:str):
        super().__init__(nombre, apellido)

class Estudiante(Usuario):
    def __init__(self,nombre:str, apellido:str, carrera:str):
        super().__init__(nombre, apellido)
        self.Carrera = carrera
        self.Materias=[]
    
    def agregar_materias(self, Materia:Asignatura) -> None:
        self.Materias.append(Materia)
        
    def obtener_materias(self, nombre:str) -> Asignatura:
        hallado = False
        for materia in self.Materias:
            if materia.nombre == nombre:
                hallado = nombre
        return hallado

