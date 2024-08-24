
from elasticsearch import Elasticsearch
import pytz
from datetime import datetime, timedelta

from src.handlers.toml_handler import TOMLHandler

class ESHandler:

    def __init__(self):

        self.config_tomlHandler = TOMLHandler('config.toml')
        self.es = Elasticsearch(self.config_tomlHandler.obtener_valor('es', 'url'))
        self.conexion_exitosa = self.conectar()


    def conectar(self):

        if self.es.ping():
            # print("Conectado a Elasticsearch")
            return True

        else:
            # print("No se puede conectar a Elasticsearch")
            return False
        

    def obtener_fecha_correcta_para_ES(self, fecha):

        huso_config = self.config_tomlHandler.obtener_valor('config', 'huso')

        timezone = pytz.timezone(huso_config)

        spain_time = datetime.now(timezone)

        is_dist = spain_time.dst() != timedelta(0)

        if is_dist:
            time = fecha.replace(tzinfo=pytz.utc).astimezone(timezone) - timedelta(hours=2)

        else:
            time = fecha.replace(tzinfo=pytz.utc).astimezone(timezone) - timedelta(hours=1)

        return time
    

    def enviar_datos(self, indice, datos):

        datos['fecha'] = self.obtener_fecha_correcta_para_ES(datos['fecha'])

        if self.conexion_exitosa:

            response = self.es.index(index=indice, document=datos)
            # print(response)