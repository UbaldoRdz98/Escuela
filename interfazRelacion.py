import classRelacion
import classGrupos
import classMaterias
import interfazMaterias
class interfazRelacion:
    def __init__(self):
        self.re = classRelacion.classRelacion()
        self.gr = classGrupos.classGrupos()
        self.ma = classMaterias.classMaterias()
        self.im = interfazMaterias.interfazMaterias()
        self.lstRelacion = []
        self.lstGrupos = []
        self.lstMaterias = []
        self.load()

    def menu(self):
        m = 0
        while m < 1:
            print("     1.- Nueva Relacion")
            print("     2.- Agregar Materias a una Relacion")
            print("     3.- Eliminar Materias de una Relacion")
            print("     4.- Ver Relacion")
            print("     5.- Regresar")
            opcion = input("     Seleccione el modulo: ")
            if opcion == "1":
                self.create()
            elif opcion == "2":
                self.addMaterias()
            elif opcion == "3":
                self.deleteMaterias()
            elif opcion == "4":
                self.read()
            else:
                m = 3

    def load(self):
        self.lstRelacion = self.re.load()
        self.lstGrupos = self.gr.load()
        self.lstMaterias = self.ma.load()

    def create(self):
        self.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")
        r = self.lstGrupos[int(grupoIndex)]
        nombreGr = r.nombre
        it = 0
        y = []
        while it < 1:
            self.im.read()
            mat = input("Ingrese el número de la Materia: ")
            y.append(self.lstMaterias[int(mat)])
            opcion = input("¿Termino de Cargar las Materias? (S/N): ")
            if opcion.upper() == "S":
                it = 2
        self.re.create(nombreGr, y)
        self.load()

    def addMaterias(self):
        self.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")
        it = 0
        y = []
        while it < 1:
            self.im.read()
            mat = input("Ingrese el número de la Materia: ")
            y.append(self.lstMaterias[int(mat)])
            opcion = input("¿Termino de Cargar las Materias? (S/N): ")
            if opcion.upper() == "S":
                it = 2
        self.re.addMaterias(int(grupoIndex), y)
        self.load()

    def deleteMaterias(self):
        self.readGrupos()
        grupo = input("        Ingrese el número del Grupo: ")
        it = 0
        while it < 1:
            self.readMateriasGrupo(int(grupo))
            materia = input("        Ingrese el número de la Materia: ")
            self.re.deleteMaterias(int(grupo), int(materia))
            opcion = input("        ¿Termino de eliminar las Materias? (S/N): ")
            if opcion.upper() == "S":
                it = 2
        self.load()
        print("        Para el buen funcionamiento de la aplicación, favor de recargar las materias en el apartado de salones.")

    def read(self):
        self.load()
        if len(self.lstRelacion) > 0:
            for i, val in enumerate(self.lstRelacion):
                print ("       ",i, ".- Grupo: ",val.grupo)
                print ("                Materias: ")
                for s in val.materias:
                    print ("                    > Nombre: ",s.nombre)
        else:
            print("        No existen Relaciones")

    def readMateriasGrupo(self, index):
        lstG = self.lstRelacion[index].materias
        if len(lstG) > 0:
            for i, val in enumerate(lstG):
                print ("       ",i, ".- ",val.nombre)
        else:
            print("        No existen Relaciones")

    def readGrupos(self):
        self.load()
        if len(self.lstGrupos) > 0:
            for i, val in enumerate(self.lstGrupos):
                print ("       ",i, ".- ",val.nombre)
        else:
            print("        No existen Grupo")