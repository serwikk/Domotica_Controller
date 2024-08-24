from src.dispositivos.sensores.sensor import Sensor
from src.handlers.generation_handler import generar_id_aleatorio


class SensorTemperatura(Sensor):

    def __init__(self, en_funcionamiento = True, unidad='c'):

        super().__init__( prefijo= "temp-", magnitud = "temperatura", en_funcionamiento = en_funcionamiento, unidad = unidad)
