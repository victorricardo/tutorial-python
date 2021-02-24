#!/usr/bin/env python
# coding: utf-8

# # Módulos y Paquetes

# Para facilitar el mantenimiento y la lectura los programas demasiado largos pueden dividirse en módulos, agrupando elementos relacionados.
# 
# Los módulos son entidades que permiten una organización y división lógica de nuestro código. Los ficheros son su contrapartida física: cada archivo Python almacenado en disco equivale a un módulo.

# Vamos a crear nuestro primer módulo entonces creando un pequeño archivo modulo.py con el siguiente contenido:

# In[3]:


#!/usr/bin/env python
# coding: utf-8

def mi_funcion():
  print("una funcion")
class MiClase:
  def __init__(self):
    print ("una clase")

print ("un modulo")


# Si quisiéramos utilizar la funcionalidad definida en este módulo en nuestro programa tendríamos que importarlo. Para importar un módulo se utiliza la palabra clave import seguida del nombre del módulo, que consiste en el nombre del archivo menos la extensión. Como ejemplo, creemos un archivo programa.py en el mismo directorio en el que guardamos el archivo del módulo (esto es importante, porque si no se encuentra en el mismo directorio Python no podrá encontrarlo), con el siguiente contenido:

# In[4]:


import modulo

modulo.mi_funcion()


# La clausula import también permite importar varios módulos en la misma línea. En el siguiente ejemplo podemos ver cómo se importa con una sola clausula import los módulos de la distribución por defecto de Python os, que engloba funcionalidad relativa al sistema operativo; sys, con funcionalidad relacionada con el propio intérprete de Python y time, en el que se almacenan funciones para manipular fechas y horas.

# In[6]:


import os, sys, time

print(time.asctime())


# Sin embargo es posible utilizar la construcción from-import para ahorrarnos el tener que indicar el nombre del módulo antes del objeto que nos interesa. De esta forma se importa el objeto o los objetos que indiquemos al espacio de nombres actual.

# In[7]:


from time import asctime

print(asctime())


# A la hora de importar un módulo Python recorre todos los directorios indicados en la variable de entorno PYTHONPATH en busca de un archivo con el nombre adecuado. El valor de la variable PYTHONPATH se puede consultar desde Python mediante sys.path

# In[8]:


import sys

sys.path


# Por último es interesante comentar que en Python los módulos también son objetos; de tipo module en concreto. Por supuesto esto significa que pueden tener atributos y métodos. Uno de sus atributos, __name__, se utiliza a menudo para incluir código ejecutable en un módulo pero que este sólo se ejecute si se llama al módulo como programa,
# y no al importarlo. Para lograr esto basta saber que cuando se ejecuta el módulo directamente __name__ tiene como valor “__main__”, mientras que cuando se importa, el valor de __name__ es el nombre del módulo:

# In[10]:


print ("Se muestra siempre")
if __name__ == "__main__":
  print ("Se muestra si no es importacion")


# ## Paquetes

# Si los módulos sirven para organizar el código, los paquetes sirven para organizar los módulos. Los paquetes son tipos especiales de módulos (ambos son de tipo module) que permiten agrupar módulos relacionados.
# Mientras los módulos se corresponden a nivel físico con los archivos, los paquetes se representan mediante directorios.

# Para hacer que Python trate a un directorio como un paquete es necesario
# crear un archivo __init__.py en dicha carpeta. En este archivo se pueden definir elementos que pertenezcan a dicho paquete, como una constante DRIVER para el paquete bbdd, aunque habitualmente se tratará
# de un archivo vacío. Para hacer que un cierto módulo se encuentre dentro de un paquete, basta con copiar el archivo que define el módulo al directorio del paquete.
# Como los modulos, para importar paquetes también se utiliza import y from-import y el caracter . para separar paquetes, subpaquetes y módulos.

# In[11]:


# import paq.subpaq.modulo
# paq.subpaq.modulo.func()


# In[ ]:




