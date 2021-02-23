#!/usr/bin/env python
# coding: utf-8

# # Tipos básicos

# In[3]:


# y esto es un entero
e = 23
# podemos comprobarlo con la función type
type(e)


# In[4]:


# 027 octal = 23 en base 10
entero = 0o27


# In[5]:


type(entero)


# In[6]:


# 0×17 hexadecimal = 23 en base 10
entero = 0x17


# In[7]:


type(entero)


# In[8]:


# numeros reales
real = 0.2703


# In[9]:


type(real)


# In[10]:


# numeros reales
real = 0.1e-3


# In[11]:


type(real)


# In[12]:


# numeros complejos
complejo = 2.1 + 7.8j


# In[13]:


type(complejo)


# # Operadores aritméticos

# In[15]:


# Suma
r = 3 + 2 # r es 5
print (r)


# In[16]:


# Resta
r = 4 - 7 # r es -3
print (r)


# In[17]:


# Negación
r = -7 # r es -7
print (r)


# In[18]:


# Multiplicación
r = 2 * 6 # r es 12
print (r)


# In[19]:


# Multiplicación
r = 2 ** 6 # r es 64
print (r)


# In[20]:


# División
r = 3.5 / 2 # r es 1.75
print (r)


# In[21]:


# División entera
r = 3.5 // 2 # r es 1.0
print (r)


# In[22]:


# Módulo. El operador de módulo no hace otra cosa que devolvernos el resto de la división entre los dos operandos.
r = 7 % 2 # r es 1
print (r)


# # Operadores a nivel de bit

# In[24]:


# Por ejemplo, si veis una operación como 3 & 2, lo que estais viendo es un and bit a bit entre los números binarios 11 y 10 (las representaciones en binario de 3 y 2).
# and
r = 3 & 2 # r es 2
print (r)


# In[25]:


# or
r = 3 | 2 # r es 3
print (r)


# In[26]:


# xor
r = 3 ^ 2 # r es 1
print (r)


# In[27]:


# not
r = ~3 # r es -4
print (r)


# In[28]:


# Desplazamiento izq
r = 3 << 1 # r es 6
print (r)


# In[29]:


# Desplazamiento der.
r = 3 >> 1 # r es 1
print (r)


# # Cadenas

# In[31]:


print("Las cadenas no son más que texto encerrado entre comillas simples ('cadena') o dobles (\"cadena\"). Dentro de las comillas se pueden añadir caracteres especiales escapándolos con \\, como \\n, el carácter de nueva línea, o \\t, el de tabulación.")


# In[32]:


print ("Una cadena puede estar precedida por el carácter u o el carácter r, los cuales indican, respectivamente, que se trata de una cadena que utiliza codificación Unicode y una cadena raw (del inglés, cruda). \n\nLas cadenas raw se distinguen de las normales en que los caracteres escapados mediante la barra invertida (\) no se sustituyen por sus contrapartidas. Esto es especialmente útil, por ejemplo, para las expresiones regulares, como veremos en el capítulo correspondiente.")


# In[33]:


unicode = u"äóè"
raw = r"\n"
print (unicode)
print (raw)


# In[34]:


# Podremos escribir el texto en varias líneas, y al imprimir la cadena
triple = """primera linea
esto se vera en otra linea"""
print (triple)


# In[35]:


print ("Las cadenas también admiten operadores como +, que funciona realizando una concatenación de las cadenas utilizadas como operandos y *, en la que se repite la cadena tantas veces como lo indique el número utilizado como segundo operando.")


# In[36]:


a = "uno"
b = "dos"
c = a + b # c es "unodos"
print (c)
c = a * 3 # c es "unounouno"
print (c)


# # Booleanos

# In[38]:


# and ¿se cumple a y b? 
r = True and False # r es False
print (r)


# In[39]:


# or ¿se cumple a o b?
r = True or False # r es True
print (r)


# In[40]:


# not No a
r = not True # r es False
print (r)


# In[41]:


print ("Los valores booleanos son además el resultado de expresiones que utilizan operadores relacionales (comparaciones entre valores):")


# In[42]:


# == ¿son iguales a y b?
r = 5 == 3 # r es False
print (r)


# In[43]:


# != ¿son distintos a y b?
r = 5 != 3 # r es True
print (r)


# In[44]:


# < ¿son distintos a y b?
r = 5 < 3 # r es False
print (r)


# In[45]:


# > ¿es a mayor que b?
r = 5 > 3 # r es True
print (r)


# In[46]:


# <= ¿es a menor o igual que b?
r = 5 <= 5 # r es True
print (r)


# In[47]:


# >= ¿es a mayor o igual que b?
r = 5 >= 3 # r es True
print (r)

