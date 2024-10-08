# FTP
  
Conecta y gestiona un servidor FTP  

*Read this in other languages: [English](Manual_ftp_.md), [Português](Manual_ftp_.pr.md), [Español](Manual_ftp_.es.md)*
  
![banner](imgs/Banner_ftp_.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar con FTP
  
Conectar con FTP para gestionarlo con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Servidor|Dirección del servidor FTP|test.ftp.com|
|Puerto|Puerto del servidor FTP|5518|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|
|Usuario|Usuario del servidor FTP|user@test.com|
|Contraseña|Contraseña del usuario del servidor FTP|******|
|TLS|Activar TLS|True|
|Codificación|Codificación del servidor FTP|utf-8|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|result|

### Listar directorio
  
Lista el directorio del FTP en una variable de Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Guardar resultado en variable|Variable donde se guardará el resultado|Variable|

### Crear directorio
  
Crear directorio en la ruta actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de directorio|Nombre del directorio a crear|test|
|Asignar resultado a variable|Variable donde se almacenará el resultado|Variable|

### Ir a directorio
  
Ir a directorio especificado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de directorio|Nombre del directorio al cual acceder|test|
|Guardar directorio actual en variable|Nombre de la variable donde se guardará el directorio actual|Variable|

### Subir archivo
  
Subir archivo a directorio actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo a subir|Archivo que se subirá al directorio ftp|C:\Users\Usuario\Desktop\test.png|
|Tiempo de espera|Tiempo de espera máximo en segundos|10|
|Asignar resultado en variable|Variable donde se guardará el resultado|Variable|

### Descargar archivo
  
Descarga el archivo seleccionado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de archivo a descargar|Nombre del archivo que se descargará desde el directorio ftp|test.png|
|Ruta donde descargar|Ruta donde se descargará el archivo|C:\Users\Usuario\Desktop|
|Asignar resultado en variable|Asigna el resultado de la descarga a la variable seleccionada|Variable|

### Descargar directorio
  
Descarga el directorio actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta donde descargar|Ruta donde se descargará el directorio actual|C:/Users/User/Desktop|
|Incluir subdirectorios|Si se marca, se incluirán los subdirectorios en la descarga de manera recursiva|False|
|Asignar resultado en variable|Asigna el resultado de la descarga a la variable seleccionada|Variable|

### Eliminar archivo
  
Eliminar archivo en directorio actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de archivo a eliminar|Nombre de archivo que se eliminará del directorio actual|test.png|
|Asignar resultado en variable|Variable donde se almacenará el resultado de la operación|Variable|

### Cerrar Conexión
  
Cierra la conexión FTP
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
