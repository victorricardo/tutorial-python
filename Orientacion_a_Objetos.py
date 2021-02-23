#!/usr/bin/env python
# coding: utf-8

# # Orientación a Objetos
# 
# # Hay tres conceptos que son básicos para cualquier lenguaje de programación orientado a objetos: el encapsulamiento, la herencia y el polimorfismo.

# In[21]:


# En Python las clases se definen mediante la palabra clave class seguida
# del nombre de la clase, dos puntos (:) y a continuación, indentado, el cuerpo de la clase. Como en el caso de las
# funciones, si la primera línea del cuerpo se trata de una cadena de texto, esta será la cadena de documentación de 
# la clase o docstring.

class Coche:
  """Abstraccion de los objetos coche."""
  def __init__(self, gasolina):
    self.gasolina = gasolina
    print ("Tenemos " + str(gasolina) + " litros")
  def arrancar(self):
    if self.gasolina > 0:
      print ("Arranca")
    else:
      print ("No arranca")
  def conducir(self):
    if self.gasolina > 0:
      self.gasolina -= 1
      print ("Quedan " + str(self.gasolina) + " litros")
    else:
      print ("No se mueve")
    
mi_coche = Coche(3)
mi_coche.arrancar()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()


# ## Herencia

# In[4]:


# En un lenguaje orientado a objetos cuando hacemos que una clase (subclase) herede de otra clase (superclase) 
# estamos haciendo que la subclase contenga todos los atributos y métodos que tenía la superclase.
# No obstante al acto de heredar de una clase también se le llama a menudo “extender una clase”.

# Tomado de https://www.codigofuente.org/herencia-en-python/
# Un polígono es una figura cerrada con 3 o más lados. Digamos que tenemos una clase llamada Polígono definida 
# de la siguiente manera.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
# Esta clase tiene atributos de datos para almacenar el número de lados, y la magnitud n de cada lado como una lista, 
# lados.

# El método inputSides() toma la magnitud de cada lado y, de manera similar, dispSides() los mostrará correctamente.

# Un triángulo es un polígono con 3 lados. Entonces, podemos crear una clase llamada Triángulo que se hereda de Polígono. 
# Esto hace que todos los atributos disponibles en la clase Polígono estén disponibles en Triángulo. No necesitamos 
# definirlos de nuevo(reutilización del código). Triángulo se define de la siguiente manera.

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s =(a + b + c) / 2
        area =(s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('El area del triangulo es %0.2f' %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()


# # Herencia Múltiple

# Al igual que C ++, una clase puede derivarse de más de una clase base en Python. Esto se llama herencia múltiple.
# 
# En la herencia múltiple, las características de todas las clases base se heredan en la clase derivada. La sintaxis para la herencia múltiple es similar a la herencia simple.
# 
# En el siguiente ejemplo, como Terrestre se encuentra más a la izquierda, sería la definición de desplazar de esta clase la que prevalecería, y por lo tanto si llamamos al método desplazar de un objeto de tipo Cocodrilo lo que se imprimiría sería “El animal anda”.

# In[7]:


class Terrestre:
  def desplazar(self):
    print ('El animal anda')

class Acuatico:
  def desplazar(self):
    print ('El animal nada')

class Cocodrilo(Terrestre, Acuatico):
  pass

c = Cocodrilo()
c.desplazar()


# # Encapsulación

# La encapsulación se refiere a impedir el acceso a determinados métodos y atributos de los objetos estableciendo así qué puede utilizarse desde fuera de la clase.
# 
# Esto se consigue en otros lenguajes de programación como Java utilizando modificadores de acceso que definen si cualquiera puede acceder a esa función o variable (public) o si está restringido el acceso a la propia clase (private).

# In[10]:


class MiClase:
    
    def __init__(self):
        self._atributo_privado = 1
    
    def _metodo_privado(self):
        print("Hola mundo!")


mi_objeto = MiClase()
print(mi_objeto._atributo_privado)
mi_objeto._metodo_privado()


# In[11]:


# Métodos especiales


# En Python, los métodos especiales son un conjunto de métodos predefinidos que puede usar para enriquecer sus clases. Son fáciles de reconocer porque comienzan y terminan con guiones bajos dobles, por ejemplo __init__o __str__. Estos métodos también son con conocidos como “dunders”, una abreviación de double underline.
# 
# ## Inicialización: método __init__
# 
# Necesito inicializar mi clase con el método __init__ para establecer los valores de la instancia.
# 
# ## Representación del objeto: __str__,__repr__
# 
# Es una práctica recomendada crear una representación de los objetos en texto. Hay 2 formas de hacer esto con métodos especiales:
# 
# - __str__: Es una representación orientada al usuario final, es la manera “informal” de representarlo
# - __repr__: Es una representación “formal” de cómo se genera el objeto.
# 
# ## Funcionalidad de iteración: __len__, __getitem__, __reversed__
# 
# Para añadir una funcionalidad de iteraciones necesito añadir primero algunos productos al objeto, crearé un método en la clase para hacerlo. Será una función simple que verifique si aún hay espacios en el almacén para poder añadirlo.
# 
# ## Sobrecarga de operadores: __add__
# 
# ¿Alguna vez quisiste usar el operador + con algunas de tus clases? Bueno, en Python todo es un objeto, por lo que entra en juego el famoso poliformismo.
# 
# Cuando usamos el operador + se comporta muy distinto si lo usamos con un número, un string o una lista. En este momento nuestra clase Almacen no soporta el uso de este operador…
# 
# ## Operadores de comparación: __eq__
# 
# También podemos usar los operadores como >, >=, <=, < o ==. Con la ayuda del método __eq__ podemos hacer comparaciones lógicas con ==. 

# In[ ]:




