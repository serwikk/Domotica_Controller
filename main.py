from dispositivos.controlador import Controlador

from handlers.toml_handler import TOMLHandler
from handlers.logger_handler import LoggerHandler, DebugConsoleLoggerHandler
import logging
import math


def main():
    
    debug_logger_handler = DebugConsoleLoggerHandler()

    config_tomlhandler = TOMLHandler('config.toml')

    habitaculo = config_tomlhandler.obtener_valor('config', 'habitaculo')

    controlador = Controlador(habitaculo, 
                    nombres_sensores=['sensor_temperatura', 'sensor_humedad', 'sensor_luz'],
                    nombres_actuadores=['actuador_persiana', 'actuador_ventana', 'actuador_luz', 'actuador_puerta', 'actuador_climatizador'])

    # debug_logger_handler.logger.debug(vars(controlador))

    ventana = controlador.actuadores['actuador_ventana']

    puerta = controlador.actuadores['actuador_puerta']

    persiana = controlador.actuadores['actuador_persiana']

    luz = controlador.actuadores['actuador_luz']

    climatizador = controlador.actuadores['actuador_climatizador']

    luz.apagar()

    datos_actuales_perifericos = controlador.obtener_datos_actuales_perifericos()

    print(datos_actuales_perifericos)

    temperatura_ambiente = datos_actuales_perifericos['sensor_temperatura']
    # temperatura_objetivo_climatizador

    return

    if abs(temperatura_ambiente - datos_actuales_perifericos['actuador_climatizador'][1]) > 1:
        # print(f"diferencia: {}")
        pass

    if climatizador.en_funcionamiento == 1.0:
        print("El climatizador está encendido")

    if climatizador.en_funcionamiento == 0.0:
        print("El climatizador está apagado")


if __name__ == "__main__":
    main()