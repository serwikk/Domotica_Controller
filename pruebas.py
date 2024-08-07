from dispositivos.sensores.sensor_temperatura import SensorTemperatura
from dispositivos.sensores.sensor_humedad import SensorHumedad
from dispositivos.sensores.sensor_luz import SensorLuz

from dispositivos.controlador import Controlador

from handlers.toml_handler import TOMLHandler

config_tomlhandler = TOMLHandler('config.toml')

habitaculo = config_tomlhandler.obtener_valor('config', 'habitaculo')

controlador = Controlador(habitaculo, nombres_sensores=['sensor_temperatura', 'sensor_humedad', 'sensor_luz'])

for sensor in controlador.sensores:
    print(controlador.sensores[sensor].obtener_valor())
