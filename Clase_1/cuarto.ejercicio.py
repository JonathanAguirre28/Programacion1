#def restar_numeros_4(un_numero, otro_numero, tercer_numero = 0):
 #   resta = un_numero - otro_numero - tercer_numero
 #   mensaje = f"{resta}"
 #   return resta

#resultado = restar_numeros_4(10, 5)

#print(resultado)

#resultado = restar_numeros_4(10, 5, 7)

#print(resultado)

def presentar_profesor(nombre, edad, mail = None):
    if mail is None:
        print(f"Hola me llamo {nombre} y tengo {edad} años.")
    else:
        print(f"Hola me llamo {nombre} y tengo {edad} años. Mi correo es {mail}")
        
presentar_profesor("Matias", 27, "mati@gmail.com")

presentar_profesor("German", 36)
