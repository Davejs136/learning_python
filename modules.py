import os, sys, time

def p(arg):
  return print(arg)

""" OS module """

# Devuelve si es posible acceder al archivo/directorio
# os.access(ruta, modo-acceso)
p(os.access('./paquetes', 1))

# Devuelve el directorio actual
p(os.getcwd())

# Cambia directorio trabajo
# os.chdir('/dir1/dir2')  

# Cambia permisos a un archivo
# os.chmod(path, mode)

# Cambia propietario de un archivo 
# os.chown(path, uid, gid)

# Cambia al directorio raíz
# os.chroot(path)
# os.chroot('./basic')

# Devuelve numero de CPUs del sistema
p(os.cpu_count())

# Devuelve el directorio actual
p(os.curdir)

# Devuelve el directorio padre
p(os.pardir)

# Devuelve nombre del archivo del terminal
p(os.ctermid())

# Devuelve ruta del dispositivo nulo
p(os.devnull)

# Devuelve diccionario con variables de entorno
# p(os.environ.items())

# Devuelve id usuario real del proceso actual (Unix)
p(os.getuid())

# Devuelve id grupo real del proceso actual (Unix)
p(os.getgid())