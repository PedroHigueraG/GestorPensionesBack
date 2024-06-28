# GestorPensionesBack
Backend del gestor de pensiones desarrollado en FastAPI

## Requisitos

- Python 3.7 o superior
- pip (para instalar paquetes)
- mongodb

## Descarga y Configuración

1. Clona este repositorio:
```
git clone https://github.com/PedroHigueraG/GestorPensionesBack.git cd GestorPensionesBack
```

2. Crea un entorno virtual:
```
python -m venv venv source venv/bin/activate # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```
pip install -r requirements.txt
```

4. Instala MongoDB siguiendo las instrucciones en mongodb.com
   
5. Asegúrate de que MongoDB esté en funcionamiento en `localhost` en el puerto predeterminado (27017)

6. En el proyecto configura el archivo database.py con el puerto donde se está ejecutando mongodb
```
client = AsyncIOMotorClient('mongodb://localhost')
```

7. Configura el archivo .venv con el puerto donde se va a ejecutar el front, ya que este es el que permite el acceso a las peticiones
```
FRONTEND_URL = http://localhost:5173
```

## Ejecución

1. Inicia el servidor:
```
fastapi dev main.py
```

2. Abre tu navegador en http://127.0.0.1:8000/docs para acceder a la documentación interactiva.
