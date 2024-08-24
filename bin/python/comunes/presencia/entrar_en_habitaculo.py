import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from handlers.toml_handler import TOMLHandler


def main():

    valores_actuales_tomlHandler = TOMLHandler('valores_actuales.toml')

    valores_actuales_tomlHandler.establecer_valor('valores_magnitudes', 'presencia', True)




if __name__ == "__main__":
    main()