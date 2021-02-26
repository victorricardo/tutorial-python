#!/usr/bin/env python
# coding: utf-8

# ## Cliente en Python
# 
# Ahora el código del cliente, también con comentarios.

# In[ ]:


# Importamos las librerias necesarias
import socket

# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5001 # Puerto de comunicacion
# Realizamos la conexion al la IP y puerto
sock.connect(('localhost',port))
# Leemos los datos del servidor
data = sock.recv(4096)
# Cerramos el socket
sock.close()
# Mostramos los datos recibidos
print(data.decode())





