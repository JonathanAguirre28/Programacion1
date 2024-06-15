# mi_set = {4,4,8,8,2,5,2,4,9,3,1,9}
# print(mi_set)
# print(type(mi_set))
# for elemento in mi_set:
#     print(elemento)
    
# mi_set.add(6) # agrege un numero
# print(mi_set)

# mi_set.remove(2) # desaparce el numero, tira una acepcion si no lo encuentra
# print(mi_set)

# mi_set.discard(1000) # si lo encuentra lo elimina si no lo encuentra no hace nada 

# elemento = mi_set.pop() # elimina y devuelve
# print(elemento)
# print(mi_set)

set_a = {3,1,5}
set_b = {5,2,4}

# union =  set_a.union(set_b)
# print(union)

# tabla = str.maketrans("abc", "123")

# print(tabla)

interseccion = set_a.difference(set_b) # me muestra lo que esta en set_a y no esta en set_b

print(interseccion)