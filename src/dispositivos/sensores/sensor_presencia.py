from dispositivos.sensores.sensor import Sensor
from handlers.generation_handler import generar_id_aleatorio


class SensorPresencia(Sensor):

    def __init__(self, en_funcionamiento=True, unidad= ""):
        
        super().__init__( prefijo = "prese-", magnitud = "presencia", en_funcionamiento = en_funcionamiento, unidad = unidad)
