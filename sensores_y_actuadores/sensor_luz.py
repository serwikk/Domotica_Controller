from handlers import generation_handler as fc
from sensores_y_actuadores.sensor import Sensor


class SensorLuz(Sensor):

    def __init__(self, en_funcionamiento=True, unidad= "lm"):
        
        super().__init__( id= fc.generar_id_aleatorio("lux-"), magnitud = "luz", en_funcionamiento = en_funcionamiento, unidad = unidad)
