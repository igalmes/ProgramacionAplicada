# Instituto de formación técnica superior N° 18
# Programación Aplicada - Ejercicios de programación
# Profesor Bonini Juan Ignacio
# Ejercicios utilizando clases





#
# 4.2. Animal: Utilizar la clase Animal del ejercicio de herencia y aplicar
# polimorfismo para realizar el sonido característico del animal. Luego,
# crear una lista de animales de diferentes tipos y utilizar el polimorfismo
# para hacer que emiten sus sonidos.
# 4.3. Empleado: Utilizar la clase Empleado del ejercicio de herencia y aplicar
# polimorfismo para calcular el salario de acuerdo con las reglas
# específicas de cada tipo de empleado. Luego, crear una lista de
# empleados de diferentes tipos y utilizar el polimorfismo para calcular
# sus salarios.





# 1. Abstracción
# 1.1. FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo
# y Triangulo y que contenga métodos y atributos relacionados con el
# cálculo del área y perímetro de una figura geométrica. Definan los
# métodos y atributos necesarios para calcular el área y el perímetro de
# cada tipo de figura utilizando los conceptos de abstracción.


from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio =radio

    def area(self):
        return f'Area del Círculo: {3.14 * self.radio **2}'
    
    def perimetro(self):
        return f'Perímetro del Círculo: {2 * 3.14 * self.radio}'

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f'Area del Rectángulo: {self.base * self.altura}'
    
    def perimetro(self):
        return f'Perímetro del Rectángulo: {2 * (self.base + self.altura)}'

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, a, b, c):
        self.base = base
        self.altura = altura
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        return f'Area del Triángulo: {(self.base * self.altura) / 2}'

    def perimetro(self):
        return f'Perímetro del Triángulo: {self.a + self.b + self.c}'


circulo = Circulo(100)
print(circulo.area())
print(circulo.perimetro())

rectangulo = Rectangulo(100, 200)
print(rectangulo.area())
print(rectangulo.perimetro())

triangulo = Triangulo(100, 200, 20, 20, 20)
print(triangulo.area())
print(triangulo.perimetro())


# 1.2. Libro: Crear las clases Libro y Libreria. La clase Libro debe incluir
# atributos como titulo, autor y precio. La clase Libreria debe contener una
# lista de objetos Libro y métodos para calcular el precio total de todos
# los libros en la librería.



"""
from abc import ABC, abstractmethod

class Libro(ABC):
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @abstractmethod
    def precio_final (self):
        pass

class Libreria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def precio_final(self):
        suma = sum(libro.precio for libro in self.libros)
        return suma


"""

# 1.3. Vehiculo: Implementar las clases Vehiculo, Coche, Motocicleta y
# Bicicleta. La clase Vehiculo debe tener propiedades como marca,
# modelo y velocidad_maxima. Cada subclase debe definir sus métodos y
# atributos específicos relacionados con el comportamiento de cada tipo
# de vehículo.
"""

from abc import ABC, abstractmethod

class Vehiculo(ABC):
   def __init__(self, marca, modelo, velocidad_maxima):
       self.marca = marca
       self.modelo = modelo
       self.velocidad_maxima = velocidad_maxima


@abstractmethod
def arrancar(self):
    pass
   
class Coche(Vehiculo):
    
    def arrancar(self):
        print('arranca el auto')


class Motocicleta(Vehiculo):
    def arrancar(self):
        print('arranca la moto')
    
class Bicicleta(Vehiculo):
    def arrancar(self):
       print('arranca la bici')


ejemplo = Bicicleta('100','200',100)
ejemplo.arrancar()

ejemplo2 = Motocicleta('100','200',100)
ejemplo2.arrancar()

ejemplo3 = Coche ('200','2',1)
ejemplo3.arrancar()
"""


#2. Herencia
# 2.1. Animal: Utilizar las clases Animal, Perro, Gato y Pájaro. Se debe incluir
# atributos como nombre y edad. Las subclases deben heredar y definir
# métodos y atributos relacionados con el comportamiento y
# características de cada tipo de animal.

"""

class Animal:
    def __init__(self,edad, nombre):
        self.edad = edad
        self.nombre = nombre
    
    def hacer_ruido(self):
        pass

class Perro(Animal):
    def __init__(self, edad, nombre, raza):
        super().__init__(edad, nombre)
        self.raza = raza

    def hacer_ruido(self):
        return 'Guau'


class Gato(Animal):
    def __init__(self, edad, nombre, color):
        super().__init__(edad, nombre)
        self.color = color
    
    def hacer_ruido(self):
        return 'miau'

class Pajaro(Animal):
    def __init__(self, edad, nombre,especie ):
        super().__init__(edad, nombre)
        self.especie = especie

    def hacer_ruido(self):
        return 'pio pio'
    

perrito = Perro(1,'norberto','doberman')
print(f'El perro {perrito.nombre}, tiene {perrito.edad} año y es un {perrito.raza}')
print (perrito.hacer_ruido())

gatito = Gato(2,'chipitas','negro')
print(f'El gato {gatito.nombre}, tiene {gatito.edad} años y tiene un color {gatito.color}')
print (gatito.hacer_ruido())

pajarito = Pajaro(3,'Oscar','Paloma')
print(f'El pajaro {pajarito.nombre}, tiene {pajarito.edad} años y tiene es una {pajarito.especie}')
print (pajarito.hacer_ruido())

"""


# 2.2. Empleado: Crear las clases Empleado, Gerente y Trabajador. Se debe
# tener atributos como nombre, salario y departamento. Las subclases
# deben heredar y definir los métodos y atributos necesarios para
# representar cada tipo de empleado.


"""

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def saludo (self):
        pass

class Gerente(Empleado):
   
    def __init__(self, nombre, salario, departamento, cargo):
        super().__init__(nombre, salario, departamento)
        self.cargo = cargo
    
    def saludo (self):
        return f'Hola empleados, soy su nuevo gerente {self.nombre}\nOcupo el departamento de {self.departamento}\ny mi cargo es el de... {self.cargo}'
    

class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, saludo):
        super().__init__(nombre, salario, departamento)
    
    def saludo(self):
        return f'Hola, jefe. Soy {self.nombre}\nocupo el puesto de {self.departamento}\naumentame el salario que cobro {self.salario} mangos'

boss = Gerente('Lucas', 100000, 'Ventas','nose')
print(boss.saludo())

admin = Trabajador('Alberto', 10, 'Compras','holaa')
print(admin.saludo())

"""
# 2.3. Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las
# clases deben contener atributos como color y dimensiones. Las
# subclases deben heredar y definir métodos y atributos para calcular el
# área y el perímetro de cada forma.

"""
class Forma:
    def __init__(self, color, dimensiones):
        self.color = color
        self.dimensiones = dimensiones
    

class Circulo(Forma):
    def __init__(self, color, radio):
        super().__init__(color, dimensiones=[radio])
        self.radio = radio
    
    def calcular_area(self):
        return 3.14*(self.radio**2)
    
    def calcular_perimetro(self):
        return 2*3.14*self.radio

class Rectangulo(Forma):
    def __init__(self, color, base, altura):
        super().__init__(color, dimensiones=[base, altura])
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base*self.altura
    
    def calcular_perimetro(self):
        return 2 *(self.altura+self.base)
    
circulo = Circulo("rojo", 200)
print(f'area: {circulo.calcular_area()}\n perimetro: {circulo.calcular_perimetro()}')

rectangulo = Rectangulo('blanco', 100, 200)
print(f'Rectangulo: \narea: {rectangulo.calcular_area()}\nperimetro: {rectangulo.calcular_perimetro()}')

"""


#3. Encapsulamiento
# 3.1. CuentaBancaria: Crear la clase CuentaBancaria con atributos privados y
# públicos para el saldo y titular. Definir métodos para depositar, retirar y
# consultar el saldo de la cuenta.

"""
class CuentaBancaria:
    def __init__(self,saldo, titular):
        self._saldo = saldo
        self.titular = titular

    
    def depositar(self, deposito):
        self._saldo += deposito
        return self._saldo
    
    def retirar(self, extraccion):
        self._saldo -= extraccion
        return self._saldo
    
    def consultar(self):
        return self._saldo

cliente=CuentaBancaria(1, 'GALMES')
print(f'saldo: ',cliente.consultar())
print(f'retira: $1 ',cliente.retirar(1))
print(f'deposito; $2 = ',cliente.depositar(2))

"""

# 3.2. Estudiante: Implementar la clase Estudiante con atributos como nombre,
# edad y calificaciones. Utilizar el encapsulamiento para proteger los
# datos que deban ser protegidos y proporcionar métodos públicos para
# obtener dichos datos.
"""
class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = [nombre]
        self._edad = edad
        self._calificaciones = [calificaciones]
    
    def consultar_edad(self, nombre):
        self._edad = 25
        return f'nombre: {nombre}, edad es {self._edad}'
    
    def consultar_calificaciones(self):
        return self._calificaciones
    
yo = Estudiante('igalmes', 20, [5, 4])
print(yo.consultar_calificaciones())
"""


# 3.3. Coche: Crear la clase Coche con atributos privados y/o públicos según
# corresponda de velocidad y kilometraje. Definir métodos públicos para
# acelerar y registrar el kilometraje de manera segura.
"""
class Coche:
    def __init__(self, velocidad, kms):
        self.velocidad = velocidad
        self._kms=kms
        print(f'velocidad: ',self.velocidad,'km')
       


    def acelerar (self, recorrido):
            recorrido = self._kms+self.velocidad
            return recorrido
    
    def registro(self, ):
            self._kms += self.velocidad
            print(f'listado de historicos: {self._kms}')

coche = Coche(100,200)
print(f'acelera: ',coche.acelerar(''))
print(f'registro histotico: ',coche.acelerar(recorrido=20))
    
"""
# 4. Polimorfismo
# 4.1. FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de
# abstracción y crear un método muestre información específica de la
# figura utilizando polimorfismo. Luego, crear una lista de figuras
# geométricas de diferentes tipos y utilizar el polimorfismo para imprimir
# su información.




# 5. Sistema de Gestión de Personal
# Diseña un sistema de gestión de personal para una empresa. Debes
# implementar las siguientes clases:

# Persona: Una clase base que representa a una persona con atributos como
# nombre, edad y DNI. Utiliza el encapsulamiento para proteger los datos sensibles.

# Empleado: Una subclase de Persona que agrega atributos como salario y
# cargo. Implementa el cálculo del salario en base al cargo y permite consultar el
# salario.
# Gerente: Una subclase de Empleado que agrega atributos específicos de un
# gerente, como departamento.
# Departamento: Una clase que contiene una lista de empleados y métodos
# para agregar, eliminar y consultar empleados.
#  Crea instancias de estas clases y demuestra cómo agregar empleados a un
# departamento, calcular salarios y acceder a la información de las personas
# Importante
# Se deberá escribir un detalle del ejercicio explicando de qué manera lo
# resolvieron, como aplicaron los distintos conceptos de la POO.
"""

5.1 falta instanciar bien la metodo "consulta" con bucle for.

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self._edad = edad
        self._dni = dni
    
    def informacio_personal(self):
        return f'Nombre: {self.nombre}\nedad: {self._edad}\nDni: {self._dni}'
    
class Empleado(Persona):
    def __init__(self, nombre, edad, dni, salario, cargo):
        super().__init__(nombre, edad, dni)
        self.salario = salario
        self.cargo = cargo
    
    def calcular_salario(self):
        return f'salario: {self.salario}'
       
class Gerente(Empleado):
    def __init__(self, nombre, edad, dni, salario, cargo, departamento):
        super().__init__(nombre, edad, dni, salario, cargo)
        self.departamento = departamento
    
    def asignar_departamento(self):
        return f'departamento: {self.departamento}'

class Departamento:
    def __init__(self):
        self.listaEmpleados = []
            
    def agregar(self,ingresante):
        self.listaEmpleados.append(ingresante)
        
    def borrar(self, ingresante):
        self.listaEmpleados.remove(ingresante)
    
    def consulta(self):
        return self.listaEmpleados
    

messi = Persona('Lio Messi', 36, 10101010)
print(messi.informacio_personal())

aimar = Empleado('Pablo Aimar', 40, 10000000,10000,'ayudante')
print(aimar.calcular_salario())

scaloni = Gerente('Lionel Scaloni', '41', '2222222', 100000,'DT', 'unknow')
print(scaloni.informacio_personal())


afa = Departamento()
afa.agregar(aimar)
afa.agregar(scaloni)
print(afa.consulta())

1- cree las clases 
2- encapsule los atributos sensibles como dni y edad
3- herencia en empleado
4-crear metodos para agregar en listas -empaquetado y desempaquetado de listas me cuesta mucho darle la vuelta-
5- instanciar todo 

"""

# 6. Sistema de Comercio Electrónico
# Diseña un sistema de comercio electrónico para una tienda en línea. Debes
# implementar las siguientes clases:
# Producto: Una clase que representa un producto con atributos como nombre,
# precio, cantidad en stock, etc.
# CarritoCompra: Una clase que representa el carrito de compras de un cliente.
# Debe permitir agregar, eliminar y calcular el total de los productos en el carrito.

# Cliente: Una clase que representa a un cliente con atributos como nombre,
# dirección, carrito de compra, etc.
# Crea instancias de estas clases y demuestra cómo un cliente puede agregar
# productos a su carrito, realizar una compra y calcular el total.
# Importante
# Se deberá escribir un detalle del ejercicio explicando de qué manera lo
# resolvieron, cómo aplicaron los distintos conceptos de la POO.

"""
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self._precio= precio
        self._stock = stock
    
    def ver_precio(self):
        return self._precio
    
    def ver_stock(self):
        return self._stock


class CarritoCompras:
    def __init__(self, producto):
        
        self.producto = []
    
    def agregar(self, producto):
        return self.producto.append(producto)    
    
    def remover(self, producto):
        for producto in self.producto:
            self.producto.remove(producto) 
    
    def calcular_total(self):
        sum(Producto.ver_precio())

class Cliente:
    def __init__(self, nombre_cliente, direccion, carrito_compras):
        self.nombre_cliente = nombre_cliente
        self._direccion = direccion
        self._carrito_compras = carrito_compras

    def agregar_producto(self, agregar):
        self._carrito_compras = []
        return self._carrito_compras.append(agregar)


    def ver_carrito(self):
        return f'productos seleccionados: {self._carrito_compras}'

producto1 = Producto('Coca Cola', 1000, 500)
producto2 = Producto('Doritos', 800, 200)
print(f'Producto: {producto1.nombre}\nPrecio: ${producto1.ver_precio()} \nStock: {producto1.ver_stock()} unidades')
print()
print(f'Producto: {producto2.nombre}\nPrecio: ${producto2.ver_precio()} \nStock: {producto2.ver_stock()} unidades')
print()
cliente1 = Cliente('Juan', 'MarceloT 200','sprite, chizitos')
print(f'Cliente Nombre: {cliente1.nombre_cliente}\nProductos En Carrito:{cliente1.ver_carrito()}')


Nota: 

Cree las clases (producto, carrito y cliente)
la clase producto y clientes tienen atributos privados para proteger datos sensibles. 
puse metodos como ver carrito, sumar prodcutos y remover dentro de la clase carrito, en la clase producto cree los metodos para
ver precio y stock
en la clase cliente cree el metodo agregar producto a carrito y ver los productos dentro de esa lista.
-- no puede sumar el precio de los productos dentro del carrito--

"""

# 7. Sistema de Geometría 3D
# Diseña un sistema de geometría tridimensional que trabaje con figuras en el
# espacio 3D. Debes implementar las siguientes clases:
# Punto3D: Una clase que representa un punto en el espacio 3D con
# coordenadas x, y, y z.
# Figura3D: Una clase abstracta que representa una figura tridimensional y
# define métodos abstractos para calcular su volumen y área superficial.
# Cubo, Esfera y Cilindro: Subclases de Figura3D que implementan los métodos
# para calcular el volumen y área superficial específicos de cada figura.

# Crea instancias de estas clases y demuestra cómo calcular el volumen y área
# superficial de diferentes figuras tridimensionales.

# Importante:
# Se deberá escribir un detalle del ejercicio explicando de qué manera lo
# resolvieron, cómo aplicaron los distintos conceptos de la POO.

"""

from abc import ABC, abstractmethod
import math

class Punto3D(ABC):
    def __init__(self, x, y, yz):
        self.x = x
        self.y = y
        self.yz = yz

class Figura3D:
    def __init__(self):
        pass

    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass

class Cubo(Figura3D):
    
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_vol(self):
        return self.lado**3

    def calcular_area(self):
        pass #no entiendo qué tengo que calcular :@

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_vol(self):
        return math.pi * self.radio**2

    def calcular_area(self):
        pass #no entiendo qué tengo que calcular :@

class Cilindro(Figura3D):
    def __init__(self, radio, altura):
        self.radio = radio

        self. altura=altura
    
    def calcular_vol(self):
        return math.pi * self.radio **2 *self.altura

punto = Punto3D(1,2,3)
cubo = Cubo(2)
esfera = Esfera(10)
cilindro = Cilindro(10, 12)

print(f'Volumen del cubo:',cubo.calcular_vol())
print(f'Volumen de la esfera:',esfera.calcular_vol())
print(f'Volumen del cilindro:',cilindro.calcular_vol())


#falta instanciar métodos.

"""

# Ejercicios python avanzado
# 1. Decoradores
# 1.1. Hacer un decorador para registrar las llamadas a una función, junto con
# sus argumentos y resultados.
"""
def registro(funcion):
    def decorador(*args, **kwargs):
        resultado = funcion(*args,**kwargs)
        print(f'funcion: {funcion.__name__} args: {args}\n kwargs: {resultado}')
        return resultado

    return decorador

@registro
def suma(a,b):
    print (a+b)

resultado = suma(2,2)

"""

# 1.2. Hacer un decorador para verificar que los argumentos de una función
# sean del tipo correcto.

# def verificacion(*argumento):
#     def decorador(funcion):
#         pass
# 1.3. Hacer un decorador para agrega un retardo antes de que se ejecute
# una función





# 1.4. Hacer un decorador para verificar las precondiciones antes de ejecutar
# una función.
# 2. Administradores de contexto
# 2.1. Hacer un administrador de contexto para notificar eventos al entrar y al
# salir de un bloque de código.
# 2.2. Crea un administrador de contexto que permita cambiar el directorio de
# trabajo al entrar en un bloque y volver al directorio original al salir.
# Ejemplo:
# 3. Imports
# 3.1. Crear dos módulos en el mismo directorio. Desde un módulo, importa
# una función o variable del otro utilizando una importación absoluta.
# 3.2. Crear dos módulos en el mismo directorio. Desde un módulo, importa
# una función o variable del otro utilizando una importación relativa.
# 3.3. Crear dos módulos en el mismo directorio. Desde un módulo, importar
# el otro sin usar from.
# 3.4. Crear dos módulos en el mismo directorio. Desde un módulo, importa
# una función o variable del otro utilizando una importación absoluta y
# generar un error de importación circular.
# 3.5. Crear dos módulos en el mismo directorio. Desde un módulo, importar
# el otro sin usar from y utilizando alias.
# 1
# 3.6. Crear dos módulos en el mismo directorio. Desde un módulo, importa
# una función o variable del otro utilizando una importación absoluta y
# utilizar un alias
# 3.7. Crear dos módulos en el mismo directorio. Desde un módulo, importa
# una función o variable del otro utilizando una importación relativa y
# utilizar un alias
# 4. Funciones Lambda
# 4.1. Dada una lista de números, utiliza map y una función lambda para crear
# una nueva lista que contenga el doble de cada número.
# 4.2. Toma una lista de cadenas y utiliza map con una función lambda para
# convertir todas las cadenas en mayúsculas.
# 4.3. Dada una lista de cadenas, utiliza map y una función lambda para crear
# una lista con la longitud de cada palabra.
# 4.4. Toma una lista de números y utiliza map con una función lambda para
# calcular la raíz cuadrada de cada número.
# 5. Algoritmos
# 5.1. Escribe una función que sume los dígitos de un número pares de un
# número entero. Si el número es impar, restarle 3 y sumarlo. Si el número
# da negativo, sumar 1.
# 6. Recursividad
# 6.1. Escribe una función recursiva para encontrar y sumar todos los números
# primos desde 1 hasta un número deseado.
# 6.2. Escribe una función recursiva para calcular el MCD de dos números
# enteros.
# 6.3. Escribe una función recursiva para invertir una cadena.
# 7. Excepciones
# 7.1. Manejo de excepciones
# 7.1.1. Escribe un programa que solicite al usuario dos números y realice
# la división de uno por el otro. Utiliza un bloque try y except para
# manejar la excepción que ocurre si el segundo número es cero.
# 7.1.2. Crea una lista de números y, a continuación, intenta acceder a un
# elemento en un índice especificado por el usuario. Utiliza un
# 2
# bloque try y except para manejar la excepción que se produce si
# el índice está fuera de rango.
# 7.1.3. Solicita al usuario que ingrese una cadena que represente un
# número. Utiliza un bloque try y except para manejar la excepción
# que se produce si la cadena no se puede convertir a un número.
# 7.1.4. Escribe un programa que intente abrir un archivo que no existe y
# utilice un bloque try y except para manejar la excepción de
# "FileNotFoundError".
# 7.1.5. Crea un diccionario y luego intenta acceder a un valor utilizando
# una clave que no está en el diccionario. Utiliza un bloque try y
# except para manejar la excepción que se produce si la clave no
# existe.
# 7.2. Excepciones personalizadas
# 7.2.1. Para cada caso anterior del manejo de excepciones (7.1.1, 7.1.2,
# 7.1.3, 7.1.4, 7.1.5) crear una excepción personalizada.
# 7.3. Bloques try-except-finally
# 7.3.1. Escribe un programa que intente abrir un archivo, leer su
# contenido y luego cerrarlo. Utiliza bloques try, except y finally
# para asegurarte de que el archivo se cierre correctamente,
# incluso si ocurre una excepción durante la lectura.
# 7.3.2. Crea un programa que solicite al usuario dos números y una
# operación matemática (suma, resta, multiplicación, división) para
# realizar. Utiliza bloques try, except y finally para manejar cualquier
# excepción que pueda ocurrir durante la operación y asegurarte
# de que los recursos se liberen correctamente.
# 7.3.3. Escribe un programa que abra un archivo, lea su contenido y
# escriba el mismo contenido en otro archivo. Utiliza bloques try,
# except y finally para manejar cualquier excepción que pueda
# ocurrir durante la lectura o escritura, y asegúrate de que ambos
# archivos se cierren correctamente.
# 7.4. Lanzamiento de excepciones
# 7.4.1. Capturar las excepciones personalizadas en el punto 7.2, imprimir
# un mensaje en pantalla y lanzarlas nuevamente.
# 3
# 8. Manejo de archivos
# 8.1. Escribe un programa que abra un archivo de entrada, lea su contenido y
# luego escriba ese contenido en un nuevo archivo de salida. Asegúrate
# de cerrar ambos archivos al final.
# 8.2. Escribe un programa que abra un archivo de texto, cuente cuántas
# palabras contiene y muestre el resultado en la pantalla.
# 8.3. Lee un archivo CSV que contiene registros de datos y realiza alguna
# operación de procesamiento en los datos, cómo calcular promedios,
# encontrar valores máximos o mínimos, o filtrar registros que cumplan
# ciertas condiciones.
# 8.4. Escribe un programa que tome varios archivos de texto y los concatena
# en un solo archivo de salida. Asegúrate de cerrar todos los archivos
# correctamente.
# 8.5. Lee un archivo CSV que contiene registros de datos y convertirlo en un
# archivo JSON.
# 9. Programación concurrente / paralelo
# 9.1. Crea dos hilos que ejecuten dos funciones diferentes simultáneamente
# y muestran mensajes de salida.
# 9.2. Implementa el problema del productor-consumidor utilizando hilos,
# donde un hilo produce datos y otro hilo los consume desde una cola
# compartida.
# 9.3. Crea dos procesos utilizando la biblioteca multiprocessing y ejecuta
# funciones diferentes en cada proceso.
# 9.4. Utiliza un pool de procesos para realizar operaciones en paralelo en
# una lista de datos.
