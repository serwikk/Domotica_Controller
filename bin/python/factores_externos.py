from handlers.csv_handler import CSVHandler
from handlers.datetime_handler import DatetimeHandler
from handlers.pvlib_handler import PVlibHandler
from handlers.toml_handler import TOMLHandler
from handlers import generation_handler

import logging
from handlers.logger_handler import LoggerHandler
import time


def main():
    """
    Simula los valores externos del habitáculo de las siguientes magnitudes:
        Temperatura (ºC)
        Humedad (%)
        Luz (lux)
    """

    # Invocación de handlers
    datetime_handler = DatetimeHandler()
    loggerHandler = LoggerHandler(f'logs/factores_externos.log', 'factores_externos', logging.INFO)
    valores_actuales_tomlHandler = TOMLHandler('valores_actuales.toml')
    config_tomlHandler = TOMLHandler('config.toml')

    HUSO = config_tomlHandler.obtener_valor('config', 'huso')
    HABITACULO = config_tomlHandler.obtener_valor('config', 'habitaculo')


    print(f"Fecha y hora: {datetime_handler.fecha_completa}")

    # Temperatura
    temperatura_csv_handler = CSVHandler('handlers/csv/temperaturas_hora_mes_vitoria.csv')

    valor_temperatura = temperatura_csv_handler.buscar_valor_temperatura(datetime_handler.hora, DatetimeHandler.obtener_mes_string(datetime_handler.mes))

    valor_temperatura = generation_handler.agregar_umbral_a_valor(valor_temperatura)

    print(f"Temperatura: {valor_temperatura}")

    # Humedad
    humedad_csv_handler = CSVHandler('handlers/csv/humedad_por_habitaciones.csv')

    valores_espacio = humedad_csv_handler.buscar_valor_humedad(HABITACULO)

    valor_humedad = generation_handler.generar_valor_distribucion_normal(valores_espacio[0], valores_espacio[1])

    print(f"Humedad: {valor_humedad}")

    # LUX
    datos_solares = PVlibHandler(logger=True)
    valor_lux = datos_solares.obtener_lux(datetime_handler, config_tomlHandler, valores_actuales_tomlHandler)

    print(f"Luz: {valor_lux}")

    valor_temperatura_final = generation_handler.temperatura_interna_externa(valores_actuales_tomlHandler, config_tomlHandler, valor_temperatura)
    valor_humedad_final = generation_handler.humedad_interna_externa(valores_actuales_tomlHandler, config_tomlHandler, valor_humedad)

    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'temperatura', valor_temperatura_final)
    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'humedad', valor_humedad_final)
    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'luz_ambiente', valor_lux)
    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'luz_resultante', valor_lux)


if __name__=="__main__":

    while True:
        try:
            main()
        
        except Exception as e:
            print(e)
        
        finally:
            time.sleep(60)