# Test_Athmos
Para la solución del test se creó un programa consiste en un modulo de gestión de usuarios con guardado en bases de datos, usando archivos JSON.

## Estructura de Carpetas
```
.
├── db # Contiene los archivos JSON generados por el usuario.
├── logic 
|   └── exceptions.py # excepciones personalizadas arrojadas por el programa.
|   └── user.py # Clase que define un usuario.
|   └── user_crud.py # Archivo que almacena los métodos que implementan la clase usuario.
├── mvc
|   └── controlador.py # Clase controlador la cual se encarga de comunicar el modelo y las vistas.
|   └── modelo.py # Clase modelo, esta implementa la lógica del programa, así como el manejo de las bases de datos.
|   └── vista.py # Clase vista, maneja la representación de los datos proporcionados por el modelo.
├── run
|   └── run.py # Maneja el menú principal e implementa el controlador.
├── test
|   └── test_user.py # Unit test para los setters y getters de la clase usuario.
|   └── test_user_crud.py # Unit test para los métodos que implementan la clase usuario y el manejo de la lista.
|   └── test_model.py # Unit test para los métodos que manejan la base de datos en la clase modelo. 
├── venv # contiene los distintos archivos del ambiente virutal.
├── requirements.txt # librerias usadas en el desarrollo del programa.

```
## Uso
Al ejecutar el script run.py se desplegará un UI en consola con el siguiente menú: 

```python
  #output
  >>> "***Menu Principal***"
  >>> "1 - Agregar usuario"
  >>> "2 - Mostrar lista de usuarios"
  >>> "3 - Buscar usuario"
  >>> "4 - Actualizar usuario"
  >>> "5 - Eliminar usuario"
  >>> "6 - Guardar en Base de datos"
  >>> "7 - Mostrar Bases de datos"
  >>> "8 - Cargar usuarios desde Base de datos"
  >>> "9 - Eliminar Base de datos"
  >>> "10 - Vaciar lista"
  >>> "11 - Salir"
```
al seleccionar opciones relaciones con operaciones tales como agregar, actualizar, buscar o borrar. Las operaciones se realizarán sobre la lista temporal disponible en el programa

Vista del método buscar:
```python
---LISTA DE USUARIOS---
+----+---------+-----------+------+---------------------+
| Id | Nombres | Apellidos | Edad |        Email        |
+----+---------+-----------+------+---------------------+
| 1  |   jhon  |    doe    |  20  | jhondoe@hotmail.com |
+----+---------+-----------+------+---------------------+
```

Para trabajar con una lista guardada en un base de datos debe seleccionar la opción cargar usuarios y suministrar el nombre del archivo, de esta manera la lista temporal será reemplazada por la extraída desde el archivo JSON.

```python
>>> Ingrese Opcion: 8
>>> Ingrese nombre del archivo: prueba
# output
>>> Se han cargado los usuarios correctamente
```

Cabe destacar que al cargar usuarios desde una base de datos externa el programa reconocerá que se ha abierto un archivo recientemente, por lo que al intentar salir o vaciar la lista se le preguntara si desea guardar los cambios.

```python
>>>  Ingrese Opcion: 10
>> Ha cargado usuario desde una base de datos recientemente
¿Desea guardar los cambios? s/n: s
>>> Volvera al menu principal en breve
```
## Funcionalidades faltantes
El programa solo permite realizar búsqueda por nombres, si se crea una clase abstracta para el método y se procede a implementar el filtrado con los diferentes campos se ampliaran las formas de buscar usuarios.

Poder restaurar bases de datos usando copias de seguridad mediante el patrón memento, sería una funcionalidad que complementaria la gestión de archivos ya presente en el programa.
