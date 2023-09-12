# API de chistes

Este API REST proporciona una serie de endpoints para gestionar chistes.

Endpoint de chistes: 

Este endpoint devuelve un chiste aleatorio. Si se envía el parámetro chuck en la consulta, el chiste se obtendrá del API de Chuck Norris. Si no se envía ningún parámetro, el chiste se obtendrá de la base de datos.

Endpoint de creación de chistes: Este endpoint permite guardar un chiste en la base de datos.

Endpoint de actualización de chistes: Este endpoint permite actualizar un chiste existente en la base de datos.

Endpoint de eliminación de chistes: Este endpoint permite eliminar un chiste de la base de datos.

## Instalación

Para instalar el API, siga estos pasos:

Clonar el repositorio:

__git clone https://github.com/cristian1903/chistes.git__

Instalar las dependencias:
```
pip install -r requirements.txt
```
Uso
Para usar el API, siga estos pasos:

#Ejecutar las migraciones:
```
python manage.py migrate
```
Inicialize el servidor:
```
python manage.py runserver*
```
Envíe una solicitud al endpoint de chistes:
```
curl -X GET http://localhost:8000/chistes
```
Esto devolverá un chiste aleatorio.

Para obtener un chiste de Chuck Norris, envíe la siguiente solicitud:
```
curl -X GET http://localhost:8000/chistes?chuck=1
```
Para guardar un chiste, envíe la siguiente solicitud:
```
curl -X POST http://localhost:8000/chistes -d '{"texto": "Este es un chiste"}'
```
Para actualizar un chiste, envíe la siguiente solicitud:
```
curl -X PUT http://localhost:8000/chistes/1 -d '{"texto": "Este es un chiste actualizado"}'
```
Para eliminar un chiste, envíe la siguiente solicitud:
```
curl -X DELETE http://localhost:8000/chistes/1
```

