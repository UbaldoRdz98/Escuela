import interfazMaterias
import interfazGrupos
import interfazRelacion
import interfazAlumnos
import interfazSalones
class Principal:
    def __init__(self):
        self.option = 0
        self.IntMat = interfazMaterias.interfazMaterias()
        self.IntGru = interfazGrupos.interfazGrupos()
        self.IntRel = interfazRelacion.interfazRelacion()
        self.IntAlu = interfazAlumnos.interfazAlumnos()
        self.IntSal = interfazSalones.interfazSalones()

    def menu_principal(self):
        i = 0
        while i < 1:
            print("1.- Materias")
            print("2.- Grupos")
            print("3.- Relacionar Materias-Grupos")
            print("4.- Alumnos")
            print("5.- Salones")
            print("6.- Salir")

            opcion = input("Seleccione el modulo: ")

            if opcion == "1":
                self.IntMat.menu()
            elif opcion == "2":
                self.IntGru.menu()
            elif opcion == "3":
                self.IntRel.menu()
            elif opcion == "4":
                self.IntAlu.menu()
            elif opcion == "5":
                self.IntSal.menu()
            else:
                opcion = input("¿Desea Salir? (S/N): ")
                if opcion.upper() == "S":
                    i = 2
                    print("ADIOS!!!")
                    exit()

prinp = Principal()
prinp.menu_principal()