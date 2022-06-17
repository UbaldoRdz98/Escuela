import json
import classSalones
class classAlumnos:
    def __init__(self):
        self.value = 0
        self.lstAlumnos = []
        self.sa = classSalones.classSalones()
        self.matricula = 0
        self.nombre = ""
        self.apellidoPaterno = ""
        self.apellidoMaterno = ""
        self.filename = "JSONS/Alumnos.json"

    def load(self):
        self.lstAlumnos.clear()
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)
        for alumnos in json_object:
            m = classAlumnos()
            m.matricula = int(alumnos["Matricula"])
            m.nombre = alumnos["Nombre"]
            m.apellidoPaterno = alumnos["Apellido_Paterno"]
            m.apellidoMaterno = alumnos["Apellido_Materno"]
            self.lstAlumnos.append(m)
        return self.lstAlumnos

    def create(self, alumno):
        m = classAlumnos()
        for x in alumno:
            m.matricula = x['Matricula']
            m.nombre = x["Nombre"]
            m.apellidoPaterno = x["Apellido_Paterno"]
            m.apellidoMaterno = x["Apellido_Materno"]
            self.lstAlumnos.append(m)
        y = self.jsonCreate()
        return y

    def update(self, matricula, nombre, apellidoPaterno, apellidoMaterno, opcion):
        index = 0
        i = 0
        for x in self.lstAlumnos:
            if x.matricula == matricula:
                index = i
            i = i + 1

        self.lstSalones = self.sa.load()

        if opcion == "0":
            self.lstAlumnos[index].nombre = nombre
            for x in self.lstSalones:
                for y in x.alumnos:
                    if y.matricula == matricula:
                        y.nombre = nombre
                    val = self.sa.jsonCreate()
        elif opcion == "1":
            self.lstAlumnos[index].apellidoPaterno = apellidoPaterno
            for x in self.lstSalones:
                for y in x.alumnos:
                    if y.matricula == matricula:
                        y.apellidoPaterno = apellidoPaterno
                    val = self.sa.jsonCreate()
        else:
            self.lstAlumnos[index].apellidoMaterno = apellidoMaterno
            for x in self.lstSalones:
                for y in x.alumnos:
                    if y.matricula == matricula:
                        y.apellidoMaterno = apellidoMaterno
                    val = self.sa.jsonCreate()
        y = self.jsonCreate()
        return y

    def jsonCreate(self):
        al = []
        for x in self.lstAlumnos:
            al.append({"Matricula": x.matricula, "Nombre": x.nombre, "Apellido_Paterno": x.apellidoPaterno, "Apellido_Materno": x.apellidoMaterno})
        with open(self.filename, "w") as file:
            json.dump(al, file, indent = 4)
        m = 3
        return m