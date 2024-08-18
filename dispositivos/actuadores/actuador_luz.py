from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler

from dispositivos.actuadores.actuador import Actuador 

class ActuadorLuz(Actuador):

    def __init__(self):
        
        super().__init__( id= generar_id_aleatorio("luz-"), tipo_actuador='luz')

    
    def encender(self):

        lux_artificial = 500
        super().encender()
        super().cambiar_estado(lux_artificial)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'lux', lux_artificial)

    def apagar(self, luz_ambiente):
        super().apagar()
        super().cambiar_estado(0)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'lux', luz_ambiente)
