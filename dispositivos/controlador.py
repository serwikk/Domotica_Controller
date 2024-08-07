from handlers.generation_handler import generar_id_aleatorio

from dispositivos.sensores.sensor_temperatura import SensorTemperatura
from dispositivos.sensores.sensor_humedad import SensorHumedad
from dispositivos.sensores.sensor_luz import SensorLuz


class Controlador():

    def __init__(self, espacio, nombres_sensores= [], nombres_actuadores = []):
        self.espacio = espacio
        self.id_controlador = generar_id_aleatorio(f"contr-")
        self.sensores = self.inicializar_sensores(nombres_sensores)
        #self.actuadores = self.inicializar_actuadores(nombres_actuadores)

    def inicializar_sensores(self, nombres_sensores):

        sensores = {}

        for sensor in nombres_sensores:

            if sensor == 'sensor_temperatura':
                sensores[sensor] = SensorTemperatura()

            if sensor == 'sensor_humedad':
                sensores[sensor] = SensorHumedad()

            if sensor == 'sensor_luz':
                sensores[sensor] = SensorLuz()


        return sensores


    def inicializar_actuadores(self, nombres_actuadores):

        actuadores = {}

        raise NotImplementedError

        return actuadores