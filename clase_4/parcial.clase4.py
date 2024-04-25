'''
Desarrollar una función que reciba como parametros el precio de un producto y el porcentaje de descuento que se aplicara. La funcion retornara el precio del producto con descuento

Alumno: Aguirre Jonathan Adrian
'''

def calcular_precio(precio, descuento):
    descuento_decimal = descuento / 100
    valor_descuento = precio * descuento_decimal
    precio_final = precio - valor_descuento
    return precio_final

precio_con_descuento = calcular_precio(100, 20)
print("Precio final con descuento:", precio_con_descuento)