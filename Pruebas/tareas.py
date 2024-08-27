tareas =[]

def agregar_tarea(tarea): 
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada")

def mostrar_tareas():
    if tareas:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas en la lista.")



def eliminar_tarea(numero): 
    if 0 < numero <= len(tareas): 
        tarea= tareas.pop (numero-1)
        print(f"Tara '{tarea} eliminada")

    else:
        print ('Numero incorrecto')


while True:
    print("\nOpciones:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Ingresa la tarea: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        numero = int(input("Número de tarea a eliminar: "))
        eliminar_tarea(numero)
    elif opcion == "4":
        break
    else:
        print("Opción no válida, intenta de nuevo.")
     

