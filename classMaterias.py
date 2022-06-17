import json
import classRelacion
import classSalones
class classMaterias:
    def __init__(self):
        self.value = 0
        self.re = classRelacion.classRelacion()
        self.lstMaterias = []
        self.nombre = ""
        self.parciales = []
        self.nombreParcial = ""
        self.calificacion = 0
        self.filename = "JSONS/Materias.json"

    def load(self):
        self.lstMaterias.clear()
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)

        for materia in json_object:
            l = []
            m = classMaterias()
            m.nombre = materia["Nombre"]
            for p in materia["Parciales"]:
                n = classMaterias()
                n.nombreParcial = p["Parcial"]
                n.calificacion = p["Calificacion"]
                l.append(n)
            m.parciales = l
            self.lstMaterias.append(m)
        return self.lstMaterias

    def create(self, nombre, parciales):
        m = classMaterias()
        m.nombre = nombre
        l = []
        for i in range(parciales):
            u = i + 1
            n = classMaterias()
            np = "Parcial " + str(u)
            n.nombreParcial = np
            n.calificacion = 0.0
            l.append(n)
        m.parciales = l
        self.lstMaterias.append(m)
        y = self.Jsoncreate()
        return y

    def update(self, nombre, index, parciales):
        self.sa = classSalones.classSalones()
        if parciales == 0:
            nombreAnt = self.lstMaterias[index].nombre
            self.lstMaterias[index].nombre = nombre
            self.lstRelacion = self.re.load()
            for x in self.lstRelacion:
                for y in x.materias:
                    if y.nombre == nombreAnt:
                        y.nombre = nombre
            val = self.re.jsonCreate()
            self.lstSalones = self.sa.load()
            for w in self.lstSalones:
                for x in w.alumnos:
                    for y in x.materias:
                        if y.nombre == nombreAnt:
                            y.nombre = nombre
            val = self.sa.jsonCreate()
        else:
            l = []
            for i in range(parciales):
                u = i + 1
                n = classMaterias()
                np = "Parcial " + str(u)
                n.nombreParcial = np
                n.calificacion = 0.0
                l.append(n)
            nombreAnt = self.lstMaterias[index].nombre
            self.lstMaterias[index].parciales = l
            self.lstRelacion = self.re.load()
            self.lstSalones = self.sa.load()
            for x in self.lstRelacion:
                for y in x.materias:
                    if y.nombre == nombreAnt:
                        y.parciales = self.lstMaterias[index].parciales
            val = self.re.jsonCreate()
            for w in self.lstSalones:
                for x in w.alumnos:
                    for y in x.materias:
                        if y.nombre == nombreAnt:
                            y.parciales = self.lstMaterias[index].parciales
            val = self.sa.jsonCreate()
        y = self.Jsoncreate()
        return y

    def Jsoncreate(self):
        ls = []
        lp = []
        for x in self.lstMaterias:
            for y in x.parciales:
                lp.append({"Parcial": y.nombreParcial, "Calificacion": y.calificacion})
            ls.append({"Nombre": x.nombre, "Parciales": lp})
            lp = []
        
        with open(self.filename, "w") as file:
            json.dump(ls, file, indent = 4)
        valida = True
        m = 3
        return m