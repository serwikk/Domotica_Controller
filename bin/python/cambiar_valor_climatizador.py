import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dispositivos.actuadores.actuador_climatizador import ActuadorClimatizador
from handlers.toml_handler import TOMLHandler
import argparse


def main():

    parser = argparse.ArgumentParser(description="Script para cambiar el valor especificado al climatizador.")

    parser.add_argument('--estado', '-e', type=float, help="Establece el valor del climatizador.")

    config_tomlHandler = TOMLHandler('config.toml')

    valores = config_tomlHandler.obtener_valores_seccion('config_controlador')['climatizador']
    temperatura_min = valores['temperatura_min']
    temperatura_max = valores['temperatura_max']

    args = parser.parse_args()

    
    actuador_climatizador = ActuadorClimatizador()

    if args.estado >= temperatura_min and args.estado <= temperatura_max:
        actuador_climatizador.cambiar_estado(args.estado)

    else:
        print(f"Valor no válido: ({args.estado}). Tiene que ser un valor comprendido entre {temperatura_min} y {temperatura_max}, ambos inclusive")





if __name__ == "__main__":
    main()