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

### Urls catalogo

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

- #### Lista de Juegos

```API
  GET /catalogo/Juegos/
```

```API
  GET /GameVault/catalogo/Juegos/?limit={int}
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

- #### Seleccionar un Juego

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

- #### Solicitar Recomendaciones

```API
  POST /catalogo/Juegos/recomendations/:titulo/
```

| Parametro | Tipo     | Descripción                                                               |
| :-------- | :------- | :------------------------------------------------------------------------ |
| `titulo`  | `string` | **Requiere**. Es el nombre del juego al cual se solicitan Recomendaciones |

- Crear un Catalogo

```API
  POST /catalogo/Catalogos/create/
```

- Se agregara un juego especifico al catalogo

```API
  POST /catalogo/Catalogos/usuario/add_juego/:id/
```

- Se eliminara un juego del catalogo seleccionado

```API
  DELETE /catalogo/Catalogos/usuario/delete_juego/:id_catalogo/:id_juego/
```

- Se eliminara un usuario especifico

```API
  DELETE /catalogo/Catalogos/usuario/delete/(?P<id>\d+)/
```

- Muestra los catalogos del usuario

```API
  GET /catalogo/Catalogos/usuario/
```

- Muestra los catalogos de un usuario en especifico

```API
  GET /catalogo/Catalogos/usuario/(?P<id>\d+)/
```
