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
    def mostrar(self, num):
        print(f'{num}.   {self.estudiante_apellido} {self.estudiante_nombre}   {self.estudiante.cedula}   {self.notas.FINAL}')


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
        detalle = detacta(estudiante, Int_notas, Int_asistencia, Str_estado )
        self.detalles.append(detalle)

    def imprimir(self):
        print('UNIVERSIDAD ESTATAL DE MILAGRO')
        print(self.nombre.center(20))
        print(f'FACULTAD: {self.facultad}')
        print(f'CARRERA: {self.carrera}')
        print(f'NIVEL: {self.nivel}')
        print(f'PARALELO: {self.paralelo}')
        print(f'ASIGNATURA: {self.asignatura}')
        print(f'PROFESOR(A): {self.profesor}')
        print(f'PERIODO LECTIVO: {self.inicio} - {self.fin}')
        print("----------------------------------------------------------------")
        print('No.   APELLIDOS Y NOMBRES   N1    N2   EX1   P1   N3   N4   EX2   P2   RE     N.FINAL    ASIST    ESTADO')
        for i, detalle in enumerate(self.detalles, start=1):
            detalle.mostrar(i)
            print('---')
