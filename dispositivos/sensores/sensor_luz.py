from dispositivos.sensores.sensor import Sensor
from handlers.generation_handler import generar_id_aleatorio


class SensorLuz(Sensor):

    def __init__(self, en_funcionamiento=True, unidad= "lx"):
        
        super().__init__( id= generar_id_aleatorio("lux-"), magnitud = "lux", en_funcionamiento = en_funcionamiento, unidad = unidad)
