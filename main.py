# Imprimir en pantalla
print("Hola mundo")

# Variables y operaciones básicas
x = 10
print(x)

a = 10
b = 20
c = a + b
print(c)

# Uso de condicionales
a = 20
if a == 20:
    print("a es igual a 20")
elif a == 10:
    print("a es igual a 10")
else:
    print("a no es igual a 20")

# Trabajando con decimales y cadenas
valor_decimal = 3.1416
cadena = "Hola"

# Comentarios
# Este es un comentario de una sola línea

"""
Este es un comentario
de varias líneas
"""

# Identación en Python

# Función
def funcion(a, b):
    return a + b

d = funcion(1, 2)
print(d)

# Nombres de variables
_variable = 10
variable = 20
variable_3 = 30
vabiaBle = 40

# Bucle for
for i in range(10):
    print(i)

# Bucle while
x = 10
while x > 0:
    print(x)
    x -= 1

# Listas
mi_lista = ["manzana", "banana", "cereza"]
print(mi_lista)
print(mi_lista[1])  # Acceso
mi_lista[1] = "arándano"  # Modificación
mi_lista.append("durazno")  # Agregar
mi_lista.remove("durazno")  # Eliminar
print(mi_lista)

# Diccionarios
mi_diccionario = {"marca": "Ford", "modelo": "Mustang", "año": 1964}
print(mi_diccionario)
print(mi_diccionario["modelo"])  # Acceso
mi_diccionario["año"] = 2020  # Modificación
mi_diccionario["color"] = "rojo"  # Agregar
del mi_diccionario["color"]  # Eliminar
print(mi_diccionario)

# Tuplas
mi_tupla = ("manzana", "banana", "cereza")
print(mi_tupla)
print(mi_tupla[1])  # Acceso

# Conjuntos
# Colecciones no ordenadas y sin elementos duplicados.
mi_conjunto = {"manzana", "banana", "cereza"}
print(mi_conjunto)
mi_conjunto.add("naranja")  # Agregar
mi_conjunto.remove("banana")  # Eliminar
print(mi_conjunto)

# Operaciones con conjuntos
otro_conjunto = {"cereza", "sandía", "kiwi"}
interseccion = mi_conjunto.intersection(otro_conjunto)
print(interseccion)

# Funciones con argumentos variables
def funcion_varios_args(*args):
    print(args)  # args es una tupla

funcion_varios_args(1, 'a', True)

# Funciones con argumentos de palabra clave (keyword arguments)
def funcion_kwargs(**kwargs):
    print(kwargs)  # kwargs es un diccionario

funcion_kwargs(clave1="valor1", clave2="valor2")

# Clases y objetos
class MiClase:
    x = 5

objeto = MiClase()
print(objeto.x)

# Métodos en clases
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        print("Hola, mi nombre es " + self.nombre)

p1 = Persona("Juan", 36)
p1.saludo()

# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, año):
        super().__init__(nombre, edad)
        self.año = año

    def bienvenida(self):
        print(f"Bienvenido {self.nombre} al año {self.año}.")

e1 = Estudiante("Ana", 21, 2023)
e1.bienvenida()

# Manejo de excepciones
try:
    print(x / 0)
except ZeroDivisionError:
    print("División por cero.")
finally:
    print("Este bloque se ejecuta siempre.")

# Módulos
# Para usar un módulo, deberías tener un archivo .py adicional; por ejemplo, mi_modulo.py
# Supongamos que mi_modulo.py contiene una función llamada mi_funcion.
# Importarías y usarías así:
# import mi_modulo
# mi_modulo.mi_funcion()

# Archivos
# Abrir un archivo y leer su contenido
# with open('mi_archivo.txt', 'r') as archivo:
#     contenido = archivo.read()
#     print(contenido)

# Escribir en un archivo
# with open('mi_archivo.txt', 'w') as archivo:
#     archivo.write("Hola Mundo")

