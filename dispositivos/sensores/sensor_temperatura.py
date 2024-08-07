from dispositivos.sensores.sensor import Sensor
from handlers.generation_handler import generar_id_aleatorio


class SensorTemperatura(Sensor):

    def __init__(self, en_funcionamiento = True, unidad='c'):

        super().__init__( id= generar_id_aleatorio("temp-"), magnitud = "temperatura", en_funcionamiento = en_funcionamiento, unidad = unidad)
