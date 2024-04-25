'''
Funciones_2
Ejercicio N° 3.
Alumno: Jonathan Adrian Aguirre

3.
Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender).
'''

def get_string(cadena: str, longitud: int) -> str|None:
    if len(cadena) == longitud:
        mensaje = "Exelente coincide"
    else:
        mensaje = "Error la cadena no conincide con la longitud"
        
    return mensaje
        
    
mensaje = get_string("programacion", 12)
print(mensaje)