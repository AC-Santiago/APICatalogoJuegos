# API-Catalogo-Juegos

Es un proyecto universitario, sobre una API Rest el cual proporcionara un catalogo de juegos variados y sus recomendaciones por medios de modelos de aprendizaje podrá realizar recomendaciones.

### Requerimientos

Para poder trabajar en este proyecto es necesario instalar las dependencias del proyecto las cuales estan en el archivo requirements.txt.

para instalarlos usar el siguiente comando:

```bash
  pip install -r requirements.txt
```

Se recomienda crear un entorno virtual antes de instalar las dependencias.

```bash
  python -m venv venv
```

y activarlo:

```bash
  .\venv\Scripts\activate
```

Para desacativarlo usar:

```bash
  deactivate
```

### Tecnologias

- Python
- Django
- Django rest framework
- Numpy
- Pandas

## API Reference

La url base de la API, es:

```link
  https://apicatalogojuegos.onrender.com
```

Esta url base es temporal, y pude cambiar por otra.

### Urls catalogo

/GameVault/ es la url base de para peticiones de Urls catalogo, osea que una url de ejemplol es:

```link
  http://localhost:8000/GameVault/
```

- Obtener Urls catalogo:

```API
  GET /GameVault/
```

Responce:

```Response
  {
    "catalogo/Juegos": "http://localhost:8000/GameVault/catalogo/Juegos/",
    "catalogo/ImagenesJuegos": "http://localhost:8000/GameVault/catalogo/ImagenesJuegos/",
    "catalogo/Plataformas": "http://localhost:8000/GameVault/catalogo/Plataformas/",
    "catalogo/Desarrolladoras": "http://localhost:8000/GameVault/catalogo/Desarrolladoras/",
    "catalogo/Generos": "http://localhost:8000/GameVault/catalogo/Generos/"
}
```

- Obtener Lista de Juegos

```API
  GET /catalogo/Juegos/
```

```API
  GET /catalogo/Juegos/?limit={int}
```

```API
  GET /catalogo/Juegos/?limit={int}&offset={int}
```

| Parametro | Tipo     | Descripción                                     |
| :-------- | :------- | :---------------------------------------------- |
| `limit`   | `string` | Por defecto viene con un limit de 10 por pagina |
| `offset`  | `string` | El offset determina desde que item empieza      |

Response:

```Response
{
    "count": {# de juegos},
    "next": "http://localhost:8000/GameVault/catalogo/Juegos/?limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "id": 0,
            "titulo": "Elden Ring",
            "fecha_Lanzamiento": "2022-02-25",
            "resumen": "////",
            "valoracion": 4.5,
            "numero_Partidas": 21000,
            "numero_jugadores": 4100,
            "comprado_no_jugado": 5600,
            "menciones_listas": 4600,
            "listas_de_deseos": 5500,
            "images": [],
            "reseñas": 3000,
            "generos": [
                "Adventure",
                "RPG"
            ],
            "plataformas": [
                "Windows PC",
                "PlayStation 4",
                "Xbox One",
                "PlayStation 5",
                "Xbox Series"
            ],
            "desarrolladora": [
                "FromSoftware",
                "Bandai Namco Entertainment"
            ]
        }
    ]
}
```

- Seleccionar un Juego

```API
  GET /catalogo/Juegos/:id/
```

| Parametro | Tipo     | Descripción                                  |
| :-------- | :------- | :------------------------------------------- |
| `id`      | `string` | **Requiere**. Que la id pertenzca a un Juego |

Response:

```Response
{
    "id": 0,
    "titulo": "Elden Ring",
    "fecha_Lanzamiento": "2022-02-25",
    "resumen": "/////",
    "valoracion": 4.5,
    "numero_Partidas": 21000,
    "numero_jugadores": 4100,
    "comprado_no_jugado": 5600,
    "menciones_listas": 4600,
    "listas_de_deseos": 5500,
    "images": [
        "https://tse2.mm.bing.net/th/id/OIP.3SOUHFaAQSZ2AQdN1XbUIgHaEK"
    ],
    "reseñas": 3000,
    "generos": [
        "Adventure",
        "RPG"
    ],
    "plataformas": [
        "Windows PC",
        "PlayStation 4",
        "Xbox One",
        "PlayStation 5",
        "Xbox Series"
    ],
    "desarrolladora": [
        "FromSoftware",
        "Bandai Namco Entertainment"
    ]
}
```

- Obtener lista de imagenes de los Juegos

```API
  GET /catalogo/ImagenesJuegos/
```

```API
  GET /catalogo/ImagenesJuegos/?limit=10
```

```API
  GET /catalogo/ImagenesJuegos/?limit=10&offset=10
```

| Parametro | Tipo     | Descripción                                     |
| :-------- | :------- | :---------------------------------------------- |
| `limit`   | `string` | Por defecto viene con un limit de 10 por pagina |
| `offset`  | `string` | El offset determina desde que item empieza      |

Response:

```Response
[
  {
    "id": 0,
    "url": "https://tse2.mm.bing.net/th/id/OIP.3SOUHFaAQSZ2AQdN1XbUIgHaEK"
  },
  ...
]
```

- Obtener lista de plataformas

```API
  GET /catalogo/Plataformas/
```

```API
  GET /catalogo/Plataformas/?limit=10
```

```API
  GET /catalogo/Plataformas/?limit=10&offset=10
```

| Parametro | Tipo     | Descripción                                     |
| :-------- | :------- | :---------------------------------------------- |
| `limit`   | `string` | Por defecto viene con un limit de 10 por pagina |
| `offset`  | `string` | El offset determina desde que item empieza      |

Response:

```Response
[
  {
    "id": 0,
    "nombre": "PlayStation 4"
  },
  ...
]
```

- Obtener lista de desarrolladoras

```API
  GET /catalogo/Desarrolladoras/
```

```API
  GET /catalogo/Desarrolladoras/?limit=10
```

```API
  GET /catalogo/Desarrolladoras/?limit=10&offset=10
```

| Parametro | Tipo     | Descripción                                     |
| :-------- | :------- | :---------------------------------------------- |
| `limit`   | `string` | Por defecto viene con un limit de 10 por pagina |
| `offset`  | `string` | El offset determina desde que item empieza      |

Response:

```Response
[
  {
    "id": 0,
    "nombre": "FromSoftware"
  },
  ...
]
```

- Solicitar Recomendaciones

```API
  POST /catalogo/Juegos/recomendations/:titulo/
```

| Parametro | Tipo     | Descripción                                                               |
| :-------- | :------- | :------------------------------------------------------------------------ |
| `titulo`  | `string` | **Requiere**. Es el nombre del juego al cual se solicitan Recomendaciones |

```Response
[
  {
    "id": 584,
    "titulo": "Halo 3: ODST",
    "fecha_Lanzamiento": "2009-09-22",
    "resumen": ///,
    "valoracion": 3.7,
    "numero_Partidas": 7300,
    "numero_jugadores": 57,
    "comprado_no_jugado": 1300,
    "menciones_listas": 824,
    "listas_de_deseos": 273,
    "images": [
      "https://tse3.mm.bing.net/th/id/OIP.xbiUOdKHQKxBdOpA3s4vfQHaEK"
    ],
    "reseñas": 346,
    "generos": [
      ///
    ],
    "plataformas": [
      ///
    ],
    "desarrolladora": [
      ///
    ]
  },... 10 juegos recomendados
]
```

- Crear un Catalogo

```API
  POST /catalogo/Catalogos/create/
```

| Parametro             | Tipo        | Descripción                                                  |
| :-------------------- | :---------- | :----------------------------------------------------------- |
| `Autenticacion Token` | `string`    | **Requiere**. Es el token de autenticacion del usuario       |
| `nombre`              | `string`    | **Requiere**. Es el nombre del catalogo                      |
| `Portada`             | `string`    | Es la url de la imagen de portada, se debe enviar un archivo |
| `Juegos`              | `List<int>` | Es la lista de juegos que se agregaran al catalogo           |

Response:

```Response
{
  "id": 31,
  "Nombre": "Ejemplo",
  "Portada": "CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t",
  "usuario": 1,
  "juegos": [
    0,
    1,
    193
  ]
}
```

- Se agregara un juego especifico al catalogo

```API
  POST /catalogo/Catalogos/usuario/add_juego/:id_catalogo/
```

| Parametro             | Tipo        | Descripción                                                        |
| :-------------------- | :---------- | :----------------------------------------------------------------- |
| `Autenticacion Token` | `string`    | **Requiere**. Es el token de autenticacion del usuario             |
| `id_catalogo`         | `string`    | **Requiere**. Es el id del catalogo al que se le agregara el juego |
| `juego_id`            | `List<int>` | **Requiere**. Es el id del juego a agregar                         |

Response:

```Response
{
  "id": 31,
  "Nombre": "Ejemplo",
  "Portada": "url de la imagen de portada",
  "usuario": 1,
  "juegos": [
    {
      Estructura de un juego
    },
    {
      Estructura de un juego
    }
  ]
}
```

- Se eliminara un juego del catalogo seleccionado

```API
  DELETE /catalogo/Catalogos/usuario/delete_juego/:id_catalogo/:id_juego/
```

| Parametro             | Tipo     | Descripción                                                         |
| :-------------------- | :------- | :------------------------------------------------------------------ |
| `Autenticacion Token` | `string` | **Requiere**. Es el token de autenticacion del usuario              |
| `id_catalogo`         | `string` | **Requiere**. Es el id del catalogo al que se le eliminara el juego |
| `id_juego`            | `String` | **Requiere**. Es el id del juego a eliminar                         |

Response:

```Response
code  202 Accepted
```

- Se eliminara el catalogo seleccionado

```API
  DELETE /catalogo/Catalogos/usuario/delete/:id_catalogo/
```

| Parametro             | Tipo     | Descripción                                            |
| :-------------------- | :------- | :----------------------------------------------------- |
| `Autenticacion Token` | `string` | **Requiere**. Es el token de autenticacion del usuario |
| `id_catalogo`         | `String` | **Requiere**. Es el id del catalogo a eliminar         |

Response:

```Response
code  204 No Content
```

- Muestra los catalogos del usuario

```API
  GET /catalogo/Catalogos/usuario/
```

| Parametro             | Tipo     | Descripción                                            |
| :-------------------- | :------- | :----------------------------------------------------- |
| `Autenticacion Token` | `string` | **Requiere**. Es el token de autenticacion del usuario |

Response:

```Response
[
  {
    "id": 1,
    "Nombre": "Halo",
    "Portada": "https://res.cloudinary.com/du2tpjzke/image/upload/c_fill,g_auto/f_webp,q_auto/v1/CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t",
    "usuario": 1,
    "juegos": [
      {
        "id": 193,
        "titulo": "Halo 3",
        "fecha_Lanzamiento": "2007-09-25",
        "resumen": ///,
        "valoracion": 4.2,
        "numero_Partidas": 13000,
        "numero_jugadores": 120,
        "comprado_no_jugado": 1800,
        "menciones_listas": 1800,
        "listas_de_deseos": 603,
        "images": [
          "https://tse3.mm.bing.net/th/id/OIP.86-cXEaiaGjdRj9pudPLqwHaEK"
        ],
        "reseñas": 691,
        "generos": [
          "Shooter"
        ],
        "plataformas": [
          "Windows PC",
          "Xbox One",
          "Xbox 360"
        ],
        "desarrolladora": [
          "Bungie",
          "Microsoft Game Studios"
        ]
      }
    ]
  }
]
```

- Muestra el catalogo seleccionado del usuario

```API
  GET /catalogo/Catalogos/usuario/:id_catalogo/
```

| Parametro             | Tipo     | Descripción                                            |
| :-------------------- | :------- | :----------------------------------------------------- |
| `Autenticacion Token` | `string` | **Requiere**. Es el token de autenticacion del usuario |
| `id_catalogo`         | `String` | **Requiere**. Es el id del catalogo a mostrar          |

Response:

```Response
{
  "id": 1,
  "Nombre": "Halo",
  "Portada": "https://res.cloudinary.com/du2tpjzke/image/upload/c_fill,g_auto/f_webp,q_auto/v1/CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t",
  "usuario": 1,
  "juegos": [
    {
      "id": 193,
      "titulo": "Halo 3",
      "fecha_Lanzamiento": "2007-09-25",
      "resumen": ///,
      "valoracion": 4.2,
      "numero_Partidas": 13000,
      "numero_jugadores": 120,
      "comprado_no_jugado": 1800,
      "menciones_listas": 1800,
      "listas_de_deseos": 603,
      "images": [
        "https://tse3.mm.bing.net/th/id/OIP.86-cXEaiaGjdRj9pudPLqwHaEK"
      ],
      "reseñas": 691,
      "generos": [
        "Shooter"
      ],
      "plataformas": [
        "Windows PC",
        "Xbox One",
        "Xbox 360"
      ],
      "desarrolladora": [
        "Bungie",
        "Microsoft Game Studios"
      ]
    }
  ]
}

```

- Actualiza el catalogo seleccionado del usuario

```API
  PATCH /catalogo/Catalogos/usuario/update/:id_catalogo/
```

| Parametro             | Tipo        | Descripción                                                  |
| :-------------------- | :---------- | :----------------------------------------------------------- |
| `Autenticacion Token` | `string`    | **Requiere**. Es el token de autenticacion del usuario       |
| `nombre`              | `string`    | Es el nombre del catalogo                                    |
| `Portada`             | `string`    | Es la url de la imagen de portada, se debe enviar un archivo |
| `Juegos`              | `List<int>` | Es la lista de juegos que se agregaran al catalogo           |

Response:

```Response
{
  "id": 1,
  "Nombre": "Halo",
  "Portada": "image/upload/CatalogoJuegos/Portadas/tt6wwojkibqqjtlu3o1t",
  "usuario": 1,
  "juegos": [
    193
  ]
}
```

### Urls Usuarios

/GameVault/Usuario/ es la url base para peticiones de Urls Usuarios, osea que una url de ejemplol es:

```link
  http://localhost:8000/GameVault/Usuario/
```

- Registro del usuario

Los Token tienen un timepo de expiracion de un dia.

```API
  POST /register/
```

| Parametro       | Tipo     | Descripción                                                 |
| :-------------- | :------- | :---------------------------------------------------------- |
| `first_name`    | `string` | **Requiere**. Es el nombre del usuario                      |
| `last_name`     | `string` | **Requiere**. Es el apellido del usuario                    |
| `username`      | `string` | **Requiere**. Es el nombre de la cuenta del usuario         |
| `email`         | `string` | **Requiere**. Es el email del usuario                       |
| `password`      | `string` | **Requiere**. Es la contraseña del usuario                  |
| `image_profile` | `string` | Es la url de la imagen de perfil, se debe enviar un archivo |

Response:

```Response
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxN,
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxN
}
```

- Login del usuario

Los Token tienen un timepo de expiracion de un dia.

```API
  POST /login/
```

| Parametro  | Tipo     | Descripción                                         |
| :--------- | :------- | :-------------------------------------------------- |
| `username` | `string` | **Requiere**. Es el nombre de la cuenta del usuario |
| `password` | `string` | **Requiere**. Es la contraseña del usuario          |

Response:

```Response
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxN,
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxN
}
```

- Perfil del usuario

```API
  GET /profile/
```

| Parametro             | Tipo     | Descripción                                            |
| :-------------------- | :------- | :----------------------------------------------------- |
| `Autenticacion Token` | `string` | **Requiere**. Es el token de autenticacion del usuario |

Response:

```Response
{
  "Usuario": "Spiderman123",
  "Nombre": "Lucius",
  "Apellido": "Johnson",
  "Email": "emailicuenta@gmail.com",
  "Imagen": "Url de la imagen de perfil"
}
```

- Refrescar el Token de acceso

```API
  POST /token/refresh/
```

| Parametro | Tipo     | Descripción                                       |
| :-------- | :------- | :------------------------------------------------ |
| `refresh` | `string` | **Requiere**. Es el token de refresco del usuario |

Response:

```Response
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxN
}
```

- Enviar codigo de verificacion al correo

```API
  POST /email/register/send_code/
```

```API
  POST /email/change_password/send_code/
```

| Parametro  | Tipo     | Descripción                           |
| :--------- | :------- | :------------------------------------ |
| `to_email` | `string` | **Requiere**. Es el email del usuario |

Response:

```Response
{"Mensaje": "Correo enviado correctamente"}
```

- Verificacion del codigo de verificacion

```API
  POST /email/code_verify/
```

| Parametro | Tipo     | Descripción                                |
| :-------- | :------- | :----------------------------------------- |
| `email`   | `string` | **Requiere**. Es el email del usuario      |
| `code`    | `string` | **Requiere**. Es el codigo de verificacion |

Response:

```Response
{"Mensaje": "Correo verificado correctamente"}
```

- Cambio de contraseña

```API
  POST /change_password/
```

| Parametro  | Tipo     | Descripción                                |
| :--------- | :------- | :----------------------------------------- |
| `email`    | `string` | **Requiere**. Es el email del usuario      |
| `code`     | `string` | **Requiere**. Es el codigo de verificacion |
| `password` | `string` | **Requiere**. Es la nueva contraseña       |

Response:

```Response
{"Mensaje": "Contraseña cambiada correctamente"}
```

- Editar usuario

```API
  PATCH /edit_user/
```

| Parametro       | Tipo     | Descripción                                                 |
| :-------------- | :------- | :---------------------------------------------------------- |
| `first_name`    | `string` | Es el nombre del usuario                                    |
| `last_name`     | `string` | Es el apellido del usuario                                  |
| `username`      | `string` | Es el nombre de la cuenta                                   |
| `email`         | `string` | Es el email del usuario                                     |
| `image_profile` | `string` | Es la url de la imagen de perfil, se debe enviar un archivo |

Response:

```Response
{
  "Usuario": "Spiderman123",
  "Nombre": "William",
  "Apellido": "Castillo",
  "Email": "correo del usuario",
  "Imagen": Url de la imagen de perfil
}
```

- Eliminar usuario

```API
  DELETE /delete_user/:id_usuario/
```

| Parametro             | Tipo     | Descripción                                            |
| :-------------------- | :------- | :----------------------------------------------------- |
| `Autenticacion Token` | `string` | **Requiere**. Es el token de autenticacion del usuario |
| `id_usuario`          | `string` | **Requiere**. Es el id del usuario a eliminar          |

Response:

```Response
code  204 No Content
```
