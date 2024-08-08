from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler

from dispositivos.actuadores.actuador import Actuador 

class ActuadorPuerta(Actuador):

    def __init__(self):
        
        super().__init__( id= generar_id_aleatorio("puer-"), tipo_actuador='puerta')