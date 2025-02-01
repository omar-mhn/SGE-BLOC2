# SGE-BLOC2
# Automatización de una Tabla de Clientes con Python y PostgreSQL

En este proyecto, estoy trabajando con una tabla de clientes en la que quiero realizar operaciones básicas como:

- Insertar un nuevo usuario.
- Leer los usuarios existentes.
- Modificar los datos de un usuario.
- Eliminar un usuario por completo.

Todo este trabajo, que en Excel se hace manualmente, se puede automatizar utilizando Python y una base de datos (BD) mediante la librería `psycopg2`, que permite trabajar con PostgreSQL desde Python.

En las siguientes líneas, probaré paso a paso cómo realizar esta conexión.

Se ha organizado el proyecto creando la carpeta `bloc2_NOMALUMNX`, con una subcarpeta `postgresql_python` que contiene los archivos principales del sistema: `connect.py`, `main.py`, `create_registre.py`, `read_registre.py`, `update_registre.py` y `delete_registre.py`. Todo se puede gestionar desde un IDE como VSCode o PyCharm.

![Structura](CapturAS/Structura.png)
 
# Conexión a la base de datos con Python y PostgreSQL

En este paso, hemos creado el archivo `connect.py`, que permite conectar a una base de datos PostgreSQL. El código utiliza la librería `psycopg2`, que facilita la interacción con PostgreSQL desde Python. Hemos configurado los parámetros de conexión con la información proporcionada en el archivo `docker-compose.yml`, incluyendo el nombre de la base de datos ("the_bear"), el usuario ("admin"), la contraseña ("admin"), el host ("localhost") y el puerto ("5432").

![Connexion à la base de données](CapturAS/cnx.png)

Esta conexión es fundamental para realizar las operaciones de gestión de la tabla de clientes: insertar, leer, actualizar y eliminar datos (CRUD). Una vez validada la conexión, podremos empezar a implementar estas funcionalidades en el proyecto.
# Creación de la tabla y carga de datos desde un CSV a la base de datos

En este paso, se realizará una prueba para verificar si la conexión a la base de datos es correcta. Para ello, es necesario tener los servicios de `docker-compose.yml` creados y activos. Una vez que los servicios estén en funcionamiento y podamos verlos en pgAdmin 4, se procederá a crear un script en Python para crear la tabla con los datos de los clientes en la base de datos.

## Pasos a seguir

### 1. Crear un script para pasar los datos de un CSV a la base de datos

Deberás descargar el archivo de clientes en formato `.csv` y agregarlo a una carpeta llamada `send_data_to_db` que estará dentro de la carpeta `bloc2`.

La estructura de los archivos dentro de `send_data_to_db` será la siguiente:

- `create_table_to_db.py`: Este script servirá para crear la tabla en la base de datos con los campos (sin registros) según el archivo `.csv` de clientes.
- `csv_to_dict.py`: Este script transformará la información del archivo `.csv` en formato diccionario.
- `dict_to_db.py`: Este script insertará los datos del diccionario en la base de datos, campo por campo (columna por columna).

### 2. Crear la tabla en la base de datos

El script `create_table_to_db.py` se encargará de crear la tabla correspondiente en la base de datos a partir de las cabeceras del archivo `.csv`. 

### 3. Convertir el CSV a un diccionario

El script `csv_to_dict.py` leerá el archivo `.csv` y convertirá cada fila en un diccionario, donde las claves serán las cabeceras del archivo y los valores serán los datos correspondientes.

### 4. Insertar los datos en la base de datos

El script `dict_to_db.py` tomará el diccionario generado y se encargará de insertar los datos en la base de datos, columna por columna, asegurando que cada campo se corresponda con el campo adecuado en la tabla de la base de datos.

![Inserción del registro](CapturAS/insercio%20del%20registre.png)


