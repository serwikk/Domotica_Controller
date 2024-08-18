from handlers.generation_handler import generar_id_aleatorio
from handlers.toml_handler import TOMLHandler
import random as rd

from dispositivos.actuadores.actuador import Actuador 

class ActuadorClimatizador(Actuador):

    def __init__(self):
        
        super().__init__( id= generar_id_aleatorio("clim-"), tipo_actuador='climatizador')


    def subir_temperatura_ambiente(self):

        temperatura_ambiente = self.valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'temperatura')

        temperatura_ambiente += rd.uniform(0.1, 0.3)
        temperatura_ambiente = round(temperatura_ambiente, 2)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'temperatura', temperatura_ambiente)


    def bajar_temperatura_ambiente(self):

        temperatura_ambiente = self.valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'temperatura')

        temperatura_ambiente -= rd.uniform(0.1, 0.3)
        temperatura_ambiente = round(temperatura_ambiente, 2)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'temperatura', temperatura_ambiente)



