# ##################################### strip() saca los espacios de adelante y atras ######################
# cadena = "          pepito            "

# cadena = cadena.strip()

# print(cadena)

####################################### strip() caso 2 ####################################################
# cadena = "matias         pepito esta comiendo oreos            "

# #me saca matias que esta alprincipio
# cadena = cadena.strip("matias")
# #me saca los espacios del principio y del final
# cadena = cadena.strip()

# print(cadena)

######################################### upper() ##########################################################

# cadena = "MaTiaS"

# # cadena = cadena.upper() # para mayusculas
# cadena = cadena.lower() # para minusculas
# print(cadena)

##################################### capitalize() ##########################################################

# cadena = "maTiaS qUiRoz"

# print(cadena)

# cadena = cadena.capitalize()

# print(cadena)


###################################  replace () #############################################################

# cadena = "jonathan jonathan jonathan"

# print(cadena)

# cadena = cadena.replace("jonathan","adrian") # primeros le pasas el string que queres remplazar, despues por lo que lo vas a remplazar

# print(cadena)

################################## split() ##################################################################

# cadena = "jonathan*+adrian*aguirre*simon*aguirre"

# print(cadena)

# lista_de_nombres = cadena.split("*") # cada ves que encuentra un * guarda ese elemento en una lista y me devuelve una lista.

# print(lista_de_nombres)

################################# join () ##################################################################

# cadena = "jonathan*+adrian*aguirre*simon*aguirre"

# print(cadena)

# lista_de_nombres = cadena.split("*") 
# lista_de_nombres.append("carla") # me agrege un elemento


# # separador = "*"
# cadena = "*".join(lista_de_nombres) # me une todos los elementos de una lista con un *

# print(cadena)

################################## zfill() ###################################################################

# hora = "1:10"

# print(hora)

# hora = hora.zfill(5) # si se pasa de caracteres, agrega un cero.

# print(hora)

################################ isaplha () ##################################################################

# cadena = "skadhfaskj hfkasdj"

# print(cadena)

# booleano = cadena.isalpha() # si se pasa de caracteres, agrega un cero.

# print(booleano)

################################# count() ####################################################################

# cadena = "pedro pedro pedro pedro pedro"

# print(cadena)

# cantidad = cadena.count("pe")  # cuenta cuantas coincidencias hay

# print(cantidad)


################################ format() ###################################################################

# nombre = "jonathan"
# apellido = "aguirre"

# cantidad = "nombre: {0} --- apellido: {1}"

# print(cantidad.format(nombre,apellido)) 

################################# investigar el find  ######################################################

################################# splice()  ################################################################

cadena = "jonathan aguirre"

nombre = cadena[0:8] # incluye la primer posicion y excluye el final
nombre = nombre.capitalize()
apellido = cadena[9:] # me toma del inicio al final si dejo los dos puntos ":"
apellido = apellido.capitalize()

cadena = " ".split(cadena,apellido)     ########## TERMINAR DE RESOLVER ###################################

print(cadena)

