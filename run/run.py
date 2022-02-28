import sys
sys.path.append("..")
from mvc.controlador import Controlador
from mvc.modelo import Modelo
from mvc.vista import Vista
import os
import time
user_list = [
    {
        "id": 1,
        "nombres": 'el pepe',
        "apellidos": 'Tapia metza',
        "edad": 20,
        "email": 'armitame@hotmail.com'
    },
]

# user_list = []
c = Controlador(Modelo(user_list), Vista())
clear = lambda: os.system('cls')
pause = lambda: os.system('pause')
carga = False


def agregar_usuario():
    print('\n')
    id = int(input(' Ingrese id: '))
    nombres = input(' Ingrese nombres : ')
    apellidos = input(' Ingrese apellidos: ')
    edad = int(input(' Ingrese edad: '))
    email = input(' Ingrese email: ')
    c.agregar_usuario(id, nombres, apellidos, edad, email)
    print('\n')
    time.sleep(2.5)
    clear()


def mostrar_lista():
    print('\n')
    c.mostrar_lista()
    print('\n')
    pause()
    clear()


def salir():
    global carga
    if carga is True:
        print('Ha cargado usuario desde una base de datos recientemente')
        borrar = input('¿Desea guardar los cambios? s/n: ')
        if borrar == 's' or borrar == 'S':
            print('\n')
            print('Volvera al menu principal en breve')
            time.sleep(2.5)
            clear()
        else:
            print('\n')
            carga = False
            print('\n')
            print("Hasta luego")
            exit(0)
    elif carga is False:
        print('\n')
        print("Hasta luego")
        exit(0)


def buscar_usuario():
    print('\n')
    nombres = input(' Ingrese nombres del usuario a buscar: ')
    c.mostrar_usuario(nombres)
    print('\n')
    pause()
    clear()


def actualizar_usuario():
    print('\n')
    id = int(input(' Ingrese id del usuario que desea modificar: '))
    nombres = input('Ingrese nombres : ')
    apellidos = input('Ingrese apellidos: ')
    edad = int(input('Ingrese edad: '))
    email = input('Ingrese email: ')
    c.actualizar_usuario(id, nombres, apellidos, edad, email)
    print('\n')
    time.sleep(2.5)
    clear()


def eliminar_usuario():
    print('\n')
    id = int(input(' Ingrese id del usuario a eliminar : '))
    c.eliminar_usuario(id)
    print('\n')
    time.sleep(2.5)
    clear()


def guardar_db():
    global carga
    print('\n')
    nombre = input('Ingrese nombre del archivo: ')
    extension = '.json'
    completo = nombre + extension
    ruta_actual = os.getcwd()
    padre = os.path.dirname(ruta_actual)
    ruta_completa = os.path.join(padre, c.modelo.ruta_db, completo)
    if os.path.exists(ruta_completa):
        print('\n')
        sobre = input(' ya existe una base de datos con el nombre ingresado  ¿Desea sobreescribirla? s/n: ')
        print('\n')
        if sobre == 'S' or sobre == 's':
            carga = False
            c.guardar(completo)
            time.sleep(2.5)
            clear()
        else:
            print('\n')
            time.sleep(2.5)
            clear()
            print('Volvera al menu principal en breve')
            print('\n')
    else:
        carga = False
        c.guardar(completo)
        time.sleep(2.5)
        clear()


def mostrar_db():
    print('\n')
    c.mostrar_archivos()
    pause()
    clear()


def cargar_db():
    global carga
    print('\n')
    nombre = input('Ingrese nombre del archivo: ')
    extension = '.json'
    completo = nombre + extension
    exito = c.cargar_usuarios(completo)
    if exito is True:
        carga = exito
    time.sleep(2.5)
    clear()


def eliminar_db():
    print('\n')
    nombre = input('Ingrese nombre del archivo: ')
    extension = '.json'
    completo = nombre + extension
    c.eliminar_db(completo)
    time.sleep(2.5)
    clear()


def vaciar_lista():
    global carga
    print('\n')
    if carga is True:
        print('Ha cargado usuario desde una base de datos recientemente')
        borrar = input('¿Desea guardar los cambios? s/n: ')
        if borrar == 's' or borrar == 'S':
            print('\n')
            print('Volvera al menu principal en breve')
            time.sleep(2.5)
            clear()
            print('\n')
        else:
            carga = False
            c.vaciar_lista()
            time.sleep(2.5)
            clear()
    elif carga is False:
        c.vaciar_lista()
        time.sleep(2.5)
        clear()


switcher = {
    1: agregar_usuario,
    2: mostrar_lista,
    3: buscar_usuario,
    4: actualizar_usuario,
    5: eliminar_usuario,
    6: guardar_db,
    7: mostrar_db,
    8: cargar_db,
    9: eliminar_db,
    10: vaciar_lista,
    11: salir
}


def opciones(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "Opcion invalida")
    # Execute the function
    return func()



if __name__ == "__main__":

    opt = int()

    while opt != 11 or carga == True:
        print('\n')
        print('***Menu Principal***')
        print(' 1 - Agregar usuario')
        print(' 2 - Mostrar lista de usuarios')
        print(' 3 - Buscar usuario')
        print(' 4 - Actualizar usuario')
        print(' 5 - Eliminar usuario')
        print(' 6 - Guardar en Base de datos')
        print(' 7 - Mostrar Bases de datos')
        print(' 8 - Cargar usuarios desde Base de datos')
        print(' 9 - Eliminar Base de datos ')
        print(' 10 - Vaciar lista')
        print(' 11 - Salir')
        print('\n')
        opt = int(input(' Ingrese Opcion: '))
        opciones(opt)
        clear()