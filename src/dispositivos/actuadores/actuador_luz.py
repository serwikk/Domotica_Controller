from src.dispositivos.actuadores.actuador import Actuador

class ActuadorLuz(Actuador):

    def __init__(self):
        
        super().__init__( prefijo= "luz-", tipo_actuador='luz')

    
    def encender(self):

        lux_artificial = 500
        super().encender()
        super().cambiar_estado(lux_artificial)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'luz_resultante', lux_artificial)

    def apagar(self, luz_ambiente):
        super().apagar()
        super().cambiar_estado(0)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'luz_resultante', luz_ambiente)
