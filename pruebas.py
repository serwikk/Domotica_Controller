from dispositivos.sensores.sensor_temperatura import SensorTemperatura
from dispositivos.sensores.sensor_humedad import SensorHumedad
from dispositivos.sensores.sensor_luz import SensorLuz


sensor_temperatura = SensorTemperatura()
sensor_humedad = SensorHumedad()
sensor_luz = SensorLuz()


temp = sensor_temperatura.obtener_valor()
hum = sensor_humedad.obtener_valor()
lux = sensor_luz.obtener_valor()

print(temp, hum, lux)