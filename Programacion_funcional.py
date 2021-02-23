#!/usr/bin/env python
# coding: utf-8

# # Programación funcional

# La programación funcional es un paradigma en el que la programaciónse basa casi en su totalidad en funciones, entendiendo el concepto de función según su definición matemática, y no como los simples subprogramas de los lenguajes imperativos que hemos visto hasta ahora.
# 
# En los lenguajes funcionales puros un programa consiste exclusivamente en la aplicación de distintas funciones a un valor de entrada para obtener un valor de salida.
# 
# Python, sin ser un lenguaje puramente funcional incluye varias características
# tomadas de los lenguajes funcionales como son las funciones de orden superior o las funciones lambda (funciones anónimas).

# ## Funciones de orden superior

# In[2]:


# El concepto de funciones de orden superior se refiere al uso de funciones como si de un valor cualquiera se 
# tratara, posibilitando el pasar funciones como parámetros de otras funciones o devolver funciones como valor de retorno.
# Esto es posible porque, como hemos insistido ya en varias ocasiones, en Python todo son objetos. Y las funciones 
# no son una excepción.

# Veamos un pequeño ejemplo

def saludar(lang):
  def saludar_es():
    print ('Hola')
    
  def saludar_en():
    print ('Hi')
    
  def saludar_fr():
    print ('Salut')
    
  lang_func = {'es': saludar_es,
               'en': saludar_en,
               'fr': saludar_fr}
  return lang_func[lang]

f = saludar('es')
f()
saludar('en')()
saludar('fr')()


# ## Iteraciones de orden superior sobre listas
# 
# Una de las cosas más interesantes que podemos hacer con nuestras funciones de orden superior es pasarlas como argumentos de las funciones map, filter y reduce. Estas funciones nos permiten sustituir los bucles típicos de los lenguajes imperativos mediante construcciones equivalentes.

# ## map(function, sequence[, sequence, ...])
# 
# La función map aplica una función a cada elemento de una secuencia y devuelve una lista con el resultado de aplicar la función a cada elemento.
# 
# Si se pasan como parámetros n secuencias, la función tendrá que aceptar n argumentos. Si alguna de las secuencias es más pequeña que las demás, el valor que le llega a la función function para posiciones mayores que el tamaño de dicha secuencia será None.
# 
# A continuación podemos ver un ejemplo en el que se utiliza map para elevar al cuadrado todos los elementos de una lista:

# In[4]:


def cuadrado(n):
  return n ** 2

l = [1, 2, 3]
l2 = map(cuadrado, l)
print(list(l2))


# ## filter(function, sequence)
# 
# La funcion filter verifica que los elementos de una secuencia cumplan una determinada condición, devolviendo una secuencia con los elementos que cumplen esa condición. Es decir, para cada elemento de sequence se aplica la función; si el resultado es True se añade a la lista y en caso contrario se descarta.
# 
# A continuación podemos ver un ejemplo en el que se utiliza filter para conservar solo los números que son pares.

# In[6]:


def es_par(n):
  return (n % 2.0 == 0)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = filter(es_par, l)
print(list(l2))


# ## reduce(function, sequence[, initial])
# 
# La función reduce aplica una función a pares de elementos de una secuencia hasta dejarla en un solo valor.
# 
# A continuación podemos ver un ejemplo en el que se utiliza reduce para sumar todos los elementos de una lista.

# In[9]:


# Is reduce really removed in Python 3.2, It was moved to functools.
from functools import reduce

def sumar(x, y):
  return x + y

l = [1, 2, 3]
l2 = reduce(sumar, l)
print(l2)


# ## Funciones lambda

# El operador lambda sirve para crear funciones anónimas en línea. Al ser funciones anónimas, es decir, sin nombre, estas no podrán ser referenciadas más tarde.
# 
# Las funciones lambda se construyen mediante el operador lambda, los parámetros de la función separados por comas (atención, SIN paréntesis), dos puntos (:) y el código de la función.
# 
# Esta construcción podrían haber sido de utilidad en los ejemplos anteriores para reducir código. El programa que utilizamos para explicar filter, por ejemplo, podría expresarse así:

# In[3]:


l = [1, 2, 3]
l2 = filter(lambda n: n % 2.0 == 0, l)
print(list(l2))


# Comparemoslo con la versión anterior:

# In[4]:


def es_par(n):
  return (n % 2.0 == 0)

l = [1, 2, 3]
l2 = filter(es_par, l)
print(list(l2))


# ## Comprensión de listas

# En Python 3000 map, filter y reduce perderán importancia. Y aunque estas funciones se mantendrán, reduce pasará a formar parte del módulo functools, con lo que quedará fuera de las funciones disponibles por defecto, y map y filter se desaconsejarán en favor de las list comprehensions o comprensión de listas.
# 
# Veamos un ejemplo de cómo se podría utilizar la comprensión de listas para elevar al cuadrado todos los elementos de una lista, como hicimos en nuestro ejemplo de map.

# In[6]:


l = [1, 2, 3]
l2 = [n ** 2 for n in l]
print(list(l2))


# El ejemplo que utilizamos para la función filter (conservar solo los números que son pares) se podría expresar con comprensión de listas así:

# In[8]:


l = [1, 2, 3, 4]
l2 = [n for n in l if n % 2.0 == 0]
print(list(l2))


# Veamos por último un ejemplo de compresión de listas con varias clausulas for:

# In[10]:


l = [0, 1, 2, 3]
m = ['a', 'b']
n = [s * v for s in m
           for v in l
           if v > 0]
print(list(n))


# Esta construcción sería equivalente a una serie de for-in anidados:

# In[11]:


l = [0, 1, 2, 3]
m = ['a', 'b']
n = []
for s in m:
  for v in l:
    if v > 0:
      n.append(s* v)
print(list(n))    


# ## Generadores

# Las expresiones generadoras funcionan de forma muy similar a la comprensión de listas. De hecho su sintaxis es exactamente igual, a excepción de que se utilizan paréntesis en lugar de corchetes:

# In[18]:


l2 = (n ** 2 for n in l)
print(l2)
print(list(l2))


# Sin embargo las expresiones generadoras se diferencian de la comprensión de listas en que no se devuelve una lista, sino un generador.

# In[21]:


def mi_generador(n, m, s):
  while(n <= m):
    yield n
    n += s

x = mi_generador(0, 5, 1)
print(x)
print(list(x))


# El generador se puede utilizar en cualquier lugar donde se necesite un objeto iterable. Por ejemplo en un for-in:

# In[22]:


for n in mi_generador(0, 5, 1):
  print(n)


# ## Decoradores

# Un decorador no es es mas que una función que recibe una función como parámetro y devuelve otra función como resultado. Por ejemplo podríamos querer añadir la funcionalidad de que se imprimiera el nombre de la función llamada por motivos de depuración:

# In[24]:


def mi_decorador(funcion):
  def nueva(*args):
    print ("Llamada a la funcion", funcion.__name__)
    retorno = funcion(*args)
    return retorno
  return nueva


# Supongamos como ejemplo una función imp que no hace otra cosa que mostrar en pantalla la cadena pasada como parámetro.

# In[30]:


print("hola")
mi_decorador(print)("hola")


# In[ ]:




