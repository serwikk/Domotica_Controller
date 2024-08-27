import logging

class LoggerHandler:

    def __init__(self, nombre_archivo, nombre_logger, nivel):
        self.nombre_archivo = nombre_archivo
        self.nombre_logger = nombre_logger
        self.nivel = self.obtener_nivel_desde_string(nivel)
        
        # Crear un logger para esta instancia de LoggerHandler
        self.logger = logging.getLogger(self.nombre_logger)
        self.logger.setLevel(self.nivel)
        
        # Crear un manejador de archivo
        file_handler = logging.FileHandler(self.nombre_archivo)
        file_handler.setLevel(self.nivel)
        
        # Definir el formato del log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Agregar el manejador al logger
        self.logger.addHandler(file_handler)


    def obtener_nivel_desde_string(self, nivel):

        if not isinstance(nivel, str):
            print("Esto no es un string")
            return nivel

        if nivel.lower() == 'debug':
            return logging.DEBUG
        
        elif nivel.lower() == 'info':
            return logging.INFO
        
        elif nivel.lower() == 'warn':
            return logging.WARN
        
        elif nivel.lower() == 'error':
            return logging.ERROR
        
        elif nivel.lower() == 'critical':
            return logging.CRITICAL


class DebugConsoleLoggerHandler:

    def __init__(self):
        self.logger = logging.getLogger('DebugConsoleLoggerHandler')
        self.logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
