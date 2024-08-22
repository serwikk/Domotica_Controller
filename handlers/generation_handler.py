import random as rd
import math
import string

import logging
from handlers.logger_handler import LoggerHandler

generation_logger_handler = LoggerHandler('logs/generation_handler.log', 'generation_logger_handler' ,logging.INFO)

def agregar_umbral_a_valor(valor: float, umbral: float = 1) -> float:

    umbral_final = round(rd.uniform(umbral * -1, umbral), 2)

    valor_final = round(valor + umbral_final, 2)

    generation_logger_handler.logger.info(f"Agregado el umbral {umbral_final} al valor {valor}, sumando el valor final de {valor_final}")

    return valor_final



def generar_valor_distribucion_normal(valor_min: float, valor_max: float) -> float:

    media = (valor_min + valor_max) / 2
    desviacion_estandar = round((valor_max - valor_min) / 6, 2)
    valor = rd.gauss(media, desviacion_estandar)

    valor = round(max(valor_min, min(valor, valor_max)), 2)

    generation_logger_handler.logger.info(f"Generado el valor {valor} desde el mínimo {valor_min} y el valor máximo {valor_max}, media {media} y desviación estándar {desviacion_estandar}")

    return valor
    
def generar_valor_polinomico(valor_max, indice):

    k = 10

    return valor_max * (math.log(indice * k + 1) / math.log(k + 1))

#-------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA LA GENERACIÓN DE IDs

def generar_id_aleatorio(prefijo: str = None, longitud: int = 10):
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(rd.choices(caracteres, k=longitud))

    if prefijo:
        id_aleatorio = prefijo + id_aleatorio
    
    return id_aleatorio


#-------------------------------------------------------------------------------------------------------
# FUNCIONES PARA EL MANEJO DE VALORES INTERNOS Y EXTERNOS

def temperatura_interna_externa(valores_actuales_tomlHandler, config_tomlHandler, temperatura_externa):

    aislamiento_termico = config_tomlHandler.obtener_valor('config', 'aislamiento_termico')

    factor_inercia = round(1 - aislamiento_termico, 2)

    temperatura_ambiente = valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'temperatura')

    climatizador_en_funcionamiento = valores_actuales_tomlHandler.obtener_valor('actuadores', 'climatizador')['en_funcionamiento']

    climatizador_auto = config_tomlHandler.obtener_valor('modos', 'climatizador')

    if climatizador_en_funcionamiento and climatizador_auto == "auto":
        return temperatura_ambiente

    else:
        diferencia = round(abs(temperatura_externa - temperatura_ambiente), 2)

        ajuste = diferencia * factor_inercia

        temperatura_ambiente += ajuste

        if temperatura_ambiente < temperatura_externa:

            return round(temperatura_ambiente, 2)

        else:
            return round(temperatura_externa, 2)
        

def humedad_interna_externa(valores_actuales_tomlHandler, config_tomlHandler, humedad_externa):
    

    aislamiento_termico = config_tomlHandler.obtener_valor('config', 'aislamiento_termico')

    factor_inercia = round(1 - aislamiento_termico, 2)

    humedad_ambiente = valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'humedad')

    humidificador_en_funcionamiento = valores_actuales_tomlHandler.obtener_valor('actuadores', 'humidificador')['en_funcionamiento']

    humidificador_auto = config_tomlHandler.obtener_valor('modos', 'humidificador')

    if humidificador_en_funcionamiento and humidificador_auto == "auto":
        return humedad_ambiente

    else:
        diferencia = round(abs(humedad_externa - humedad_ambiente), 2)

        print(f"humedad_externa: {humedad_externa}")
        print(f"humedad_ambiente: {humedad_ambiente}")
        print(f"diferencia: {diferencia}")

        ajuste = diferencia * factor_inercia

        humedad_ambiente += ajuste

        if humedad_ambiente < humedad_externa:

            return round(humedad_ambiente, 2)

        else:
            return round(humedad_externa, 2)