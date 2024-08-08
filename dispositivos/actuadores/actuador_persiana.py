from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler

from dispositivos.actuadores.actuador import Actuador 

class ActuadorPersiana(Actuador):

    def __init__(self, en_funcionamiento=True):
        
        super().__init__( id= generar_id_aleatorio("pers-"), en_funcionamiento = en_funcionamiento)

    def abrir_cerrar_persiana(self, valor):
        self.estado = valor
        self.valores_actuales_tomlHandler.establecer_valor('estado_actuadores', 'persiana', self.estado)