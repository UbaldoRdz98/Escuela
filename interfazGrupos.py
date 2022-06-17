import classGrupos
class interfazGrupos:
    def __init__(self):
        self.ma = classGrupos.classGrupos()
        self.lstGrupos = []
        self.load()

    def menu(self):
        m = 0
        while m < 1:
            print("     1.- Nuevo Grupo")
            print("     2.- Editar Grupo")
            print("     3.- Eliminar Grupo")
            print("     4.- Ver Grupos")
            print("     5.- Regresar")
            opcion = input("     Seleccione el modulo: ")
            if opcion == "1":
                self.create()
            elif opcion == "2":
                self.update()
            elif opcion == "3":
                self.editarMateria()
            elif opcion == "4":
                self.read()
            else:
                m = 3

    def load(self):
        self.lstGrupos = self.ma.load()
        return self.lstGrupos

    def create(self):
        nombre = input("        Ingrese el nombre del Grupo: ")
        m = 0
        generacion = input("        Ingrese el año del Grupo (YYYY): ")
        x = self.ma.create(nombre, generacion)
        while m < 1:
            if x:
                print("        Grupo Creado!")
                m = 3
            else:
                nombre = input("        Ingrese el nombre del Grupo: ")
                x = self.ma.create(nombre, generacion)
        self.load()

    def update(self):
        self.read()
        nombre = input("        Ingrese el número del Grupo: ")
        grupoIndex = int(nombre)
        nombre = input("        Ingrese el nombre del Grupo: ")
        x = self.ma.update(nombre, grupoIndex)
        print("        Grupo Actualizado!")
        self.load()
    
    def read(self):
        self.load()
        if len(self.lstGrupos) > 0:
            for i, val in enumerate(self.lstGrupos):
                print ("       ",i, ".- ",val.nombre)
                print ("            > Año",val.generacion)
        else:
            print("        No existen Grupo")