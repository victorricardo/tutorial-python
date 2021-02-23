#!/usr/bin/env python
# coding: utf-8

# # Colecciones - Listas

# In[1]:


l = [22, True, "una lista", [1, 2]]
mi_var = l[0] # mi_var vale 22
mi_var1 = l[3] # mi_var1 vale [1, 2]
print (mi_var)
print (mi_var1)


# In[50]:


# Si queremos acceder a un elemento de una lista incluida dentro de otra lista tendremos que 
# utilizar dos veces este operador
l = ["una lista", [1, 2]]
mi_var = l[1][0] # mi_var vale 1
print (mi_var)


# In[51]:


# También podemos utilizar este operador para modificar un elemento de la lista si lo colocamos en la parte izquierda 
# de una asignación
l = [22, True]
l[0] = 99 # Con esto l valdrá [99, True]
print (l)


# In[52]:


# Una curiosidad sobre el operador [] de Python es que podemos utilizar también números negativos. Si se utiliza un número 
# negativo como índice, esto se traduce en que el índice empieza a contar desde el final, hacia la izquierda; es decir, 
# con [-1] accederíamos al último elemento de la lista, con [-2] al penúltimo, con [-3], al antepenúltimo, y así 
# sucesivamente.
l = [22, True, "una lista", [1, 2], "antepenúltimo", "penúltimo",  "último"]
print (l[-1]) # último
print (l[-2]) # penúltimo
print (l[-3]) # antepenúltimo


# In[53]:


# Otra cosa inusual es lo que en Python se conoce como slicing o particionado, y que consiste en ampliar este mecanismo 
# para permitir seleccionar porciones de la lista. Si en lugar de un número escribimos dos números inicio y fin separados 
# por dos puntos (inicio:fin) Python interpretará que queremos una lista que vaya desde la posición inicio a la posición 
# fin, sin incluir este último. Si escribimos tres números (inicio:fin:salto) en lugar de dos, el tercero se utiliza para 
# determinar cada cuantas posiciones añadir un elemento a la lista.
l = [99, True, "una lista", [1, 2]]
mi_var = l[0:2] # mi_var vale [99, True]
print (mi_var)
mi_var = l[0:4:2] # mi_var vale [99, "una lista"]
print (mi_var)


# In[54]:


# Hay que mencionar así mismo que no es necesario indicar el principio y el final del slicing, sino que, si estos se 
# omiten, se usarán por defecto las posiciones de inicio y fin de la lista, respectivamente:
l = [99, True, "una lista"]
mi_var = l[1:] # mi_var vale [True, "una lista"]
print (mi_var)
mi_var = l[:2] # mi_var vale [99, True]
print (mi_var)
mi_var = l[:] # mi_var vale [99, True, "una lista"]
print (mi_var)
mi_var = l[::2] # mi_var vale [99, "una lista"]
print (mi_var)


# In[55]:


# También podemos utilizar este mecanismo para modificar la lista:
l = [99, True, "una lista", [1, 2]]
l[0:2] = [0, 1] # l vale [0, 1, "una lista", [1, 2]]
print (l)


# # Colecciones - Tuplas

# In[57]:


# Todo lo que hemos explicado sobre las listas se aplica también a las tuplas, a excepción de la forma de definirla, 
# para lo que se utilizan paréntesis en lugar de corchetes.
t = (1, 2, True, "python")
print (t)


# # Colecciones - Diccionarios

# In[59]:


# Los diccionarios, también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una clave y
# un valor. Por ejemplo, veamos un diccionario de películas y directores:
d = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}

# La diferencia principal entre los diccionarios y las listas o las tuplas es que a los valores almacenados en un 
# diccionario se les accede no por su índice, porque de hecho no tienen orden, sino por su clave, utilizando de nuevo 
# el operador [].
mi_var = d["Love Actually"] # devuelve "Richard Curtis"
print (mi_var)

# Al igual que en listas y tuplas también se puede utilizar este operador para reasignar valores.
d["Kill Bill"] = "Quentin Tarantino"
mi_var = d["Kill Bill"] # devuelve "Quentin Tarantino"
print (mi_var)

