class Personaje:
    # atributos
    # id - nomnre - usa nano - vuela - super poder - poder pelea
    
    #Constructor: contruye e inicializa un objeto en memoria, le va a dar valores
    
    def __init__(self, id, nombre, nano, vuela, super_poder, poder_pelea):
        self.id = id
        self.nombre = nombre
        self.nanotecnologia = nano
        self.vuela = vuela
        self.super_poder = super_poder
        self.poder_pelea = poder_pelea
    
    
    # metodos
    def presentarse(self):
        cadena = f"{self.nombre} - {self.super_poder}"
        if self.nanotecnologia:
            cadena += f" - Usa Nanotecnologia"
        else:
            cadena += f" - No usa Nanotecnologia"
            
        return cadena
    
    def Volar(self, altura, velocidad):
        if self.vuela:
            print(f"Estoy volando a una altura de {altura} metros, a {velocidad} Km/h")
        else:
            print(f"{self.nombre}: Ud no sabe volar")
            
    def atacar(self, enemigo : 'Personaje'):
        if self.poder_pelea > enemigo.poder_pelea:
            print(f"Gano: {self.nombre}")
            self.poder_pelea -= enemigo.poder_pelea
            enemigo.poder_pelea = 0
        elif self.poder_pelea < enemigo.poder_pelea:
            print(f"Gano: {self.nombre}")
            enemigo.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
        else:
            print("Empataron")