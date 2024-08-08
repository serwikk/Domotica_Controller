from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler


class Actuador:

    def __init__(self, id, en_funcionamiento, tipo_actuador):
        self.id = id
        self.en_funcionamiento = en_funcionamiento
        self.valores_actuales_tomlHandler = TOMLHandler(ruta_archivo='valores_actuales.toml')
        self.tipo_actuador = tipo_actuador
        self.estado = self.leer_estado()

    def leer_estado(self):
        return self.valores_actuales_tomlHandler.obtener_valor('estado_actuadores', self.tipo_actuador)

    def cambiar_valor(self, valor):
        # print(f"Antes: self.estado = {self.estado}, valor = {valor}")
        self.estado = valor
        # print(f"Después: self.estado = {self.estado}, valor = {valor}")
        self.valores_actuales_tomlHandler.establecer_valor('estado_actuadores', self.tipo_actuador, valor)
        # print(self.valores_actuales_tomlHandler.obtener_valores_seccion('estado_actuadores'))