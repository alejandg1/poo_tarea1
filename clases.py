from tabulate import tabulate
from I_acta import acta
funciones = acta()


class carrera:
    def __init__(self, nombre: str, facultad: str, universidad: str, paralelo: str) -> None:
        self.nombre = nombre
        self.facultad = facultad
        self.universidad = universidad
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

    def __init__(self, nombre: str, nivel: int, asistencia: int, docente_name: str,  matricula: str, seccion: str, Iperiodo, Fperiodo, Lperiodo,  notas=[]) -> None:
        self.nombre = nombre
        self.asistencia = asistencia
        self.nivel = nivel
        self.notas = notas
        self.docente = docente_name
        self.matricula = matricula
        self.seccion = seccion
        self.periodo_In = Iperiodo
        self.periodo_Out = Fperiodo
        self.periodo_LEV = Lperiodo

    def agregar_notas(self, n1: float, n2: float, ex1: float, n3: float, n4: float, ex2: float,rec:float) -> None:
        self.notas = Notas(n1, n2, ex1,
                            n3, n4, ex2,rec)

        self.estado = "APROBADO" if self.notas.FINAL> 70 or self.notas.FINAL+self.notas.REC > 70 else "REPROBADO"

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
    id = 0
    def __init__(self, estudiante: estudiante, notas: object, estado: str, asistencia: int) -> None:
        self.estudiante_nombre = estudiante.nombre
        self.estudiante_apellido = estudiante.apellido
        self.notas = notas
        self.asistencia = asistencia.__str__()+"%"
        self.estado = estado
        detacta.id+=1
        self.id = detacta.id

    def mostrar(self):
        linea =[self.id,(self.estudiante_nombre +" "+ self.estudiante_apellido),self.notas.N1,self.notas.N2,self.notas.EX1,self.notas.P1,self.notas.N3,self.notas.N4,self.notas.EX2,self.notas.P2,self.notas.REC,self.notas.FINAL,self.asistencia,self.estado]
        return linea


class cabecera:
    def __init__(self, carrera:carrera, nombre_acta: str, Asignatura:asignatura) -> None:
        self.nombre = nombre_acta
        self.profesor = Asignatura.docente
        self.asignatura = Asignatura.nombre
        self.nivel = Asignatura.nivel
        self.seccion = Asignatura.seccion
        self.carrera = carrera.nombre
        self.paralelo = carrera.paralelo
        self.universidad = carrera.universidad
        self.facultad = carrera.facultad
        self.Lev_periodo = Asignatura.periodo_LEV
        self.I_periodo = Asignatura.periodo_In
        self.Out_periodo = Asignatura.periodo_Out
        self.detalles = []

    def agregar_detalle(self, estudiante: estudiante, asignatura: str):
        funciones = acta()
        Int_notas = funciones.obtener_notas(estudiante, asignatura)
        Str_estado = funciones.obtener_estado(estudiante, asignatura)
        Int_asistencia = funciones.obtener_asistencia(
            estudiante, asignatura)
        detalle = detacta(estudiante, Int_notas,
                            Str_estado, Int_asistencia)
        self.detalles.append(detalle)
    def imprimir(self):
        #universidad_azul = "\033[94m" + self.universidad + "\033[0m"
        tabla = [
            #[universidad_azul],
            [self.universidad],
            [(""),self.nombre],
            [(""),(f"PERIODO LECTIVO: {self.Lev_periodo}")],
            [(f"{self.facultad}")],
            [(f"CARRERA: {self.carrera}")],
            [(f"NIVEL: {self.nivel}"),(""), (f"PARALELO: {self.paralelo}")],
            [(f"PROFESOR: {self.profesor}"),(""),(f"ASIGNATURA: {self.asignatura}")],
            [(f"SECCION: {self.seccion}"),(""),(f"INICIO: {self.I_periodo}"),(f"FIN: {self.Out_periodo}")],
        ]
        cab = tabulate(tabla,"",tablefmt="rounded_grid")
        print(cab)
        detalles =[]
        for detalle in self.detalles:
            linea = detalle.mostrar()
            detalles.append(linea)
        encabezados =["No.","APELLIDOS Y NOMBRES","N1","N2","EX1","P1","N3","N4","EX2","P2","RE","N.FINAL","% ASIST","ESTADO"]
        notas = tabulate(detalles,encabezados,tablefmt="rounded_grid")
        print(notas)
