import sys
import os

# Añadir la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.handlers.csv_handler import CSVHandler
from src.handlers.datetime_handler import DatetimeHandler
from src.handlers.pvlib_handler import PVlibHandler
from src.handlers.toml_handler import TOMLHandler
from src.handlers.logger_handler import LoggerHandler
from src.handlers import generation_handler

import logging
import time


def main():
    """
    Simula los valores externos del habitáculo de las siguientes magnitudes:
        Temperatura (ºC)
        Humedad (%)
        Luz (lux)
    """

    # Invocación de handlers

    def obtener_habitaculo_sin_numero(habitaculo):
        
        if "dormitorio" in habitaculo:
            return "dormitorio"
        
        if "aseo" in habitaculo:
            return "aseo"
        
        if "cocina" in habitaculo:
            return "cocina"
        
    
    
    datetime_handler = DatetimeHandler()


    HUSO = config_tomlHandler.obtener_valor('config', 'huso')
    HABITACULO = obtener_habitaculo_sin_numero(config_tomlHandler.obtener_valor('config', 'habitaculo'))


    # Temperatura
    temperatura_csv_handler = CSVHandler('src/handlers/csv/temperaturas_hora_mes_vitoria.csv')

    valor_temperatura = temperatura_csv_handler.buscar_valor_temperatura(datetime_handler.hora, DatetimeHandler.obtener_mes_string(datetime_handler.mes))

    valor_temperatura = generation_handler.agregar_umbral_a_valor(valor_temperatura)


    # Humedad
    humedad_csv_handler = CSVHandler('src/handlers/csv/humedad_por_habitaciones.csv')

    valores_espacio = humedad_csv_handler.buscar_valor_humedad(HABITACULO)

    valor_humedad = generation_handler.generar_valor_distribucion_normal(valores_espacio[0], valores_espacio[1])


    # LUX
    datos_solares = PVlibHandler(logger=True)
    valor_lux_ambiente, valor_lux_resultante = datos_solares.obtener_lux(datetime_handler, config_tomlHandler, valores_actuales_tomlHandler)


    valor_temperatura_final = generation_handler.temperatura_interna_externa(valores_actuales_tomlHandler, config_tomlHandler, valor_temperatura)
    valor_humedad_final = generation_handler.humedad_interna_externa(valores_actuales_tomlHandler, config_tomlHandler, valor_humedad)

    loggerHandler.logger.info(f"Temperatura: {valor_temperatura}, Humedad: {valor_humedad}, Luz ambiente: {valor_lux_ambiente}, Luz resultante: {valor_lux_resultante}")


    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'temperatura', valor_temperatura_final)
    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'humedad', valor_humedad_final)
    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'luz_ambiente', valor_lux_ambiente)
    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'luz_resultante', valor_lux_resultante)


if __name__=="__main__":
    loggerHandler = LoggerHandler(f'logs/factores_externos.log', 'factores_externos', 'info')
    valores_actuales_tomlHandler = TOMLHandler('toml/valores_actuales.toml')
    config_tomlHandler = TOMLHandler('toml/config.toml')

    while True:
       
        main()
    
    
        time.sleep(60)