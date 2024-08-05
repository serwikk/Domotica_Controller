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
    
#-------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA LA GENERACIÓN DE IDs

def generar_id_aleatorio(prefijo: str = None, longitud: int = 10):
    caracteres = string.ascii_letters + string.digits
    id_aleatorio = ''.join(rd.choices(caracteres, k=longitud))

    if prefijo:
        id_aleatorio = prefijo + id_aleatorio
    
    return id_aleatorio