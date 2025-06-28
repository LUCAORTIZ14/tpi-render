INSTALACIÓN
1- Crear un carpeta llamada TP5.
2- Ingresar a Visual Studio Code y abrir la carpeta TP5.
3- Ejecutar en el terminal de Visual Studio Code dentro de la caperta TP5: "git clone https://github.com/sistemasfm/Tpi5LabIV.git ."       Ejecutarlo sin las comillas y con el punto al final. El punto al final es para clonar en la carpeta actual.
4- Dentro de la misma carpeta TP5 crear el entorno virtual con: python -m venv venv.
5- Activar el entorno virtual con .\venv\Scripts\activate desde la terminal de Visual Studio code.
6- Instalar las dependencias con pip install -r requirements.txt.
7- Crear la base de datos, actualizar nombre y credenciales en archivo /config/database.py  
8- Correr uvicorn main:app --reload
9- Ingresar a http://127.0.0.1:8000/docs y dar de alta un usuario.
10- Ingresar a http://127.0.0.1:8000/ para ingresar al sitio.
