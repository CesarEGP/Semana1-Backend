from metodos import Password

password = "Eduardo De Rivero"

"""
Convertir el nombre del ususario en una contraseña
    -Quitar los espcios
    -Todo tiene que estar en minusculas
    -Encriptar la contraseña 
"""

""" instancia de la clase Password """
Pass=Password()


print(Pass.encriptarPassword(Pass.minusculas(Pass.quitarEspacios(password))))
