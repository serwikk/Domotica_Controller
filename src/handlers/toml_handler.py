import toml
from src.handlers.logger_handler import LoggerHandler
import logging

class TOMLHandler:

    def __init__(self, ruta_archivo, logger=False):
        self.ruta_archivo = ruta_archivo
        if logger:
            self.loggerHandler = LoggerHandler() # TODO
        else:
            self.loggerHandler = None 


    def cargar_toml(self) -> dict:
        """
        Devuelve todos los datos como un diccionario
        """

        with open(self.ruta_archivo, 'r') as archivo:
            return toml.load(archivo)
    

    def guardar_toml(self, valores):
        """
        Guarda los valores actuales en el archivo TOML
        """

        with open(self.ruta_archivo, 'w') as archivo:
            toml.dump(valores, archivo)


    def obtener_valores_seccion(self, seccion) -> dict:
        """
        Devuelve todos los valores de una sección
        """
        valores = self.cargar_toml()

        return valores[seccion]     
    

    def obtener_valor(self, seccion, clave):
        """
        Devuelve el valor de la sección y clave especificadas 
        """

        valores = self.cargar_toml()

        try:
            return valores[seccion][clave]
        
        except KeyError:
            msg = 'Sección o clave no encontrada'
            if self.loggerHandler:
                self.loggerHandler.logger.error(msg)
            return None
        
    
    def establecer_valor(self, seccion, clave, valor):
        """
        Establece un valor específico en una sección y clave del archivo TOML
        """

        valores = self.cargar_toml()

        secciones = seccion.split(".")

        sub_valores = valores

        for sub_seccion in secciones:
            if sub_seccion not in sub_valores:
                sub_valores[sub_seccion] = {}
                if self.loggerHandler:
                    self.loggerHandler.logger.info(f'Sub-sección "{sub_seccion}" creada')

            sub_valores = sub_valores[sub_seccion]

        # Establecer el valor en la clave especificada dentro de la última sub-sección
        sub_valores[clave] = valor

        # Guardar los valores actualizados en el archivo TOML
        self.guardar_toml(valores)
        
        if self.loggerHandler:
            self.loggerHandler.logger.info(f'Clave "{clave}" actualizada en la sección "{seccion}" con el valor: {valor} ({type(valor)})')

