from dispositivos.controlador import Controlador

from handlers.toml_handler import TOMLHandler
from handlers.logger_handler import LoggerHandler, DebugConsoleLoggerHandler
from handlers.datetime_handler import DatetimeHandler
import logging
from time import sleep

def main():
    
    debug_logger_handler = DebugConsoleLoggerHandler()

    datetime_handler = DatetimeHandler()

    config_tomlhandler = TOMLHandler('config.toml')

    habitaculo = config_tomlhandler.obtener_valor('config', 'habitaculo')

    modos = config_tomlhandler.obtener_valores_seccion('modos')

    controlador = Controlador(habitaculo, 
                    nombres_sensores=['sensor_temperatura', 'sensor_humedad', 'sensor_luz', 'sensor_presencia'],
                    nombres_actuadores=['actuador_persiana', 'actuador_ventana', 'actuador_luz', 'actuador_puerta', 'actuador_climatizador', 'actuador_humidificador'])

    # debug_logger_handler.logger.debug(vars(controlador))

    print(datetime_handler.fecha_completa)

    actuador_ventana = controlador.actuadores['actuador_ventana']

    actuador_puerta = controlador.actuadores['actuador_puerta']

    actuador_persiana = controlador.actuadores['actuador_persiana']

    actuador_luz = controlador.actuadores['actuador_luz']

    actuador_climatizador = controlador.actuadores['actuador_climatizador']

    actuador_humidificador = controlador.actuadores['actuador_humidificador']

    datos_actuales_perifericos = controlador.obtener_datos_actuales_perifericos()

    # print(datos_actuales_perifericos)

    temperatura_ambiente = datos_actuales_perifericos['sensor_temperatura']
    temperatura_objetivo_climatizador = datos_actuales_perifericos['actuador_climatizador']['estado']


    humedad_ambiente = datos_actuales_perifericos['sensor_humedad']
    humedad_objetivo_humidificador = datos_actuales_perifericos['actuador_humidificador']['estado']


    luz_resultante = datos_actuales_perifericos['sensor_luz']
    presencia = datos_actuales_perifericos['sensor_presencia']

    if modos['climatizador'] == 'auto':
        
        print("---------------------------------------------------------------------------------")
        print("Modo climatizador AUTO")
        Controlador.gestionar_temperatura(temperatura_ambiente, temperatura_objetivo_climatizador, actuador_climatizador, actuador_humidificador)


    if modos['humidificador'] == 'auto':
        
        print("---------------------------------------------------------------------------------")
        print("Modo humidificador AUTO")
        Controlador.gestionar_humedad(humedad_ambiente, humedad_objetivo_humidificador, actuador_humidificador)


    if modos['luz'] == 'auto':
        
        print("---------------------------------------------------------------------------------")
        print("Modo luz AUTO")
        Controlador.gestionar_luz(luz_resultante, presencia, actuador_luz)

        


if __name__ == "__main__":

    while True:
        main()
        sleep(5)