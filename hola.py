#/usr/bin/python3
import os

# Limpiar la pantalla
os.system("clear")

# Pedirle el nombre al usuarix
print ("Decime tu nombre por favor: ")
nombre = input()

# Deletrearlo
print ()
print ("Lo voy a deletrear")
for letra in nombre:
    print (letra)