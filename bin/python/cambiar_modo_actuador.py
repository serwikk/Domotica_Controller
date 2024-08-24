import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from handlers.toml_handler import TOMLHandler
import argparse


def main():

    config_tomlHandler = TOMLHandler('config.toml')

    actuadores = config_tomlHandler.obtener_valores_seccion('modos').keys()

    parser = argparse.ArgumentParser(description="Script para cambiar el modo del actuador especificado.")

    parser.add_argument('--actuador', '-a', type=str, choices=actuadores,  required=True, help="El actuador del que cambiar el modo.")
    parser.add_argument('--modo', '-m', type=str, choices=['auto', 'off'], required=True, help="El modo al que cambiar el actuador")

    args = parser.parse_args()
    
    config_tomlHandler.establecer_valor('modos', args.actuador, args.modo)



if __name__ == "__main__":
    main()