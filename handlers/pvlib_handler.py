import pvlib
from pvlib.location import Location
import pandas as pd
import math
from handlers.datetime_handler import DatetimeHandler
from handlers.csv_handler import CSVHandler
import logging
from handlers.logger_handler import LoggerHandler

class PVlibHandler:

    def __init__(self, latitud=42.84419, longitud=-2.68602, timezone = 'Europe/Madrid', logger=False) -> None:
        self.latitud = latitud
        self.longitud = longitud
        self.timezone = timezone

        if logger:
            self.loggerHandler = LoggerHandler('logs/pvlib.log', 'pvlib', logging.INFO)


    def obtener_valores_posicion_solar_dia_completo(self, dia: str, intervalo: int = 10):

        
        csv_handler = CSVHandler(ruta_archivo=f'resultados/posicion_solar/{DatetimeHandler.fecha_cambiar_formato_fecha(dia)}.csv', 
                                 encabezados=['Hora','Apparent Zenith','Zenith','Apparent Elevation','Elevation','Azimuth','Equation of time'], 
                                 delimiter=';')

        for hora in range(0, 24, 1):

            for minuto in range(0, 60, intervalo):

                datetime_handler = DatetimeHandler(f'{dia} {hora}:{minuto}:00')
                
                location = Location(self.latitud, self.longitud, self.timezone)

                time = pd.Timestamp(datetime_handler.fecha_completa, tz=self.timezone)

                solar_position = location.get_solarposition(time)

                csv_handler.guardar_nuevo_valor(solar_position.to_csv())  # TODO terminar esto no funciona
                  

                break # TODO eliminar
        
            break # TODO eliminar


    def obtener_valor_posicion_solar_actual(self, fecha):
                    

            datetime_handler = DatetimeHandler(f'{fecha.anyo}-{fecha.mes}-{fecha.dia} {fecha.hora}:{fecha.minuto}:{fecha.segundo}')
                
            location = Location(self.latitud, self.longitud, self.timezone)

            time = pd.Timestamp(datetime_handler.fecha_completa, tz=self.timezone)

            solar_position = location.get_solarposition(time)

            return solar_position.to_dict('records')[0]


    def obtener_lux(self, fecha, config_tomlHandler):
        
        # Obtenemos los datos actuales de la posición solar de la fecha introducida
        datos = self.obtener_valor_posicion_solar_actual(fecha)
        elevacion = datos['elevation']
        azimut = datos['azimuth']

        # Obtenemos la lux máxima definida en el apartado 'lux' de 'config.toml'
        lux_max = config_tomlHandler.obtener_valor('lux', 'lux_max_cenit')
        lux_artificial = config_tomlHandler.obtener_valor('lux', 'lux_artificial')

        # logging.info(f"Elevación: {elevacion:.02f}º, Azimut: {azimut:.02f}º")

        # Obtenemos la lux del ambiente
        lux_ambiente = lux_max * math.sin(math.radians(elevacion))

        # logging.info(f"Lux ambiente: {lux_ambiente}")

        ventanas = config_tomlHandler.obtener_valores_seccion('ventanas')

        grados_lux_directa = config_tomlHandler.obtener_valor('lux', 'grados_lux_directa')

        lux_ventanas = {}
        for ventana in ventanas:
            orientacion_ventana = ventanas[ventana]['orientacion']

            # logging.debug(azimut, orientacion_ventana - grados_lux_directa, orientacion_ventana + grados_lux_directa)

            if orientacion_ventana - grados_lux_directa <= azimut <= orientacion_ventana + grados_lux_directa: # Si el sol se encuentra a entre grados_lux_directa grados
                lux_ventanas[ventana] = lux_max * math.sin(math.radians(elevacion))
            else:
                lux_ventanas[ventana]  = lux_ambiente / 2 # Divido entre dos porque lo normal es que si no entra la luz directa, sea menor el numero de lux

        lux_final_habitaculo = max(lux_ventanas.values())

        return round(lux_final_habitaculo, 2)