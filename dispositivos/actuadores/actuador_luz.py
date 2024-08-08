from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler

from dispositivos.actuadores.actuador import Actuador 

class ActuadorLuz(Actuador):

    def __init__(self, en_funcionamiento=True):
        
        super().__init__( id= generar_id_aleatorio("luz-"), en_funcionamiento = en_funcionamiento, tipo_actuador='luz')

    
    def cambiar_valor(self, valor):
        
        if valor != 0 and valor != 1:
            return
        else:
            self.estado = valor
            self.valores_actuales_tomlHandler.establecer_valor('estado_actuadores', self.tipo_actuador, self.estado)
