from handlers.generation_handler import generar_id_aleatorio

from dispositivos.sensores.sensor_temperatura import SensorTemperatura
from dispositivos.sensores.sensor_humedad import SensorHumedad
from dispositivos.sensores.sensor_luz import SensorLuz
from dispositivos.sensores.sensor_presencia import SensorPresencia

from dispositivos.actuadores.actuador_persiana import ActuadorPersiana
from dispositivos.actuadores.actuador_ventana import ActuadorVentana
from dispositivos.actuadores.actuador_luz import ActuadorLuz
from dispositivos.actuadores.actuador_puerta import ActuadorPuerta
from dispositivos.actuadores.actuador_climatizador import ActuadorClimatizador
from dispositivos.actuadores.actuador_humidificador import ActuadorHumidificador


class Controlador():

    def __init__(self, espacio, nombres_sensores = [], nombres_actuadores = []):
        self.espacio = espacio
        self.id_controlador = generar_id_aleatorio(f"contr-")
        self.sensores = self.inicializar_sensores(nombres_sensores)
        self.actuadores = self.inicializar_actuadores(nombres_actuadores)

    def inicializar_sensores(self, nombres_sensores):

        sensores = {}

        for sensor in nombres_sensores:

            if sensor == 'sensor_temperatura':
                sensores[sensor] = SensorTemperatura()

            if sensor == 'sensor_humedad':
                sensores[sensor] = SensorHumedad()

            if sensor == 'sensor_luz':
                sensores[sensor] = SensorLuz()

            if sensor == 'sensor_presencia':
                sensores[sensor] = SensorPresencia()


        return sensores


    def inicializar_actuadores(self, nombres_actuadores):

        actuadores = {}

        for actuador in nombres_actuadores:

            if actuador == 'actuador_persiana':
                actuadores[actuador] = ActuadorPersiana()

            if actuador == 'actuador_ventana':
                actuadores[actuador] = ActuadorVentana()

            if actuador == 'actuador_luz':
                actuadores[actuador] = ActuadorLuz()

            if actuador == 'actuador_puerta':
                actuadores[actuador] = ActuadorPuerta()

            if actuador == 'actuador_climatizador':
                actuadores[actuador] = ActuadorClimatizador()

            if actuador == 'actuador_humidificador':
                actuadores[actuador] = ActuadorHumidificador()

        return actuadores

    def obtener_datos_actuales_perifericos(self):

        datos_actuales_perifericos = {}

        for sensor in self.sensores:

            datos_sensor = self.sensores[sensor].obtener_valor()
            datos_actuales_perifericos[sensor] = datos_sensor

        for actuador in self.actuadores:

            datos_actuador = self.actuadores[actuador].leer_valores()
            datos_actuales_perifericos[actuador] = datos_actuador

        
        return datos_actuales_perifericos
    
    @staticmethod
    def gestionar_temperatura(temperatura_ambiente, temperatura_objetivo_climatizador, climatizador, humidificador):
        
        print("---------------------------------------------------------------------------------")
        print(f"Temperatura ambiente: {temperatura_ambiente}ºC")
        print(f"Temperatura objetivo: {temperatura_objetivo_climatizador}ºC")

        if temperatura_ambiente < temperatura_objetivo_climatizador and abs(temperatura_ambiente - temperatura_objetivo_climatizador) > 0.2:
            print(f"Temperatura ambiente ({temperatura_ambiente}ºC) menor que temperatura objetivo ({temperatura_objetivo_climatizador}ºC). Subiendo temperatura...")
            if not climatizador.en_funcionamiento:
                climatizador.encender()
                climatizador.subir_temperatura_ambiente()
                humidificador.bajar_humedad_ambiente()
            else:
                climatizador.subir_temperatura_ambiente()
                humidificador.bajar_humedad_ambiente()

        elif temperatura_ambiente > temperatura_objetivo_climatizador and abs(temperatura_ambiente - temperatura_objetivo_climatizador) > 0.2:
            print(f"Temperatura ambiente ({temperatura_ambiente}ºC) mayor que temperatura objetivo ({temperatura_objetivo_climatizador}ºC). Bajando temperatura...")
            if not climatizador.en_funcionamiento:
                climatizador.encender()
                climatizador.bajar_temperatura_ambiente()
                humidificador.bajar_humedad_ambiente()
            else:
                climatizador.bajar_temperatura_ambiente()
                humidificador.bajar_humedad_ambiente()

        else:
            if climatizador.en_funcionamiento:
                climatizador.apagar()


    @staticmethod
    def gestionar_humedad(humedad_ambiente, humedad_objetivo_humidificador, humidificador):
        
        print("---------------------------------------------------------------------------------")
        print(f"Humedad_ambiente: {humedad_ambiente}%")
        print(f"Humedad objetivo: {humedad_objetivo_humidificador}%")

        config_humidificador = humidificador.config_tomlHandler.obtener_valores_seccion('config_controlador')['humidificador']
        humedad_min, humedad_max = config_humidificador['humedad_min'], config_humidificador['humedad_max']

        if not humidificador.en_funcionamiento:

            if humedad_ambiente < humedad_min:
                humidificador.encender()
                humidificador.subir_humedad_ambiente()
                print(f"Humedad ambiente ({humedad_ambiente}%) menor que humedad mínima ({humedad_min}%). Subiendo humedad...")
            
            elif humedad_ambiente > humedad_max:
                humidificador.encender()
                humidificador.bajar_humedad_ambiente()
                print(f"Humedad ambiente ({humedad_ambiente}%) mayor que humedad máxima ({humedad_max}%). Bajando humedad...")


        elif humidificador.en_funcionamiento:
            
            if humedad_ambiente < humedad_objetivo_humidificador - 1:
                humidificador.subir_humedad_ambiente()
                print(f"Humedad ambiente ({humedad_ambiente}%) menor que humedad objetivo - 1 ({humedad_objetivo_humidificador - 1}%). Subiendo humedad...")
            
            elif humedad_ambiente >= humedad_objetivo_humidificador - 1 and humedad_ambiente <= humedad_objetivo_humidificador + 1:
                print(f"Humedad ambiente ({humedad_ambiente}%) cercana a la humedad objetivo ± 1 ({humedad_objetivo_humidificador - 1} - {humedad_objetivo_humidificador + 1}%).")
                humidificador.apagar()
            
            elif humedad_ambiente > humedad_objetivo_humidificador + 1:
                humidificador.bajar_humedad_ambiente()
                print(f"Humedad ambiente ({humedad_ambiente}%) mayor que humedad objetivo + 1 ({humedad_objetivo_humidificador + 1}%). Bajando humedad...")
            
    @staticmethod
    def gestionar_luz(luz_ambiente, presencia, actuador_luz):
        
        print("---------------------------------------------------------------------------------")
        print(f"Luz ambiente {luz_ambiente}")
        print(f"Presencia: {presencia}")

        if not actuador_luz.en_funcionamiento:

            if presencia:
                actuador_luz.encender()

            else:
                actuador_luz.apagar(luz_ambiente)

        elif actuador_luz.en_funcionamiento:

            if presencia and luz_ambiente < 10:
                actuador_luz.encender()

            else:
                actuador_luz.apagar(luz_ambiente)