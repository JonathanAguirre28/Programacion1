def restar_numeros_4(un_numero: int, otro_numero: int, tercer_numero : int = 0) -> int:
    resta = un_numero - otro_numero - tercer_numero
    
    return resta

resultado = restar_numeros_4(5, 5)

print(resultado)

resultado = restar_numeros_4(10, 5, 7)
restar_numeros_4(5,7)
print(resultado)