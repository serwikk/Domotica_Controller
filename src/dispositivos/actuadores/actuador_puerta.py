from src.dispositivos.actuadores.actuador import Actuador 

class ActuadorPuerta(Actuador):

    def __init__(self):
        
        super().__init__( prefijo= "puer-", tipo_actuador='puerta')