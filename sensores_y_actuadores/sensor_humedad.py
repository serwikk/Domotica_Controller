from handlers import generation_handler as fc

from sensores_y_actuadores.sensor import Sensor


class SensorHumedad(Sensor):

    def __init__(self, en_funcionamiento=True, unidad= "%"):
        
        super().__init__( id= fc.generar_id_aleatorio("hum-"), magnitud = "humedad", en_funcionamiento = en_funcionamiento, unidad = unidad)
