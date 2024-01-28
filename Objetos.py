# class auto:
#     def __init__(self, velocidadMAx=100, color = "amarillo"):
#         self.velocidadMAX = velocidadMAx
#         self.color=color
#         self.acelerar()

#     def arrancar(self):
#         print("brumm")
    
#     def acelerar(self,velocidad):
#         # velocidadMAx = 10 #variable global
#         if velocidad<=self.velocidadMAX #atributo
#            print("El auto va a:", velocidad , "km/h")
#         else:
#             print("Se funde el motor.")
        
 
# Autito1 = auto(300, "red")
# Autito2 = auto(300)
# print(Autito1.color)
# Autito2.arrancar()
# Autito2.acelerar

"""Crear una clase gato que contenga 5 atributos y 4 metodos. Luego instanciar 3 objetos de la clase gato con distintos atributos y utilizar sus metodos."""
 
class gato:
    def __init__ (self, nombre, colorPelo, colorOjos, cansancio, hambre, felicidad):
        self.nombre=nombre
        self.colorPelo=colorPelo
        self.colorOjos=colorOjos
        self.cansancio=cansancio
        self.hambre=hambre
        self.felicidad=felicidad
        self.comer()
        self.dormir()
        self.jugar()

    def dormir(self, cansancio):
        if cansancio > 0:
          cansancio-1
          print(f"el gato duerme y su cansacion es de {cansancio}")
        else:
           print("No tiene cansancio")


    def comer (self):
        if self.hambre >= 5:
          self.hambre -=5
          print("Come")
        else:
           print("No tiene hambre")

    def jugar(self, hambre, cansacio):
       if True:
          self.hambre+1
          self.cansacio+1
          print("El gato jugo ahora tiene de hambre y cansancio.")
    
    def acariciar(self, felicidad):
       if True:
          felicidad+10
          print(f"Su felicida por las caricias es {felicidad}")

Lilo = gato("Lilo", "naranja", "verdes", 10, 20, 100)
Lilo.comer(20)





