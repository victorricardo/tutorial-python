#!/usr/bin/env python
# coding: utf-8

# # Entrada/Salida Y Ficheros

# En esta lección, además de describir más detalladamente del uso de print para mostrar mensajes al usuario, aprenderemos a utilizar las funciones input y raw_input (python 2) para pedir información, así como los argumentos de línea de comandos y, por último, la entrada/salida de ficheros.

# ## Entrada estándar

# La forma más sencilla de obtener información por parte del usuario es mediante la función raw_input. Esta función toma como parámetrouna cadena a usar como prompt (es decir, como texto a mostrar al usuario pidiendo la entrada) y devuelve una cadena con los caracteres introducidos por el usuario hasta que pulsó la tecla Enter. Veamos un pequeño ejemplo:

# In[2]:


nombre = input("Como te llamas? ")
print ("Encantado, " + nombre)


# Si necesitáramos un entero como entrada en lugar de una cadena, por ejemplo, podríamos utilizar la función int para convertir la cadena a entero, aunque sería conveniente tener en cuenta que puede lanzarse una excepción si lo que introduce el usuario no es un número.

# In[4]:


try:
  edad = input("Cuantos años tienes? ")
  dias = int(edad) * 365
  print ("Has vivido " + str(dias) + " días")
except ValueError:
  print ("Eso no es un numero")


# ## Parámetros de línea de comando

# Además del uso de input y raw_input el programador Python cuenta
# con otros métodos para obtener datos del usuario. Uno de ellos es el uso de parámetros a la hora de llamar al programa en la línea de comandos. Por ejemplo:
# 
# python editor.py hola.txt

# ## Salida estándar

# La forma más sencilla de mostrar algo en la salida estándar es mediante el uso de la sentencia print, como hemos visto multitud de veces en ejemplos anteriores. En su forma más básica a la palabra clave print le sigue una cadena, que se mostrará en la salida estándar al ejecutarse el estamento.

# In[1]:


print ("Hola\n\n\tmundo")


# La sentencia print, o más bien las cadenas que imprime, permiten también utilizar técnicas avanzadas de formateo, de forma similar al sprintf de C. Veamos un ejemplo bastante simple:

# In[5]:


print ("Hola %s" % "mundo")


# Los especificadores más sencillos están formados por el símbolo % seguido de una letra que indica el tipo con el que formatear el valor Por ejemplo:

# ![](imagenes/tabla-01.jpg)

# In[7]:


print ("%10s mundo" % "Hola")
print ("%-10s mundo" % "Hola")


# En el caso de los reales es posible indicar la precisión a utilizar precediendo la f de un punto seguido del número de decimales que queremos mostrar:

# In[10]:


from math import pi

print ("%.7f" % pi)


# La misma sintaxis se puede utilizar para indicar el número de caracteres de la cadena que queremos mostrar

# In[13]:


print ("%.8s" % "hola mundo")


# ## Archivos

# Los ficheros en Python son objetos de tipo file creados mediante la función open (abrir). Esta función toma como parámetros una cadena con la ruta al fichero a abrir, que puede ser relativa o absoluta; una cadena opcional indicando el modo de acceso (si no se especifica se accede en modo lectura) y, por último, un entero opcional para especificar un tamaño de buffer distinto del utilizado por defecto.
# 
# El modo de acceso puede ser cualquier combinación lógica de los siguientes modos:
# 
# - 'r' : read, lectura. Abre el archivo en modo lectura. El archivo tiene que existir previamente, en caso contrario se lanzará una excepción de tipo IOError.
# - 'w' : write, escritura. Abre el archivo en modo escritura. Si el archivo no existe se crea. Si existe, sobreescribe el contenido.
# - 'a' : append, añadir. Abre el archivo en modo escritura. Se diferencia del modo ‘w’ en que en este caso no se sobreescribe el contenido del archivo, sino que se comienza a escribir al final del archivo.
# - 'b' : binary, binario.
# - '+' : permite lectura y escritura simultáneas.
# - 'U' : universal newline, saltos de línea universales. Permite trabajar con archivos que tengan un formato para los saltos de línea que no coincide con el de la plataforma actual (en Windows se utiliza el caracter CR LF, en Unix LF y en Mac OS CR).

# In[21]:


f = open("archivos/archivo.txt", "r")


# Tras crear el objeto que representa nuestro archivo mediante la función open podremos realizar las operaciones de lectura/escritura pertinentes utilizando los métodos del objeto que veremos en las siguientes secciones.
# Una vez terminemos de trabajar con el archivo debemos cerrarlo utilizando el método close.

# In[22]:


while True:
  linea = f.readline()
  if not linea: break
  print (linea)


# In[23]:


f.close()


# ## Escritura de archivos

# Para la escritura de archivos se utilizan los método write y writelines. Mientras el primero funciona escribiendo en el archivo una cadena de texto que toma como parámetro, el segundo toma como parámetro una lista de cadenas de texto indicando las líneas que queremos escribir en el fichero.

# In[28]:


title = 'Days of the Week\n'
path = 'archivos/days.txt'
days_file = open(path,'w')
days_file.write(title)
days_file.close()


# In[29]:


path = 'archivos/days.txt'
days_file = open(path,'r')
days = days_file.read()
print(days)
days_file.close()


# In[ ]:




