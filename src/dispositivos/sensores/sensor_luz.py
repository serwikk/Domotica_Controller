from src.dispositivos.sensores.sensor import Sensor
from src.handlers.generation_handler import generar_id_aleatorio


class SensorLuz(Sensor):

    def __init__(self, en_funcionamiento=True, unidad= "lx", magnitud="luz_resultante"):
        
        super().__init__( prefijo= "lux-", magnitud = magnitud, en_funcionamiento = en_funcionamiento, unidad = unidad)
