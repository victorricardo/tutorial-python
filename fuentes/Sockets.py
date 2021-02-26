#!/usr/bin/env python
# coding: utf-8

# ## Servidor en Python
# 
# Aquí les dejo el código con comentarios para hacer mas fácil la comprensión.

# In[ ]:


# Importamos las librerias necesarias
import socket

# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000 # Puerto de comunicacion
sock.bind(('localhost',port)) # IP y Puerto de conexion en una Tupla

print ("esperando conexiones en el puerto ", port)
# Vamos a esperar que un cliente se conecte
# Mientras tanto el script se va a pausar
sock.listen(1)
# Cuando un cliente se conecte vamos a obtener la client_addr osea la direccion
# tambien vamos a obtener la con, osea la conexion que servira para enviar datos y recibir datos
con, client_addr =  sock.accept()
text = "Hola, soy el servidor!" # El texto que enviaremos
con.send(text.encode()) # Enviamos el texto al cliente que se conecta

con.close() # Cerramos la conexion
sock.close() # Cerramos el socket


# ## Cliente en Python
# 
# Ahora el código del cliente, también con comentarios.

# In[ ]:


# Importamos las librerias necesarias
import socket

# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000 # Puerto de comunicacion
# Realizamos la conexion al la IP y puerto
sock.connect(('localhost',port))
# Leemos los datos del servidor
data = sock.recv(4096)
# Cerramos el socket
sock.close()
# Mostramos los datos recibidos
print(data.decode())


# In[ ]:




