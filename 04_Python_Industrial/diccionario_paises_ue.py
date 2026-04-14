import os
os.system('cls')


#Crea un programa que pida continuamente el nombre de un país de la Unión Europea y nos 
# conteste de forma automática con su capital. El programa permitirá la opción de introducir 
# el nombre del país y/o salir. En el caso de introducir un nombre que no forma parte de 
# la UE se indicará.

#Hacemos un diccionario con los Paises y sus capitales.
paises_de_la_UE = {
    'alemania': 'Berlín',
    'francia': 'París',
    'españa': 'Madrid',
    'italia': 'Roma',
    'paises bajos': 'Amsterdam',
    'belgica': 'Bruselas',
    'austria': 'Viena',
    'polonia': 'Varsovia',
    'grecia': 'Atenas',
    'portugal': 'Lisboa',
    'suecia': 'Estocolmo',
    'republica checa': 'Praga',
    'finlandia': 'Helsinki',
    'dinamarca': 'Copenhague',
    'irlanda': 'Dublín',
    'croacia': 'Zagreb',
    'hungria': 'Budapest',
    'eslovaquia': 'Bratislava',
    'eslovenia': 'Liubliana',
    'estonia': 'Tallín',
    'letonia': 'Riga',
    'lituania': 'Vilna',
    'malta': 'La Valeta',
    'chipre': 'Nicosia',
    'bulgaria': 'Sofía',
    'rumania': 'Bucarest',
    'luxemburgo': 'Luxemburgo'

}

#Hacemos un bucle que te da la opción de meter un país o de salir del programa.

while True:
    pais = input ("Introduce el nombre de un país o escribe 'salir' para terminar: ").lower().strip()

    if pais == "salir":
        print ("Finalizando programa")
        break


    if pais in paises_de_la_UE:
        print(f"La capital de {pais} es {paises_de_la_UE[pais]}.") 

    else:                                   
        print ("El país introducido no corresponde a la UE o no aparece en la lista")