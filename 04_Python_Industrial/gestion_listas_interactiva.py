#Creamos una lista de alumnos.
alumnos= ["Agustin Alfonso", "Pepito Sonatas"]
alumnos.sort()

#Creamos una función que nos limpie la pantalla de la terminal.
def limpiar_pantalla():
    import os
    os.system ("cls")
    
#Creamos una función que nos permita volver al menú.
def volver_menu():
    input("Pulse una tecla para volver al menú")

#Generamos un bucle con while que salga únicamente con la opción "salir".
while True:
    limpiar_pantalla()
    print("MENU PRINCIPAL")
    print("1.Mostrar listado de alumnos.")
    print("2.Añadir alumnos a la lista.")
    print("3.Borrar alumno de la lista.")
    print("4. Salir.")

    opcion=input("Elige una opción: ")

#Para la opción 1, Mostrar Menú.
    if opcion == "1":
        limpiar_pantalla()
        print("LISTADO DE ALUMNOS")
        print(alumnos)
        volver_menu()

#Para la opción 2, Añadir Alumno.
    elif opcion == "2":
        limpiar_pantalla()
        print("AÑADIR ALUMNO")
        nombre=(input("Introduce nombre y apellido: "))
        alumnos.append(nombre)
        alumnos.sort()
        print(alumnos)
        volver_menu()

#Para la opción 3, Borrar alumno.
    elif opcion == "3":
        limpiar_pantalla()
        print("BORRAR ALUMNO")
        print(alumnos)
        clave=int(input("Introduce el codigo del alumno que desea borrar de la lista: "))
        if clave >= 1 and clave <= len(alumnos):
            alumnos.pop(clave -1)
            print("Alumno borrado correctamente.")
        else:
            print("Código incorrecto.")
        volver_menu()

#Para la opción 4, Salir.
    elif opcion == "4":
        limpiar_pantalla()
        print("Finalizando el programa...")
        break

    else:
        print("Opción Incorrecta")
        

        






            