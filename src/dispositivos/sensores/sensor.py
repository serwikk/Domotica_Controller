from src.handlers.toml_handler import TOMLHandler
from src.handlers.generation_handler import generar_id_aleatorio


class Sensor:

    def __init__(self, prefijo, magnitud, en_funcionamiento, unidad):
        self.config_tomlHandler = TOMLHandler(ruta_archivo='config.toml')
        self.magnitud = magnitud
        self.id = self.obtener_id(prefijo)
        self.en_funcionamiento = en_funcionamiento
        self.unidad = unidad
        self.valores_actuales_tomlHandler = TOMLHandler(ruta_archivo='valores_actuales.toml')

        

    def obtener_id(self, prefijo):

        id = self.config_tomlHandler.obtener_valor('ids', self.magnitud)
        if not id:
            print("El sensor no tiene un id asociado")
            id_nuevo = generar_id_aleatorio(prefijo)
            print(f"id nuevo: {id_nuevo}")
            self.config_tomlHandler.establecer_valor('ids', self.magnitud, id_nuevo)

            return id_nuevo

        return id


    def obtener_valor(self) -> float: 
        """
        Obtiene el valor del sensor

        Returns:
            float: Valor de la magnitud
        """

        return self.valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', self.magnitud)

        
        