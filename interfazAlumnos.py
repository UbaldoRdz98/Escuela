import classAlumnos
class interfazAlumnos:
    def __init__(self):
        self.al = classAlumnos.classAlumnos()
        self.lstAlumnos = []
        self.load()

    def menu(self):
        m = 0
        while m < 1:
            print("     1.- Registrar Alumnos")
            print("     2.- Editar Alumno")
            print("     3.- Ver Alumnos")
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
        self.lstAlumnos = self.al.load()

    def create(self):
        totAlumno = input("        ¿Cuantos Alumnos desea registrar?: ")
        i = 1
        while i <= int(totAlumno):
            self.load()
            alumno = []
            matricula = 21100000 + int(len(self.lstAlumnos))
            nombre = input("        Ingrese el Nombre del Alumno: ")
            apellidoPaterno = input("        Ingrese el Apellido Paterno del Alumno: ")
            apellidoMaterno = input("        Ingrese el Apellido Materno del Alumno: ")
            alumno.append({"Matricula": matricula, "Nombre": nombre, "Apellido_Paterno": apellidoPaterno, "Apellido_Materno": apellidoMaterno})
            i += 1
            self.al.create(alumno)
            print("         Alumnos Registrado | Matricula:", matricula)

    def update(self):
        self.read()
        mat = input("        Ingrese la Matricula del Alumno: ")
        matricula = int(mat)
        print("        0.- Actualizar Nombre:")
        print("        1.- Actualizar Apellido Paterno:")
        print("        2.- Actualizar Apellido Materno:")
        opcion = input("        Ingrese la Opción: ")

        if opcion == "0":
            nombre = input("        Ingrese el Nombre del Alumno: ")
            self.al.update(matricula, nombre, "", "", opcion)
        elif opcion == "1":
            apellidoPaterno = input("        Ingrese el Apellido Paterno del Alumno: ")
            self.al.update(matricula, "", apellidoPaterno, "", opcion)
        else:
            apellidoMaterno = input("        Ingrese el Apellido Materno del Alumno: ")
            self.al.update(matricula, "", "", apellidoMaterno, opcion)
        print("        Alumno Actualizado!")
        self.load()

    def read(self):
        self.load()
        if len(self.lstAlumnos) > 0:
            print("Total de Alumnos Registrados:", len(self.lstAlumnos))
            for val in self.lstAlumnos:
                print ("       ",val.matricula, ".- ",val.nombre,val.apellidoPaterno,val.apellidoMaterno)
        else:
            print("        No existen Alumnos")