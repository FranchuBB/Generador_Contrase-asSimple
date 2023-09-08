import random

class Contraseña:
    def __init__(self,nombre,largo,caracter,contra):
        self.nombre = nombre
        self.largo = largo
        self.contra = contra

passw = Contraseña  # instanciamos objeto

passw.nombre= input("ingrese un nombre para la contraseña: ")
passw.largo= int(input("Ingrese el largo de la contraseña: "))

def numaleatorio():
    num= random.randint(0,9)
    return str(num)

def letraaleatoria():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'        
    letra= random.choice(alfabeto)  # letra aleatoria
    ### mayuscula / minuscula random
    r= random.choice(["a","b"])
    if r == "a":
        return str(letra.upper())  # con mayuscula 
    else: 
        return str(letra)  # sin mayuscula 
ps= ""
for i in range (passw.largo):
    j= random.choice(["a","b"])
    if j == "a":
        n= numaleatorio()
        ps+=n
    else: 
        n= letraaleatoria()
        ps+=n
passw.contra = ps

print (f'Tu contraseña: {passw.nombre} de {passw.largo} letras de longitud, fue creada: \n {passw.contra}', end="")