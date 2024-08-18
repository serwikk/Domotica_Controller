from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler

from dispositivos.actuadores.actuador import Actuador 

class ActuadorLuz(Actuador):

    def __init__(self):
        
        super().__init__( id= generar_id_aleatorio("luz-"), tipo_actuador='luz')

    
    def encender(self):
        super().encender()
        super().cambiar_estado(500)

    def apagar(self):
        super().apagar()
        super().cambiar_estado(0)
