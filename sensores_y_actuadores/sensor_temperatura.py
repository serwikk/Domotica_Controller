from handlers import generation_handler as fc

from sensores_y_actuadores.sensor import Sensor


class SensorTemperatura(Sensor):

    def __init__(self, en_funcionamiento = True, unidad='c'):

        super().__init__( id= fc.generar_id_aleatorio("temp-"), magnitud = "temperatura", en_funcionamiento = en_funcionamiento, unidad = unidad)
