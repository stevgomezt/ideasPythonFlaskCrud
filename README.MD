* Instalar nodejs
* Instalar python

* Habilitar la ejecucion de scripts desde power shell Set-ExecutionPolicy RemoteSigned

* Crear entorno virtual
    - dentro de la ruta del proyecto abrir consola y ejecutar pip install virtualenv
    - virtualenv venv

* Crear archivo requirements.txt

* Activar entorno virtual \venv\Scripts\activate
    - instalar dependencias pip install -r requirements.txt
    - pip freeze sirve para ver todas las dependencias instaladas

* Setear variables
    - set FLASK_APP=main.py
    - set FLASK_DEBUG=1
    - set FLASK_ENV=development
    - flask run`