import classSalones
import interfazRelacion
import interfazAlumnos
class interfazSalones:
    def __init__(self):
        self.sa = classSalones.classSalones()
        self.intRel = interfazRelacion.interfazRelacion()
        self.intAlu = interfazAlumnos.interfazAlumnos()
        self.lstSalones = []
        self.lstAlumnos = []
        self.lstRelacion = []
        self.load()

    def menu(self):
        m = 0
        while m < 1:
            print("     1.- Registrar Alumnos")
            print("     2.- Calificar Alumno")
            print("     3.- Ver Salones")
            print("     4.- Ver Calificaciones por Grupo")
            print("     5.- Ver Calificaciones por Alumno")
            print("     6.- Ver Calificaciones por Alumno - Materias")
            print("     7.- Ver Calificaciones por Grupo - Materias")
            print("     8.- Recargar Materias")
            print("     9.- Agregar Alumnos un Grupo ya existente")
            print("     10.- Regresar")
            opcion = input("     Seleccione el modulo: ")
            if opcion == "1":
                self.create()
            elif opcion == "2":
                self.updateCalificaciones()
            elif opcion == "3":
                self.read()
            elif opcion == "4":
                self.showPromedioGrupo()
            elif opcion == "5":
                self.showCalificacionesMateria()
            elif opcion == "6":
                self.showCalificacionesAlumno()
            elif opcion == "7":
                self.showCalificacionesMateriaGrupo()
            elif opcion == "8":
                self.updateMaterias()
            elif opcion == "9":
                self.addAlumnoGrupo()
            else:
                m = 3

    def load(self):
        self.lstAlumnos = self.intAlu.lstAlumnos
        self.lstRelacion = self.intRel.lstRelacion
        self.lstSalones = self.sa.load()

    def addAlumnoGrupo(self):
        self.intRel.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")
        r = self.lstRelacion[int(grupoIndex)]
        nombreGr = r.grupo
        materias = r.materias
        alumnos = []
        alumno = []
        fLetra = input("        Ingrese la primera letra del Nombre: ")
        for x in self.lstAlumnos:
            if x.nombre[0:1].upper() == fLetra.upper():
                print("             ",x.matricula,".-",x.nombre, x.apellidoPaterno, x.apellidoMaterno)
        matricula = input("        Ingrese la Matricula del Alumno: ")
        for y in self.lstAlumnos:
            if y.matricula == int(matricula):
                alumno.append(matricula)
                alumno.append(y.nombre)
                alumno.append(y.apellidoPaterno)
                alumno.append(y.apellidoMaterno)
                alumno.append(materias)
                break
        alumnos.append(alumno)
        h = self.sa.addAlumnoGrupo(nombreGr, alumnos)
        print("         Alumnos Registrados")

    def create(self):
        self.intRel.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")
        r = self.lstRelacion[int(grupoIndex)]
        nombreGr = r.grupo
        materias = r.materias
        alumnos = []
        alumno = []
        totAlumno = input("        ¿Cuantos Alumnos desea registrar?: ")
        i = 1

        while i <= int(totAlumno):
            fLetra = input("        Ingrese la primera letra del Nombre: ")
            for x in self.lstAlumnos:
                if x.nombre[0:1].upper() == fLetra.upper():
                    print("             ",x.matricula,".-",x.nombre, x.apellidoPaterno, x.apellidoMaterno)
            matricula = input("        Ingrese la Matricula del Alumno: ")
            for y in self.lstAlumnos:
                if y.matricula == int(matricula):
                    alumno.append(matricula)
                    alumno.append(y.nombre)
                    alumno.append(y.apellidoPaterno)
                    alumno.append(y.apellidoMaterno)
                    alumno.append(materias)
                    break
            alumnos.append(alumno)
            alumno = []
            matricula = 0
            i += 1
        h = self.sa.create(nombreGr, alumnos)
        print("         Alumnos Registrados")

    def updateCalificaciones(self):
        it = 0
        while it < 1:
            g = 0
            ma = 0
            mat = 0
            Parcial = ""
            calificacion = ""
            self.intRel.readGrupos()
            grupoIndex = input("        Ingrese el Número del Grupo: ")
            g = int(grupoIndex)
            self.readAlumnosGrupos(g)
            matricula = input("        Ingrese el Número del Alumno: ")
            ma = int(matricula)
            self.readMateriasAlumnos(g, ma)
            materia = input("        Ingrese el Número de la Materia: ")
            mat = int(materia)
            self.readParcialesMaterias(g, ma, mat)
            Parcial = input("        Ingrese el Número del Parcial: ")
            calificacion = input("        Ingrese la Calificación: ")
            h = self.sa.updateCalificaciones(g, ma, mat, int(Parcial), float(calificacion))
            opcion = input("¿Termino de Calificar a los Alumnos? (S/N): ")
            if opcion.upper() == "S":
                it = 2
        print("         Alumnos Actualizados")
        
    def updateMaterias(self):
        self.intRel.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")

        r = self.lstRelacion[int(grupoIndex)]
        nombreGr = r.grupo
        materias = r.materias
        h = self.sa.updateMaterias(nombreGr, materias)
        print("         Alumnos Actualizados")


    def read(self):
        self.load()
        if len(self.lstSalones) > 0:
            for i, val in enumerate(self.lstSalones):
                print ("       Grupo: ",val.grupo)
                print ("                Alumnos: ")
                for s in val.alumnos:
                    print ("                    > ", s.matricula,":",s.nombre,s.apellidoPaterno,s.apellidoMaterno)
        else:
            print("        No existen Alumnos")

    def readAlumnosGrupos(self, grupoIndex):
        lstG = self.lstSalones[grupoIndex].alumnos
        if len(lstG) > 0:
            for i, val in enumerate(lstG):
                print ("                    > ", i,":",val.nombre,val.apellidoPaterno,val.apellidoMaterno)
        else:
            print("        No existen Alumnos")

    def readMateriasAlumnos(self,  grupoIndex, matricula):
        lstG = self.lstSalones[grupoIndex].alumnos[matricula].materias
        if len(lstG) > 0:
            for i, val in enumerate(lstG):
                print ("                    > ", i,":",val.nombre)
        else:
            print("        No existen Alumnos")

    def readParcialesMaterias(self,  grupoIndex, matricula, materia):
        lstG = self.lstSalones[grupoIndex].alumnos[matricula].materias[materia].parciales
        if len(lstG) > 0:
            for i, val in enumerate(lstG):
                print ("                    > ", i,":",val.nombreParcial)
        else:
            print("        No existen Alumnos")

    def showCalificacionesAlumno(self):
        self.intRel.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")
        g = int(grupoIndex)
        self.readAlumnosGrupos(int(grupoIndex))
        matricula = input("        Ingrese el Número del Alumno: ")
        ma = int(matricula)
        lstG = self.lstSalones[int(grupoIndex)].alumnos[ma]
        print ("                    > Alumno:", lstG.nombre, lstG.apellidoPaterno, lstG.apellidoMaterno)
        lstG = self.lstSalones[g].alumnos[ma].materias
        for x in lstG:
            print ("                        > Materia:", x.nombre)
            s = 0.0
            p = 0
            for y in x.parciales:
                s = s + y.calificacion
                p = p + 1
                print ("                            >", y.nombreParcial, ":", y.calificacion)
            total = s/p
            print ("                            > Calificación Final:", total)
        else:
            print("        No existen Alumnos")

    def showCalificacionesMateria(self):
        self.intRel.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")
        g = int(grupoIndex)
        lstG = self.lstSalones[int(grupoIndex)].alumnos
        totalFinal = 0.0
        p = 0
        u = 0
        for v in lstG:
            print ("                    > Alumno:", v.nombre, v.apellidoPaterno, v.apellidoMaterno)
            for x in v.materias:
                s = 0.0
                for y in x.parciales:
                    u = u + 1
                    s = s + y.calificacion
                total = s/u
                u = 0
                p = p + 1
                totalFinal = total + totalFinal
            totalFinal = totalFinal / p
            print ("                            > Calificación Final:", totalFinal)

    def showCalificacionesMateriaGrupo(self):
        self.lstSalones = self.sa.load()
        self.intRel.readGrupos()
        grupoIndex = input("        Ingrese el Número del Grupo: ")
        g = int(grupoIndex)
        lstG = self.lstSalones[g].alumnos
        totalParcial = 0.0
        totalMateria = 0.0
        totalFinal = 0.0
        p = 0
        m = 0
        n = 0
        
        i = 0
        nombreMat = ""
        totalLenMaterias = len(lstG[0].materias)
        while i < totalLenMaterias:
            for x in lstG:
                totalParcial = 0
                p = 0
                y = x.materias[int(i)]
                m = m + 1
                for z in y.parciales:
                    p = p + 1
                    totalParcial = totalParcial + z.calificacion
                totalParcial = totalParcial / p
                nombreMat = y.nombre
                totalFinal = totalFinal + totalParcial
                continue
            i = i +1
            totalFinal = totalFinal / m
            m = 0
            print ("            >", y.nombre, ":", totalFinal)
            totalFinal = 0

    def showPromedioGrupo(self):
        lstG = self.lstSalones
        totalAlGr = 0.0
        alumnos = 0
        for v in lstG:
            totalAlGr = 0.0
            print("          Grupo:", v.grupo)
            w = v.alumnos
            print("          Alumnos en el Grupo:", len(w))
            for x in w:
                for y in x.materias:
                    s = 0.0
                    p = 0
                    for z in y.parciales:
                        s = s + z.calificacion
                        p = p + 1
                total = s/p
                totalAlGr = totalAlGr + total
            alumnos = len(v.alumnos)
            totalAlGr = totalAlGr / alumnos
            print ("            > Calificación Grupal:", totalAlGr)
        alumnos=0