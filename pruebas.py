from dispositivos.controlador import Controlador

from handlers.toml_handler import TOMLHandler

config_tomlhandler = TOMLHandler('config.toml')

habitaculo = config_tomlhandler.obtener_valor('config', 'habitaculo')

controlador = Controlador(habitaculo, 
                nombres_sensores=['sensor_temperatura', 'sensor_humedad', 'sensor_luz'],
                nombres_actuadores=['actuador_persiana'])

print(vars(controlador))

for sensor in controlador.sensores:
    print(controlador.sensores[sensor].obtener_valor())

for actuador in controlador.actuadores:
    print(f"Valor anterior del {actuador}: {controlador.actuadores[actuador].leer_estado()}")

for actuador in controlador.actuadores:

    controlador.actuadores[actuador].abrir_cerrar_persiana(0.3)

for actuador in controlador.actuadores:
    print(f" Valor de {actuador} cambiado a: {controlador.actuadores[actuador].leer_estado()}")

