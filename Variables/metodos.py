import hashlib

class Password:
    
    """ metodos """
    def quitarEspacios(self,cadena:str):
        cadenasinEspacio=cadena.replace(" ","")
        return cadenasinEspacio
    
    def minusculas(self,cadena:str):
        cadenaMinuscula=cadena.lower()
        return cadenaMinuscula
    
    def encriptarPassword(self, nombre_sin_espacios):
        cadena_encriptada = nombre_sin_espacios.encode()
        return hashlib.sha256(cadena_encriptada).hexdigest()
        

