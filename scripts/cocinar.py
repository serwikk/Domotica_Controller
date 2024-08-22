import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from handlers.toml_handler import TOMLHandler
import argparse
import random as rd
import time


def main():

    valores_actuales_tomlHandler = TOMLHandler('valores_actuales.toml')

    parser = argparse.ArgumentParser(description="Script para simular cocina.")

    parser.add_argument('--segundos', '-s', type=float, help="Tiempo de cocina", required=True)

    args = parser.parse_args()

    
    tiempo_inicio = time.time()

    while True:

        tiempo_actual = time.time()

        temperatura_ambiente = valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'temperatura')
        humedad_ambiente = valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', 'humedad')

        temperatura_ambiente += rd.uniform(0.3, 0.6)
        temperatura_ambiente = round(temperatura_ambiente, 2)

        humedad_ambiente += rd.uniform(0.3, 0.6)
        humedad_ambiente = round(humedad_ambiente, 2)

        if temperatura_ambiente <= 35:
            valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'temperatura', temperatura_ambiente)

        
        if humedad_ambiente <= 70:
            valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'humedad', humedad_ambiente)

            

        if tiempo_actual - tiempo_inicio > args.segundos:
            print(f"Proceso de cocina terminada a los {args.segundos} segundos")
            break

        time.sleep(5)





if __name__ == "__main__":
    main()