from dispositivos.controlador import Controlador

from handlers.toml_handler import TOMLHandler

from time import sleep

config_tomlhandler = TOMLHandler('config.toml')

habitaculo = config_tomlhandler.obtener_valor('config', 'habitaculo')

controlador = Controlador(habitaculo, 
                nombres_sensores=['sensor_temperatura', 'sensor_humedad', 'sensor_luz'],
                nombres_actuadores=['actuador_persiana', 'actuador_ventana', 'actuador_luz', 'actuador_puerta'])

print(vars(controlador))

for sensor in controlador.sensores:
    print(controlador.sensores[sensor].obtener_valor())


controlador.actuadores['actuador_ventana'].cambiar_valor(0.5)
sleep(1)
controlador.actuadores['actuador_puerta'].cambiar_valor(0.1)
sleep(1)
controlador.actuadores['actuador_persiana'].cambiar_valor(0.5)
sleep(1)
controlador.actuadores['actuador_luz'].cambiar_valor(1)
sleep(1)