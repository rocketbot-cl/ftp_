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
import socket


"""
    Obtengo el modulo que fue invocado
"""
global ftp_connection
module = GetParams("module")

class FTP_Connection:
    def __init__(self, server, port, user, pwd, tls, directory="", encoding="utf-8"):
        self.server = server
        self.port = port
        self.user = user
        self.pwd = pwd
        self.tls = tls
        self.dir = directory
        self.encoding = encoding

    def config(self):
        import ssl
        global ImplicitFTP_TLS, ftplib, ftp_connect, socket, FTP_TLS_RB, FTP_RB
        
        if self.tls:
            try:
                print("Trying first tls connection")
                ftp = ImplicitFTP_TLS()
                ftp_connect(ftp, self.server, self.port)
                ftp.af = socket.AF_INET6
                ftp.encoding = self.encoding
            except:
                print("Trying second tls connection")
                ftp = FTP_TLS_RB()
                ftp.debugging = 2
                ftp.ssl_version = ssl.PROTOCOL_SSLv23
                ftp.encoding = self.encoding
                ftp_connect(ftp, self.server, self.port)
                ftp.auth()
            ftp.prot_p()
        else:
            ftp = FTP_RB()
            ftp.ssl_version = ssl.PROTOCOL_SSLv23
            ftp_connect(ftp, self.server, self.port)
        return ftp
        
    def move_to_dir(self, directory=""):
        if directory == "..":
            self.dir = "/".join(self.dir.split("/")[:-1])
        else:
            self.dir += "/" +directory

class FTP_TLS_RB(ftplib.FTP_TLS):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None, timeout=999999999):
            """Store a file in binary mode.  A new port is created for you.

                Args:
                cmd: A STOR command.
                fp: A file-like object with a read(num_bytes) method.
                blocksize: The maximum data size to read from fp and send over
                            the connection at once.  [default: 8192]
                callback: An optional single parameter callable that is called on
                            each block of data after it is sent.  [default: None]
                rest: Passed to transfercmd().  [default: None]

                Returns:
                The response code.
                """
            import time

            self.voidcmd('TYPE I')
            with self.transfercmd(cmd, rest) as conn:
                ProcessTime = time.perf_counter
                start = ProcessTime()
                t = 0
                while t - start <= timeout:
                    buf = fp.read(blocksize)
                    if not buf:
                        break
                    conn.sendall(buf)
                    if callback:
                        callback(buf)
                    t = ProcessTime()
                # shutdown ssl layer
                if ftplib._SSLSocket is not None and isinstance(conn, ftplib._SSLSocket):
                    conn.unwrap()
            return self.voidresp()

class FTP_RB(ftplib.FTP):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None, timeout=999999999):
            """Store a file in binary mode.  A new port is created for you.

                Args:
                cmd: A STOR command.
                fp: A file-like object with a read(num_bytes) method.
                blocksize: The maximum data size to read from fp and send over
                            the connection at once.  [default: 8192]
                callback: An optional single parameter callable that is called on
                            each block of data after it is sent.  [default: None]
                rest: Passed to transfercmd().  [default: None]

                Returns:
                The response code.
                """
            import time

            self.voidcmd('TYPE I')
            with self.transfercmd(cmd, rest) as conn:
                ProcessTime = time.perf_counter
                start = ProcessTime()
                t = 0
                while t - start <= timeout:
                    buf = fp.read(blocksize)
                    if not buf:
                        break
                    conn.sendall(buf)
                    if callback:
                        callback(buf)
                    t = ProcessTime()
                    
                # shutdown ssl layer
                if ftplib._SSLSocket is not None and isinstance(conn, ftplib._SSLSocket):
                    conn.unwrap()
            return self.voidresp()

class ImplicitFTP_TLS(ftplib.FTP_TLS):
        """FTP_TLS subclass that automatically wraps sockets in SSL to support implicit FTPS."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._sock = None

        @property
        def sock(self):
            """Return the socket."""
            return self._sock

        @sock.setter
        def sock(self, value):
            import ssl
            """When modifying the socket, ensure that it is ssl wrapped."""
            if value is not None and not isinstance(value, ssl.SSLSocket):
                value = self.context.wrap_socket(value)
            self._sock = value

        def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None, timeout=999999999):
            """Store a file in binary mode.  A new port is created for you.

                Args:
                cmd: A STOR command.
                fp: A file-like object with a read(num_bytes) method.
                blocksize: The maximum data size to read from fp and send over
                            the connection at once.  [default: 8192]
                callback: An optional single parameter callable that is called on
                            each block of data after it is sent.  [default: None]
                rest: Passed to transfercmd().  [default: None]

                Returns:
                The response code.
                """
            import time

            self.voidcmd('TYPE I')
            with self.transfercmd(cmd, rest) as conn:
                ProcessTime = time.perf_counter
                start = ProcessTime()
                t = 0
                while t - start <= timeout:
                    buf = fp.read(blocksize)
                    if not buf:
                        break
                    conn.sendall(buf)
                    if callback:
                        callback(buf)
                    t = ProcessTime()
                # shutdown ssl layer
                if ftplib._SSLSocket is not None and isinstance(conn, ftplib._SSLSocket):
                    conn.unwrap()
            return self.voidresp()
            
def ftp_connect(ftp, server, port):
        if port:
            ftp.connect(server, int(port))
        else:

            ftp.connect(server)


if module == "conn_ftp":

    server_ = GetParams("server_")
    port = GetParams("port")
    user_ = GetParams("user_")
    pass_ = GetParams("pass_")
    tls = GetParams("tls")
    encoding = GetParams("encoding_") if GetParams("encoding_") else "utf-8"
    var_ = GetParams("var_")
    if tls is not None:
        tls = eval(tls)
    try:
        ftp_connection = FTP_Connection(server_, port, user_, pass_, tls, encoding=encoding)
        ftp = ftp_connection.config()
        conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
        res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "list_":
    var_ = GetParams("var_")
    
    try:
        ftp = ftp_connection.config()
        conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
        if ftp_connection.dir:
            go_ = ftp.cwd(ftp_connection.dir)
            pwd_ = ftp.pwd()

        files = ftp.nlst()
        print('FILES', files)
        files = [file.replace("'.',", "").replace("'..',", "") for file in files] 

        #files = str(files).replace("'.',", "").replace("'..',", "")
        SetVar(var_, files)
    except Exception as e:
        PrintException()
        raise e

if module == "mkdir_":

    dir_ = GetParams("dir_")
    var_ = GetParams("var_")

    ftp = ftp_connection.config()
    conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
    if ftp_connection.dir:
        go_ = ftp.cwd(ftp_connection.dir)
        pwd_ = ftp.pwd()

    new_ = ftp.mkd(dir_)

    res = ftp.nlst()

    if dir_ in res:
        res = True
    else:
        res = False

    SetVar(var_, res)

if module == "go_dir":
    dir_ = GetParams("dir_")
    var_ = GetParams("var_")

    ftp = ftp_connection.config()
    conn = ftp.login(ftp_connection.user, ftp_connection.pwd)

    ftp_connection.move_to_dir(dir_)
    

    
    go_ = ftp.cwd(ftp_connection.dir)
    pwd_ = ftp.pwd()

    SetVar(var_, pwd_)

if module == "upload_":

    file_ = GetParams("file_")
    var_ = GetParams("var_")
    timeout = GetParams("timeout")
    from time import sleep

    try:
        ftp = ftp_connection.config()
        conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
        if ftp_connection.dir:
            go_ = ftp.cwd(ftp_connection.dir)
            pwd_ = ftp.pwd()

        filename = os.path.basename(file_)

        try: 
            ftplib._SSLSocket = None
            global totalSize
            totalSize = os.path.getsize(file_)
            global sizeWritten
            sizeWritten = 0
            def handle(block):
                global sizeWritten, totalSize
                sizeWritten += 8192
                percentComplete = round((sizeWritten / totalSize) * 100)
                print(str(percentComplete) + "% complete remaining: " + str(totalSize - sizeWritten), flush=True)
            with open(file_, 'rb') as f:
                if timeout is not None:
                    up = ftp.storbinary('STOR ' + filename + '', f, timeout=int(timeout))
                else:
                    up = ftp.storbinary('STOR ' + filename + '', f)
        except:
            ftp = ftp_connection.config()
            conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
            if ftp_connection.dir:
                go_ = ftp.cwd(ftp_connection.dir)
                pwd_ = ftp.pwd()
            

            with open(file_, 'rb') as f:
                up = ftp.storbinary('STOR ' + filename + '', f)
#            up = ftp.storbinary('STOR ' + filename + '', f)

        res = True
    
    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "download_":

    file_ = GetParams("file_")
    path_ = GetParams("path_")
    var_ = GetParams("var_")

    try:

        ftp = ftp_connection.config()
        conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
        ftp.set_debuglevel(2)
        print(file_, "dir", ftp_connection.dir)
        if ftp_connection.dir:
            go_ = ftp.cwd(ftp_connection.dir)
            pwd_ = ftp.pwd()
        #ftp.retrlines("LIST -a")
        down_ = ftp.retrbinary('RETR ' + file_ + '', open(os.path.join(path_, file_), 'wb').write)
        
        res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "delete_file":
    file_ = GetParams("file_")
    var_ = GetParams("var_")

    try:

        ftp = ftp_connection.config()
        conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
        if ftp_connection.dir:
            go_ = ftp.cwd(ftp_connection.dir)
            pwd_ = ftp.pwd()
        
        del_ = ftp.delete(file_)
        res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)


if module == "close_conn":

    try:
        ftp = ftp_connection.config()
        conn = ftp.login(ftp_connection.user, ftp_connection.pwd)
        ftp.close()
    except Exception as e:
        PrintException()
        raise e