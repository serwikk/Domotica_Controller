import csv
import os
import logging
from handlers.logger_handler import LoggerHandler

class CSVHandler:

    def __init__(self, ruta_archivo, encabezados = None, delimiter=','):
        self.ruta_archivo = ruta_archivo
        self.delimiter = delimiter
        self.generar_archivo(encabezados)
        self.valores = self.cargar_csv()
        self.csv_logger_handler = LoggerHandler('logs/csv_handler.log', 'csv_logger_handler', logging.INFO)

    
    def generar_archivo(self, encabezados):

        if not os.path.exists(self.ruta_archivo):

            with open(self.ruta_archivo, 'w', newline='') as archivo:
                writer = csv.writer(archivo, self.delimiter)
                writer.writerow(encabezados)


    def cargar_csv(self):
        """
        Devuelve todos los datos como un diccionario
        """

        with open(self.ruta_archivo, 'r', newline='') as archivo:

            datos = []
            
            reader = csv.DictReader(archivo, delimiter=self.delimiter)

            for row in reader:

                datos.append(row)

            return datos
    

    def guardar_csv(self):
        """
        Guarda los valores actuales en el archivo CSV
        """

        with open(self.ruta_archivo, 'w') as archivo:
            csv.writer(self.valores, archivo, delimiter=self.delimiter)


    def buscar_valor_temperatura(self, hora, mes):

        for fila in self.valores:

            if fila['hora'] == str(hora):

                try:

                    valor_celda = fila[mes]
                
                    self.csv_logger_handler.logger.info(f"Obtenido el valor {valor_celda} de la hora {hora} del mes de {mes}")

                    return float(valor_celda)
                
                except Exception as e:
                    
                    self.csv_logger_handler.logger.error(e)



    def buscar_valor_humedad(self, espacio: str) -> list:

        for fila in self.valores:

            if fila['espacio'] == espacio:

                valor_min = float(fila['humedad mínima'])
                valor_max = float(fila['humedad máxima'])

                self.csv_logger_handler.logger.info(f"Obtenido los valores mínimo {valor_min} y máximo {valor_max} del espacio {espacio}")

                return [valor_min, valor_max]
            

    def guardar_nuevo_valor(self, valor):
        """
        Guarda un nuevo valor en el CSV
        """

        with open(self.ruta_archivo, 'a') as archivo:
            writer = csv.writer(archivo, delimiter=self.delimiter)
            writer.writerow(valor)


        

            