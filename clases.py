from I_acta import acta
funciones = acta()


class carrera:
    def __init__(self, nombre: str, facultad: str, universidad: str, paralelo: str) -> None:
        self.nombre = nombre
        self.facultad = facultad
        self.universidad = universidad
        # NOTE: esto podria ser en materia o semestre
        # self.inicio = Dte_inicio
        # self.fin = Dte_fin
        self.paralelo = paralelo


class Notas:
    def __init__(self, n1:float, n2:float, ex1: float, n3:float, n4:float, ex2:float, rec:float) -> None:
        self.N1 = n1
        self.N2 = n2
        self.EX1 = ex1
        self.P1 = n1+n2+ex1
        self.N3 = n3
        self.N4 = n4
        self.EX2 = ex2
        self.P2 = n3+n4+ex2
        self.REC = rec
        self.FINAL = self.P1+self.P2+self.REC
        
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

class asignatura:

    def __init__(self, nombre: str, nivel: int, asistencia: int, docente_name: str,  matricula: str, seccion: str, notas=[]) -> None:
        self.nombre = nombre
        self.asistencia = asistencia
        self.nivel = nivel
        self.notas = notas
        self.docente = docente_name
        self.matricula = matricula
        self.seccion = seccion

    def agregar_notas(self, n1: float, n2: float, ex1: float, n3: float, n4: float, ex2: float,rec:float) -> None:
        self.notas = Notas(n1, n2, ex1,
                           n3, n4, ex2,rec)

        self.estado = "aprobado" if self.notas.FINAL> 70 or self.notas.FINAL+self.notas.REC > 70 else "reprobado"

class usuario:
    def __init__(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido


class estudiante(usuario):
    def __init__(self, nombre: str, apellido: str, carrera: carrera) -> None:
        super().__init__(nombre, apellido)
        self.carrera = carrera
        self.materias = []

    def agregar_Materia(self, materia: asignatura) -> None:
        self.materias.append(materia)

    def obtener_Materia(self, nombre: str)-> asignatura:
        hallado = "no encontrado"
        for materia in self.materias:
            if materia.nombre == nombre:
                hallado = materia
        return hallado


class docente(usuario):
    def __init__(self, nombre: str, apellido: str) -> None:
        super().__init__(nombre, apellido)


class detacta:
    def __init__(self, estudiante: estudiante, notas: object, estado: str, asistencia: int, asignatura: str) -> None:
        self.estudiante_nombre = estudiante.nombre
        self.estudiante_apellido = estudiante.apellido
        self.notas = notas
        self.asistencia = asistencia
        self.estado = estado
        self.asignatura = asignatura


class cabecera:
    def __init__(self, carrera:carrera, nombre_acta: str, Asignatura:asignatura,inicio:str,fin:str) -> None:
        self.nombre = nombre_acta
        self.profesor = Asignatura.docente
        self.asignatura = Asignatura.nombre
        self.nivel = Asignatura.nivel
        self.seccion = Asignatura.seccion
        self.carrera = carrera.nombre
        self.paralelo = carrera.paralelo
        self.inicio = inicio
        self.fin = fin
        self.facultad = carrera.facultad
        self.detalles = []

    def agregar_detalle(self, estudiante: estudiante, asignatura: str):
        funciones = acta()
        Int_notas = funciones.obtener_notas(estudiante, asignatura)
        Str_estado = funciones.obtener_estado(estudiante, asignatura)
        Int_asistencia = funciones.obtener_asistencia(
            estudiante, asignatura)
        detalle = detacta(estudiante, Int_notas,
                          Str_estado, Int_asistencia, asignatura)
        self.detalles.append(detalle)

    def imprimir(self):
        print(self.nombre.center(20))
        print()

        for detalle in self.detalles:
            # completar esto
            print(detalle)
