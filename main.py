from dispositivos.controlador import Controlador

from handlers.toml_handler import TOMLHandler


def main():

    config_tomlhandler = TOMLHandler('config.toml')

    habitaculo = config_tomlhandler.obtener_valor('config', 'habitaculo')

    controlador = Controlador(habitaculo, 
                    nombres_sensores=['sensor_temperatura', 'sensor_humedad', 'sensor_luz'],
                    nombres_actuadores=['actuador_persiana', 'actuador_ventana', 'actuador_luz', 'actuador_puerta', 'actuador_climatizador'])

    print(vars(controlador))

    ventana = controlador.actuadores['actuador_ventana']
    ventana.cambiar_valor([1.0, 0.2])

    puerta = controlador.actuadores['actuador_puerta']
    puerta.cambiar_valor([1.0, 0.4])

    persiana = controlador.actuadores['actuador_persiana']
    persiana.cambiar_valor([0.0, 0.6])

    luz = controlador.actuadores['actuador_luz']
    luz.cambiar_valor([1, 500.0])

    climatizador = controlador.actuadores['actuador_climatizador']
    climatizador.cambiar_valor([1.0, 22.0])

if __name__ == "__main__":
    main()