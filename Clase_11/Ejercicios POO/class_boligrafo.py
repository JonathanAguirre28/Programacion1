class Boligrafo:
    
    def __init__(self, grosor_punta: str, color: str,):
        self.capacidad_tinta_maxima = None
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = None    
        
    def escribir(self, texto):
        if self.cantidad_tinta == None:
            self.capacidad_tinta_maxima = 100
            self.cantidad_tinta = 80
        print(f"La cantidad maxima de tinta es: {self.capacidad_tinta_maxima}")
        print(f"El grosor de la punta es: {self.grosor_punta}")
        print(f"El color es: {self.color}")
        print(f"La cantidad de la tinta es: {self.cantidad_tinta}")

        if self.grosor_punta == "Grueso":
            if (self.cantidad_tinta) >= len(texto):
                self.cantidad_tinta -= len(texto)*2
                cadena = f"La cantidad de tinta restante es: {self.cantidad_tinta}"
            else:
                cadena = "No alcanza la tinta"
                
        elif self.grosor_punta == "Fino":
            if (self.cantidad_tinta) >= len(texto):
                self.cantidad_tinta -= len(texto)
                cadena = f"La cantidad de tinta restante es: {self.cantidad_tinta}"
            else:
                cadena = "No alcanza la tinta"
            
        return cadena     
        
    def recargar(self, cantidad):

        cantidad = int(input("Ingrese la cantidad de tinta que decea cargar: "))
        cantidad += self.cantidad_tinta
        if cantidad < self.capacidad_tinta_maxima:
            cadena = f"Lapizera recargada te quedo: {cantidad} tinta"
        else:
            cantidad -= self.capacidad_tinta_maxima
            cadena = f"Se recargo la lapizera y sobro {cantidad}"
            
        return cadena
            
            
