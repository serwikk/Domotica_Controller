from sensores_y_actuadores import sensor_temperatura as st, sensor_humedad as sh, sensor_luz as sl
from handlers import generation_handler as gh

class Controlador():

    def __init__(self, espacio, sensores= []):
        self.espacio = espacio
        self.id_controlador = gh.generar_id_aleatorio(f"contr-")
        self.sensores = sensores
        self.lista_nombres_sensores = self.obtener_nombres_sensores()


    def obtener_nombres_sensores(self) -> list:

        lista_nombres_sensores = []
        
        for sensor in self.sensores:
            lista_nombres_sensores.append("sensor_"+sensor.magnitud)

        return lista_nombres_sensores
