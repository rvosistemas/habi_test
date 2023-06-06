# Prueba técnica sobre un Microservicio REST
Estructura de carpetas:

microservicio/  
├── app/  
│ ├── init.py  
│ ├── config/  
│ │ ├── init.py    
│ │ └── ...  
│ ├── controllers/  
│ │ ├── init.py  
│ │ └── ...  
│ ├── models/  
│ │ ├── init.py  
│ │ └── ...  
│ ├── routes/  
│ │ ├── init.py  
│ │ └── ...  
│ └── utils/  
│ ├── init.py  
│ └── ...  
├── tests/  
│ ├── init.py  
│ └── ...  
├── .env  
├── requirements.txt  
├── README.md  
└── app.py  
└── Makefile.py  
└── LICENSE.txt  

- La carpeta `app/` contiene la lógica principal de la aplicación:
  - `controllers/` contiene los controladores que manejan la lógica de negocio de cada ruta del microservicio.
  - `models/` contiene los modelos de datos o estructuras de objetos utilizados en el microservicio.
  - `routes/` contiene los archivos que definen las rutas del microservicio y asocian las funciones de controlador correspondientes.
  - `utils/` contiene módulos de utilidades compartidas utilizados en la aplicación.

- La carpeta `tests/` contiene los archivos de pruebas para realizar pruebas unitarias y de integración en el microservicio.

- El archivo `.env` contiene variables de entorno específicas de la aplicación.

## Desarrollo
En el siguiente microservicio se usara fastapi, con la estructura de carpetas anteriormente expuesta.

## Ejecución
Para ejecutar la aplicación, sigue los siguientes pasos:

Se debe tener instalado python el sistemas y crear un entorno virtual con: `python -m venv .venv`

y luego activa dicho entorno: `pip install -r requirements.txt`

Instala las dependencias del proyecto ejecutando el siguiente comando en **linux**: ` source /venv/bin/activate`

Instala las dependencias del proyecto ejecutando el siguiente comando en **windows**: `source .venv/Scripts/activate`

Configura las variables de entorno en el archivo .env.

Ejecuta el siguiente comando para iniciar la aplicación:
`python app.py` 

## Pruebas unitarias
Ejecuta el siguiente comando para iniciar los test, esto esta configurado en el archivo **Makefile**:

si es un sistema operativo **linux**:
`make linux-coverage-app` 

si es un sistema operativo **windows**:
`make windows-coverage-app`

## Pruebas de aplicación
En la dirección **localhost:8000/docs** se encuentra la documentación de la api, en la cual se puede probar los endpoints, usando openapi.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Likes
Para agregar un sistema de likes, se debe crear una tabla en la base de datos, los detalles están el archivo **Diagram.drawio**.

## Segundo ejercicio
Para el segundo ejercicio, se debe ejecutar el archivo **segundo_ejercicio.py** con el siguiente comando:
`python segundo_ejercicio.py` 

Aparecerá una pequeña interfaz para ingresar los arreglos y comprobar los resultados.