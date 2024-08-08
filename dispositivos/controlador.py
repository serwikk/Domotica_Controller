from handlers.generation_handler import generar_id_aleatorio

from dispositivos.sensores.sensor_temperatura import SensorTemperatura
from dispositivos.sensores.sensor_humedad import SensorHumedad
from dispositivos.sensores.sensor_luz import SensorLuz

from dispositivos.actuadores.actuador_persiana import ActuadorPersiana
from dispositivos.actuadores.actuador_ventana import ActuadorVentana
from dispositivos.actuadores.actuador_luz import ActuadorLuz
from dispositivos.actuadores.actuador_puerta import ActuadorPuerta
from dispositivos.actuadores.actuador_climatizador import ActuadorClimatizador


class Controlador():

    def __init__(self, espacio, nombres_sensores= [], nombres_actuadores = []):
        self.espacio = espacio
        self.id_controlador = generar_id_aleatorio(f"contr-")
        self.sensores = self.inicializar_sensores(nombres_sensores)
        self.actuadores = self.inicializar_actuadores(nombres_actuadores)

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

        for actuador in nombres_actuadores:

            if actuador == 'actuador_persiana':
                actuadores[actuador] = ActuadorPersiana()

            if actuador == 'actuador_ventana':
                actuadores[actuador] = ActuadorVentana()

            if actuador == 'actuador_luz':
                actuadores[actuador] = ActuadorLuz()

            if actuador == 'actuador_puerta':
                actuadores[actuador] = ActuadorPuerta()

            if actuador == 'actuador_climatizador':
                actuadores[actuador] = ActuadorClimatizador()

        return actuadores