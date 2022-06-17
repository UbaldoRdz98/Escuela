import classMaterias
class interfazMaterias:
    def __init__(self):
        self.ma = classMaterias.classMaterias()
        self.lstMaterias = []
        self.load()

    def menu(self):
        m = 0
        while m < 1:
            print("     1.- Nueva Materia")
            print("     2.- Editar Materia")
            print("     3.- Ver Materias")
            print("     4.- Regresar")
            opcion = input("     Seleccione el modulo: ")
            if opcion == "1":
                self.create()
            elif opcion == "2":
                self.update()
            elif opcion == "3":
                self.read()
            else:
                m = 3

    def load(self):
        self.lstMaterias = self.ma.load()

    def create(self):
        nombre = input("        Ingrese el nombre de la Materia: ")
        parciales = input("        Ingrese el número de parciales por esta materia: ")
        m = 0
        x = self.ma.create(nombre, int(parciales))
        while m < 1:
            if x:
                print("        Materia Creada!")
                m = 3
            else:
                nombre = input("        Ingrese el nombre de la Materia: ")
                parciales = input("        Ingrese el número de parciales por esta materia: ")
                x = self.ma.create(nombre, int(parciales))
        self.load()

    def update(self):
        print("        0.- Actualizar Nombre:")
        print("        1.- Actualizar Total de Parciales:")
        opcion = input("        Ingrese la opción deseada:")
        self.read()
        nombre = input("        Ingrese el número de la Materia: ")
        materiaIndex = int(nombre)
        
        if opcion == "0":
            nombre = input("        Ingrese el nombre de la Materia: ")
            x = self.ma.update(nombre, materiaIndex, 0)
            print("        Materia Actualizada!")
        else:
            parciales = input("        Ingrese el número de parciales por esta materia: ")
            x = self.ma.update("", materiaIndex, int(parciales))
            print("        Materia Actualizada!")
        self.load()

    def read(self):
        self.load()
        if len(self.lstMaterias) > 0:
            for i, val in enumerate(self.lstMaterias):
                print ("       ",i, ".- ",val.nombre)
        else:
            print("        No existen Materias")