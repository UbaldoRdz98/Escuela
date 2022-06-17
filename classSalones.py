import json
import classMaterias
class classSalones:
    def __init__(self):
        self.value = 0
        self.ma = classMaterias.classMaterias()
        self.lstSalones = []
        self.alumnos = []
        self.matricula = 0
        self.nombre = ""
        self.apellidoPaterno = ""
        self.apellidoMaterno = ""
        self.grupo = ""
        self.materias = []
        self.nombreMateria = ""
        self.calificacionMateria = 0.0
        self.filename = "JSONS/Salones.json"

    def load(self):
        self.lstSalones.clear()
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)

        for alumnos in json_object:
            lstAlumnos = []
            for x in alumnos["Alumnos"]:
                lstMaterias = []
                for y in x["Materias"]:
                    lstParciales = []
                    for z in y["Parciales"]:
                        par = classMaterias.classMaterias()
                        par.nombreParcial = z["Nombre_Parcial"]
                        par.calificacion = z["Calificacion"]
                        lstParciales.append(par)
                    mat = classMaterias.classMaterias()
                    mat.nombre = y["Nombre"]
                    mat.parciales = lstParciales
                    lstMaterias.append(mat)
                al = classSalones()
                al.matricula = x["Matricula"]
                al.nombre = x["Nombre"]
                al.apellidoPaterno = x["Apellido_Paterno"]
                al.apellidoMaterno = x["Apellido_Materno"]
                al.materias = lstMaterias
                lstAlumnos.append(al)
            m = classSalones()
            m.grupo = alumnos["Grupo"]
            m.alumnos = lstAlumnos
            self.lstSalones.append(m)
        return self.lstSalones

    def create(self, grupo, alumnos):
        m = classSalones()
        m.grupo = grupo
        ls = []
        for x in alumnos:
            al = classSalones()
            al.matricula = int(x[0])
            al.nombre = x[1]
            al.apellidoPaterno = x[2]
            al.apellidoMaterno = x[3]
            al.materias = x[4]
            ls.append(al)
        m.alumnos = ls
        self.lstSalones.append(m)
        y = self.jsonCreate()
        return y

    def updateCalificaciones(self, grupo, alumno, materia, parcial, calificacion):
        self.lstSalones[grupo].alumnos[alumno].materias[materia].parciales[parcial].calificacion = calificacion
        y = self.jsonCreate()
        return y

    def addAlumnoGrupo(self, grupo, alumnos):
        ls = []
        for x in alumnos:
            al = classSalones()
            al.matricula = int(x[0])
            print(al.matricula)
            al.nombre = x[1]
            al.apellidoPaterno = x[2]
            al.apellidoMaterno = x[3]
            al.materias = x[4]
            ls.append(al)
        for x in self.lstSalones:
            if x.grupo == grupo:
                x.alumnos.append(al)
        y = self.jsonCreate()
        return y

    def updateMaterias(self, grupo, materias):
        for x in self.lstSalones:
            if x.grupo == grupo:
                for y in x.alumnos:
                    y.materias = materias
        y = self.jsonCreate()
        return y

    def jsonCreate(self):
        ls = []
        al = []
        mat = []
        par = []
        for x in self.lstSalones:
            for y in x.alumnos:
                print(y.matricula)
                for z in y.materias:
                    for p in z.parciales:
                        par.append({"Nombre_Parcial": p.nombreParcial, "Calificacion": p.calificacion})
                    mat.append({"Nombre": z.nombre, "Parciales": par})
                    par = []
                al.append({"Matricula": y.matricula, "Nombre": y.nombre, "Apellido_Paterno": y.apellidoPaterno, "Apellido_Materno": y.apellidoMaterno, "Materias": mat})
                mat = []
            ls.append({"Grupo": x.grupo, "Alumnos": al})
            al = []

        with open(self.filename, "w") as file:
            json.dump(ls, file, indent = 4)
        m = 3
        return m