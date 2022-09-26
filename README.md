# Aguinaldo Bot
> Un simple bot de Twitter que contabiliza los dias restantes para cobrar aguinaldo

Este bot está creado en Python haciendo uso de ```tweepy```, un modulo que permite conectar con la API oficial de Twitter de forma sencilla. Vi la idea en un intercambio entre dos usuarios de Twitter y dije ¿por qué no?

Pueden ver una demo funcional [clickeando acá](https://twitter.com/CuandoAguinaldo). 

# Requisitos
Esta guia asume que tenes tu poder una cuenta de Developer en Twitter y las llaves de acceso correspondiente para poder interactuar con la API.

Para poder ejecutar correctamente este bot, necesitamos seguir unos sencillos pasos. 

> 1. Crear un entorno virtual
> 2. Instalar las dependencias necesarias
> 3. Crear un archivo .env donde guardaremos las credenciales
> 4. Corriendo el bot
> 5. Opcional: crear la imagen para Docker y desplegarla.  

# 1. Crear un entorno virtual
Es muy sencillo. En este caso vamos a usar virtualenv, pero podes usar el que más se adapte a tus necesidades. 
```
python3 -m venv venv
```

**Nota:** El "venv" al final del comando puede ser cambiado por un nombre personalizado. Este será el nombre de la carpeta donde se contenga el entorno virtual.
# 2. Instalar las dependencias necesarias
Tenemos un archivo `requirements.txt` donde se guardan las dependencias necesarias e instalarlo es tan sencillo como ejecutar el siguiente código.
Por supuesto, necesitamos previamente activar el entorno virtual que recien creamos.

>Activando el entorno virtual en Windows, ejecutamos :
```
venv/Scripts/activate
```

>Unix/MacOS
```
source venv/bin/activate
```

>Una vez activado el entorno, podemos proceder a instalar las dependencias usando pip.
```
pip install -r requirements.txt
```
# 3. Creando el archivo .env
Para no exponer nuestras credenciales en el código decidí usar un archivo `.env` para almacenarlas. Por supuesto, si este metodo no es cómodo para tu uso podes modificarlo a tu gusto.

> Creamos el archivo .env con la siguiente estructura
```
API_KEY=
API_KEY_SECRET=
ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=
```

# 4. Arrancando el bot
Una vez todos los requisitos fueron cumplidos, basta iniciar el comando parandose en la carpeta raiz y ejecutando
```
python3 src/main.py
```
Si la ejecución es satisfactoria, se imprirá un mensaje en pantalla indicandolo.

# 5. Opcional - Creando la imagen para Docker
Si tenes intenciones hacer un proyecto similar y correrlo en un entorno Docker, ya se provee el archivo Dockerfile para construirlo de forma sencilla. Además, está agregado un crontab para poder automatizar la ejecución del archivo, cada día a las 5 p.m (20 hrs UTC).

1. Creando la imagen en base al Dockerfile
```
docker build -t NombreImagen .
```
2. Corriendo la imagen
```
docker run -d NombreImagen
```

Adicionalmente, se puede crear un volumen para mantener el archivo `aguinaldos.json` por fuera del contendor, es quien guarda las fechas aproximadas de los cobros. Un algoritmo se encagará de actualizar la fecha un año hacia adelante, 