from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler


class Actuador:

    def __init__(self, id, tipo_actuador):
        self.id = id
        self.valores_actuales_tomlHandler = TOMLHandler(ruta_archivo='valores_actuales.toml')
        self.tipo_actuador = tipo_actuador
        self.en_funcionamiento = self.leer_valores()['en_funcionamiento']
        self.estado = self.leer_valores()['estado']

    def leer_valores(self):
        return self.valores_actuales_tomlHandler.obtener_valor('actuadores', self.tipo_actuador)

    def cambiar_valor(self, valor):
        self.en_funcionamiento = valor[0]
        self.estado = valor

    
    def encender(self):
        
        encendido = True
        self.en_funcionamiento = encendido

        self.valores_actuales_tomlHandler.establecer_valor(f'actuadores.{self.tipo_actuador}', 'en_funcionamiento', encendido)


    def apagar(self):

        encendido = False
        self.en_funcionamiento = encendido

        self.valores_actuales_tomlHandler.establecer_valor(f'actuadores.{self.tipo_actuador}', 'en_funcionamiento', encendido)

        
