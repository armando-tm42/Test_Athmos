from .user import User
from .exceptions import ItemAlreadyStored, ItemNotStored, IdNotFound, EmptyList

users = list()


def crear_usuario(id, nombres, apellidos, edad, email):
    global users
    temp = User(id, nombres, apellidos, edad, email)
    if temp in users:
        raise ItemAlreadyStored("Esta intenado registrar un email y un id que ya se encuentra en lista")
    else:
        users.append(temp)

def crear_usuarios(user_list):
    global users
    users.clear()
    for index in range(len(user_list)):
        temp = User(user_list[index]['id'], user_list[index]['nombres'],
                    user_list[index]['apellidos'], user_list[index]['edad'],
                    user_list[index]['email'])
        if temp not in users:
            users.append(temp)


def mostrar_usuario(nombres):
    global users
    result = list(filter(lambda x: x.nombres == nombres, users))
    if result:
        return result[0]
    else:
        raise ItemNotStored("No hay registros en la lista con los nombres ingresados")


def mostrar_usuarios():
    global users
    if not users:
        raise EmptyList("La lista de usuarios se encuentra vacia")
    if users:
        lista = [user for user in users]
        return lista


def actualizar_usuario(id, nombres, apellidos, edad, email):
    global users
    flag = False
    index = int
    for idx, user in enumerate(users):
        if user.id == id:
            flag = True
            index = idx
            break
    if flag is True:
        users[index].nombres = nombres
        users[index].apellidos = apellidos
        users[index].edad = edad
        users[index].email = email
    else:
        raise ItemNotStored("No se encontro registro con el id proporcionado")


def eliminar_usuario(id):
    global users
    flag = False
    index = int
    for idx, user in enumerate(users):
        if user.id == id:
            flag = True
            index = idx
            break
    if flag is True:
        del users[index]
    else:
        raise IdNotFound("No se ha encontrado el id especificado")


def vaciar_lista():
    global users
    users.clear()
