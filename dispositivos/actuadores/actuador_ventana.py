from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler

from dispositivos.actuadores.actuador import Actuador 

class ActuadorVentana(Actuador):

    def __init__(self, en_funcionamiento=True):
        
        super().__init__( id= generar_id_aleatorio("vent-"), en_funcionamiento = en_funcionamiento, tipo_actuador='ventana')