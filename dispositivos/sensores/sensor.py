from handlers.toml_handler import TOMLHandler


class Sensor:

    def __init__(self, id, magnitud, en_funcionamiento, unidad):
        self.id = id
        self.magnitud = magnitud
        self.en_funcionamiento = en_funcionamiento
        self.unidad = unidad
        self.valores_actuales_tomlHandler = TOMLHandler(ruta_archivo='valores_actuales.toml')


    def obtener_valor(self) -> float: 
        """
        Obtiene el valor del sensor

        Returns:
            float: Valor de la magnitud
        """

        return self.valores_actuales_tomlHandler.obtener_valor('valores_magnitudes', self.magnitud)

        
        