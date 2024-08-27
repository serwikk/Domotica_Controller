from src.dispositivos.actuadores.actuador import Actuador 

import random as rd

class ActuadorHumidificador(Actuador):

    def __init__(self):
        
        super().__init__( prefijo = "humid-", tipo_actuador='humidificador')


    def subir_humedad_ambiente(self):

        humedad_ambiente = self.valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'humedad')

        humedad_ambiente += rd.uniform(0.5, 0.8)
        humedad_ambiente = round(humedad_ambiente, 2)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'humedad', humedad_ambiente)


    def bajar_humedad_ambiente(self):

        humedad_ambiente = self.valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'humedad')

        humedad_ambiente -= rd.uniform(0.5, 0.8)
        humedad_ambiente = round(humedad_ambiente, 2)

        self.valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'humedad', humedad_ambiente)
