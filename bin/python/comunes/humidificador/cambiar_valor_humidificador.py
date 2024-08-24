import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.dispositivos.actuadores.actuador_humidificador import ActuadorHumidificador
from src.handlers.toml_handler import TOMLHandler
import argparse


def main():

    parser = argparse.ArgumentParser(description="Script para cambiar el valor especificado al humidificador.")

    parser.add_argument('--estado', '-e', type=float, help="Establece el valor del humidificador.")

    config_tomlHandler = TOMLHandler('config.toml')

    valores = config_tomlHandler.obtener_valores_seccion('config_controlador')['humidificador']
    humedad_min = valores['humedad_min']
    humedad_max = valores['humedad_max']

    args = parser.parse_args()

    
    actuador_humidificador = ActuadorHumidificador()

    if args.estado >= humedad_min and args.estado <= humedad_max:
        actuador_humidificador.cambiar_estado(args.estado)

    else:
        print(f"Valor no válido: ({args.estado}). Tiene que ser un valor comprendido entre {humedad_min} y {humedad_max}, ambos inclusive")





if __name__ == "__main__":
    main()