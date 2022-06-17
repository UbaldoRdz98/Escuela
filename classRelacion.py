import json
import classMaterias
class classRelacion:
    def __init__(self):
        self.value = 0
        self.lstRelacion = []
        self.grupo = ""
        self.materias = []
        self.filename = "JSONS/Relacion.json"

    def load(self):
        self.lstRelacion.clear()
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)

        for relacion in json_object:
            p = []
            materias = []
            m = classRelacion()
            m.grupo = relacion["Grupo"]

            for x in relacion["Materias"]:
                n = classMaterias.classMaterias()
                n.nombre = x["Nombre"]
                for y in x["Parciales"]:
                    o = classMaterias.classMaterias()
                    o.nombreParcial = y["Nombre_Parcial"]
                    o.calificacion = y["Calificacion"]
                    p.append(o)
                n.parciales = p
                p = []
                materias.append(n)
            m.materias = materias
            self.lstRelacion.append(m)
        return self.lstRelacion

    def create(self, grupo, materias):
        valida = False
        if grupo:
            m = classRelacion()
            m.grupo = grupo
            m.materias = materias
            self.lstRelacion.append(m)
            y = self.jsonCreate()
            return y

    def addMaterias(self, indexGrupo, materias):
        lstM = self.lstRelacion[indexGrupo].materias
        print(lstM)
        for x in materias:
            lstM.append(x)
        print(lstM)
        self.lstRelacion[indexGrupo].materias = lstM
        y = self.jsonCreate()
        return y

    def deleteMaterias(self, indexGrupo, indexMateria):
        lstG = self.lstRelacion[indexGrupo].materias
        del lstG[indexMateria]
        y = self.jsonCreate()
        return y

    def jsonCreate(self):
        ls = []
        mat = []
        par = []
        for x in self.lstRelacion:
            for y in x.materias:
                for z in y.parciales:
                    par.append({"Nombre_Parcial": z.nombreParcial, "Calificacion": z.calificacion})
                mat.append({"Nombre": y.nombre, "Parciales": par})
                par = []
            ls.append({"Grupo": x.grupo, "Materias":mat})
            mat = []
        with open(self.filename, "w") as file:
            json.dump(ls, file, indent = 4)
        m = 3
        return m