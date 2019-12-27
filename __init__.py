# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import ftplib
import os
"""
    Obtengo el modulo que fue invocado
"""
global ftp
module = GetParams("module")

if module == "conn_ftp":

    server_ = GetParams("server_")
    user_ = GetParams("user_")
    pass_ = GetParams("pass_")
    var_ = GetParams("var_")

    ftp = ftplib.FTP(server_)
    #print(ftp.login(user_,pass_))
    conn = ftp.login(user_,pass_)

    if "OK" in conn:
        res = True
    else:
        res = False

    SetVar(var_,res)

if module == "list_":

    var_ = GetParams("var_")

    files = ftp.nlst()
    files = str(files).replace("'.',","").replace("'..',","").replace(' ','')
    SetVar(var_, files)

if module == "mkdir_":

    dir_ = GetParams("dir_")
    var_ = GetParams("var_")

    new_ = ftp.mkd(dir_)

    res = ftp.nlst()

    if dir_ in res:
        res = True
    else:
        res = False

    SetVar(var_,res)


if module == "go_dir":

    dir_ = GetParams("dir_")
    var_ = GetParams("var_")

    go_ = ftp.cwd(dir_)
    pwd_ = ftp.pwd()

    SetVar(var_,pwd_)

if module == "upload_":

    file_ = GetParams("file_")
    var_ = GetParams("var_")

    filename = os.path.basename(file_)

    f = open(file_, 'rb')
    up = ftp.storbinary('STOR ' + filename + '', f)

    if "successfully" in up:
        res = True
    else:
        res = False

    SetVar(var_,res)

    f.close()

if module == "download_":

    file_ = GetParams("file_")
    path_ = GetParams("path_")
    var_ = GetParams("var_")

    down_ = ftp.retrbinary('RETR ' + file_ + '', open(os.path.join(path_,file_), 'wb').write)

    if "successfully" in down_:
        res = True
    else:
        res = False

    SetVar(var_, res)

if module == "delete_file":

    file_ = GetParams("file_")
    var_ = GetParams("var_")

    del_ = ftp.delete(file_)

    if "Deleted" in del_:
        res = True
    else:
        res = False

    SetVar(var_, res)



