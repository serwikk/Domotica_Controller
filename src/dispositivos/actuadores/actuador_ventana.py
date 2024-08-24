from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler

from dispositivos.actuadores.actuador import Actuador 

class ActuadorVentana(Actuador):

    def __init__(self):
        
        super().__init__( prefijo= "vent-", tipo_actuador='ventana')