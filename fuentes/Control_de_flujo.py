#!/usr/bin/env python
# coding: utf-8

# # Control de flujo - Sentencias condicionales

# In[61]:


# if es La forma más simple de un estamento condicional es un if (del inglés si) seguido de la condición a evaluar, 
# dos puntos (:) y en la siguiente línea e indentado, el código a ejecutar en caso de que se cumpla dicha condición.
fav = "mundogeek.net"
# si (if) fav es igual a “mundogeek.net”
if fav == "mundogeek.net":
    print ("Tienes buen gusto!")
    print ("Gracias") 


# In[62]:


fav = "lastima.net"
if fav == "mundogeek.net":
    print ("Tienes buen gusto!")
    print ("Gracias") 
else:
    print ("Vaya, que lástima")


# In[63]:


numero = 0
if numero < 0:
    print ("Negativo")
elif numero > 0:
    print ("Positivo")
else:
    print ("Cero")


# In[64]:


# También existe una construcción similar al operador ? de otros lenguajes, que no es más que una forma compacta de 
# expresar un if else. En esta construcción se evalúa el predicado C y se devuelve A si se cumple o B si no se cumple: 
# A if C else B. Veamos un ejemplo:
num = 5
var = "par" if (num % 2 == 0) else "impar"
print (var)


# # Control de flujo - Bucles

# In[66]:


# while El bucle while (mientras) ejecuta un fragmento de código mientras se cumpla una condición.
edad = 0
while edad < 3:
    edad = edad + 1
    print ("Felicidades, tienes " + str(edad))


# In[67]:


# Sin embargo hay situaciones en las que un bucle infinito es útil. Por ejemplo, veamos un pequeño programa que repite 
# todo lo que el usuario diga hasta que escriba adios.
while True:
    entrada = input("> ")
    if entrada == "adios":
        break
    else:
        print ("entrada")


# In[68]:


# Otra palabra clave que nos podemos encontrar dentro de los bucles es continue (continuar). Como habréis adivinado no hace 
# otra cosa que pasar directamente a la siguiente iteración del bucle.
edad = 0
while edad < 5:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print ("Felicidades, tienes" + str(edad))


# In[7]:


# for … in A los que hayáis tenido experiencia previa con según que lenguajes este bucle os va a sorprender gratamente. 
# En Python for se utiliza como una forma genérica de iterar sobre una secuencia. Y como tal intenta facilitar su uso 
# para este fin.
secuencia = ["uno", "dos", "tres"]
i = 0
for elemento in secuencia:
    i = i + 1
    print ("elemento: " + str(i) + " secuencia: " + str(elemento))

