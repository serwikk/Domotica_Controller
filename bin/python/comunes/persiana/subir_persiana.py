import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.dispositivos.actuadores.actuador_persiana import ActuadorPersiana
import argparse


def main():

    parser = argparse.ArgumentParser(description="Script para subir la persiana con el valor especificado.")

    parser.add_argument('--estado', '-e', type=float, help="Establece el valor de la persiana. Valor entre 0 y 1, siendo 0 cerrado totalmente y 1 abierta totalmente")

    args = parser.parse_args()
    
    actuador_persiana = ActuadorPersiana()

    actuador_persiana.subir_persiana(args.estado)





if __name__ == "__main__":
    main()