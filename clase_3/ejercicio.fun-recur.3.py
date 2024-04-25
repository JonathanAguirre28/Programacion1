'''
Actividad clase 3
Alumno: Jonathan Adrian Aguirre

1. Realizar una función recursiva que calcule la suma de los primeros números naturales.
2. Realizar una función recursiva que calcule la potencia de un número.
3. Realizar una función recursiva que la suma de los dígitos, de un número.
4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo
****Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores.
En donde:
número: el número ingresado por el usuario mediante consola, utilizando nuestra función get_int(mensaje,mensaje_error,mínimo,máximo,reintentos)
'''

def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10  
        resto_numero = numero // 10 
        return ultimo_digito + sumar_digitos(resto_numero) 

resultado = sumar_digitos(1234)
print(resultado)