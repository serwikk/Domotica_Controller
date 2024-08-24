from src.dispositivos.actuadores.actuador import Actuador 

class ActuadorVentana(Actuador):

    def __init__(self):
        
        super().__init__( prefijo= "vent-", tipo_actuador='ventana')