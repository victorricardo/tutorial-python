#!/usr/bin/env python
# coding: utf-8

# # Funciones 

# In[6]:


# Una función es un fragmento de código con un nombre asociado que realiza una serie de tareas y devuelve un valor. 
# A los fragmentos de código que tienen un nombre asociado y no devuelven valores se les suele llamar procedimientos.
def mi_funcion(param1, param2):
    """Esta funcion imprime los dos valores pasados    
       como parametros"""    
    print (param1)    
    print (param2)
    
mi_funcion("hola", 2)


# In[7]:


# Sin embargo también es posible modificar el orden de los parámetros si indicamos el nombre del parámetro al que asociar 
# el valor a la hora de llamar a la función:
mi_funcion(param2 = 2, param1 = "hola")


# In[9]:


# Para definir funciones con un número variable de argumentos colocamos un último parámetro para la función cuyo nombre 
# debe precederse de un signo *:
def varios(param1, param2, *otros):    
    for val in otros:        
        print (val)
        
varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)


# In[10]:


# En el siguiente ejemplo se utiliza la función items de los diccionarios, que devuelve una lista con sus elementos, 
# para imprimir los parámetros que contiene el diccionario.
def varios(param1, param2, **otros):    
    for i in otros.items():        
        print (i)
        
varios(1, 2, tercero = 3)


# In[1]:


# Veamos un pequeño programa para demostrarlo. En este ejemplo se hace uso del método append de las listas. Un método no 
# es más que una función que pertenece a un objeto, en este caso a una lista; y append, en concreto, sirve para añadir 
# un elemento a una lista
def f(x, y):    
    x = x + 3    
    y.append(23)    
    print (x, y)
    
x = 22
y = [22]
f(x, y)
print (x, y)


# In[3]:


def sumar(x, y):    
    return x + y

print (sumar(3, 2))


# In[5]:


# En Python las clases se definen mediante la palabra clave class segui-da del nombre de la clase, dos puntos (:) y a 
# continuación, indentado, el cuerpo de la clase. Como en el caso de las funciones, si la primera línea del cuerpo se 
# trata de una cadena de texto, esta será la cadena de documentación de la clase o docstring.
class Coche:    
    """Abstraccion de los objetos coche."""    
    def __init__(self, gasolina):        
        self.gasolina = gasolina        
        print ("Tenemos", gasolina, "litros")    
    def arrancar(self):        
        if self.gasolina > 0:            
            print ("Arranca")        
        else:            
            print ("No arranca")   
    def conducir(self):        
        if self.gasolina > 0:           
            self.gasolina -= 1            
            print ("Quedan", self.gasolina, "litros")        
        else:            
            print ("No se mueve")


# In[8]:


mi_coche = Coche(3)
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()


# In[13]:


# Python 3 code to demonstrate the  
# working of MD5 (string - hexadecimal) 
  
import hashlib 
  
# initializing string 
str2hash = "fb7f567e32ce7d..."
  
# encoding GeeksforGeeks using encode() 
# then sending to md5() 
result = hashlib.md5(str2hash.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 

