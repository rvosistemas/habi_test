# Prueba tecnica HABI sobre un Microservicio REST

Estructura de carpetas:

microservicio/  
├── app/  
│ ├── init.py  
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
├── config/  
│ ├── init.py  
│ ├── settings.py  
│ └── ...  
├── tests/  
│ ├── init.py  
│ └── ...  
├── .env  
├── requirements.txt  
├── README.md  
└── app.py  

Aquí está la descripción de cada carpeta y archivo:

- La carpeta `app/` contiene la lógica principal de la aplicación:
  - `controllers/` contiene los controladores que manejan la lógica de negocio de cada ruta del microservicio.
  - `models/` contiene los modelos de datos o estructuras de objetos utilizados en el microservicio.
  - `routes/` contiene los archivos que definen las rutas del microservicio y asocian las funciones de controlador correspondientes.
  - `utils/` contiene módulos de utilidades compartidas utilizados en la aplicación.

- La carpeta `config/` contiene la configuración de la aplicación:
  - `settings.py` contiene la configuración general de la aplicación, como variables de entorno y ajustes específicos.

- La carpeta `tests/` contiene los archivos de pruebas para realizar pruebas unitarias y de integración en el microservicio.

- El archivo `.env` (opcional) contiene variables de entorno específicas de la aplicación.

- El archivo `requirements.txt` enumera todas las dependencias del proyecto.

- El archivo `README.md` es un archivo de documentación que describe el microservicio y proporciona instrucciones para ejecutarlo y utilizarlo.

- El archivo `app.py` es el punto de entrada principal de la aplicación que inicializa el servidor y las configuraciones.

## Desarrollo
En el siguiente microservicio no se usaran frameworks, con la estructura de carpetas anteriormente expuesta.
