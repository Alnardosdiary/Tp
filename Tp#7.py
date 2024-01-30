class alumno:
    def __init__(self, nombre, apellido, fecha_nacimiento, dni, tutor):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.tutor = tutor
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0

    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def mostrar_datos(self):
        print(f"El nombre del estudiante es: {self.nombre} {self.apellido}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"DNI: {self.dni}")
        print(f"Tutor: {self.tutor}")
        print(f"Faltas: {self.faltas}")
        print(f"Notas: {self.notas}")
        print(f"Amonestaciones: {self.amonestaciones}")
    
    def modificar_datos(self, nombre, apellido, dni, tutor, fecha_nacimiento):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.tutor=tutor
        self.fecha_nacimiento=fecha_nacimiento

    def expulsar_alumno(self, nombre, apellido):
        confirmacion = input(f"Esta seguro que quiere expulsar al alumno {self.nombre} {self.apellido} ? S/N: ")
        if confirmacion.lower == "S":
            print(f"El alumno {self.apellido} fue expulsado.")
            del self
        else:
            print("Se ha cancelado la expulsion.")

class Escuela:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self,alumno):
        self.alumnos.append(alumno)
    
    def buscar_alumno(self, dni):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None
    
escuela = Escuela()

# Agregar alumnos
alumno1 = alumno("Juan", "Pérez", "01/01/2000", "12345678", "María Gómez")
alumno1.agregar_nota(8)
alumno1.agregar_nota(7)
alumno1.faltas = 2
alumno1.amonestaciones = 1
escuela.agregar_alumno(alumno1)

alumno2 = alumno("María", "López", "05/05/2001", "87654321", "Pedro Rodríguez")
alumno2.agregar_nota(9)
alumno2.agregar_nota(10)
alumno2.faltas = 0
alumno2.amonestaciones = 0
escuela.agregar_alumno(alumno2)

#buscar alumno:

dniBuscar = int(input("Ingrese el dni del alumno: "))
alumno_encontrado = escuela.buscar_alumno(dniBuscar)
if alumno_encontrado:
    alumno_encontrado.modificar_datos()
else:
    print("No se encontro a ningun estudiante con ese dni") 
