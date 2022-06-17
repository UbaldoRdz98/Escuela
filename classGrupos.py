import json
import classSalones
import classRelacion
class classGrupos:
    def __init__(self):
        self.value = 0
        self.re = classRelacion.classRelacion()
        self.lstGrupos = []
        self.nombre = ""
        self.generacion = ""
        self.filename = "JSONS/Grupos.json"

    def load(self):
        self.lstGrupos.clear()
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)
        for Grupo in json_object:
            m = classGrupos()
            m.nombre = Grupo["Nombre"]
            m.generacion = Grupo["Generacion"]
            self.lstGrupos.append(m)
        return self.lstGrupos

    def create(self, nombre, generacion):
        m = classGrupos()
        m.nombre = nombre
        m.generacion = generacion
        self.lstGrupos.append(m)
        y = self.jsonCreate()
        return y

    def update(self, nombre, index):
        self.sa = classSalones.classSalones()
        nombreAnt = self.lstGrupos[index].nombre
        self.lstGrupos[index].nombre = nombre
        self.lstRelacion = self.re.load()
        for x in self.lstRelacion:
            print(x.grupo)
            if x.grupo == nombreAnt:
                x.grupo = nombre
        val = self.re.jsonCreate()
        self.lstSalones = self.sa.load()
        for w in self.lstSalones:
            if w.grupo == nombreAnt:
                w.grupo = nombre
        val = self.sa.jsonCreate()
        y = self.jsonCreate()
        return y

    def jsonCreate(self):
        ls = []
        for x in self.lstGrupos:
                ls.append({"Nombre": x.nombre, "Generacion": x.generacion})
        with open(self.filename, "w") as file:
            json.dump(ls, file, indent = 4)
        m = 3
        return m