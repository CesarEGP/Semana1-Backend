""" Para las clases se usa la palabra reservada class """
class MiClase:
    numero = 12345
    texto = "Hola mundo"
    estado = True
valores = MiClase()    


class Vehiculo:
    """ construtor """
    def __init__(self, a, b):
        self.color = a
        self.marca = b

    """ metodo to string """
    def __str__(self):
        return f"Vehiculo {self.color} y la marca {self.mostrarMarca()}"

    """ metodo para mostrar la marca """
    def mostrarMarca(self):
        return self.marca
    
auto = Vehiculo("rojo","Mitsubishi")

""" print(auto) """

""" crear un objeto Operaciones, que tenga los siguientes metodos
-Suma
-Resta
Y los atributos se deben ingresar por el objeto """

class Operacion:
    """ constructor """
    def __init__(self,a:int,b:int):
        self.numero1=a
        self.numero2=b
    """ metodo to String """
    def __str__(self) -> str:
        return f"Respuesta de la suma es: {self.Suma()} y la resta es: {self.Resta()}"            

    def Suma(self):
        resultado= self.numero1+self.numero2
        return resultado
    
    def Resta(self):
        resultado= self.numero1-self.numero2
        return resultado
        
operaciones = Operacion(10,3)
print(operaciones)
