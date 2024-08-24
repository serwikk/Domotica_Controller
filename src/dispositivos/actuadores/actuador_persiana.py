from src.dispositivos.actuadores.actuador import Actuador 

class ActuadorPersiana(Actuador):

    def __init__(self):
        
        super().__init__( prefijo= "persi-", tipo_actuador='persiana')



    def subir_persiana(self, estado_objetivo):

        velocidad_persiana = self.config_tomlHandler.obtener_valor('config_controlador', 'persiana')['velocidad']
        en_funcionamiento_persiana = self.valores_actuales_tomlHandler.obtener_valor('actuadores', 'persiana')['en_funcionamiento']
        estado_persiana = self.valores_actuales_tomlHandler.obtener_valor('actuadores', 'persiana')['estado']

        print(f"Estado actual persiana: {estado_persiana}")
        print(f"Estado objetivo persiana: {estado_objetivo}")


        if estado_objetivo < 0 or estado_objetivo > 1:
            print(f"Los límites de la persiana son 0 y 1")
            return


        if estado_objetivo > estado_persiana:
            self.cambiar_estado(estado_objetivo)
            print(f"Subiendo persiana...\nNuevo estado: {estado_objetivo}")
        else:
            print(f"No es posible subir la persiana a un estado inferior al actual ({estado_persiana})")



    def bajar_persiana(self, estado_objetivo):

        velocidad_persiana = self.config_tomlHandler.obtener_valor('config_controlador', 'persiana')['velocidad']
        en_funcionamiento_persiana = self.valores_actuales_tomlHandler.obtener_valor('actuadores', 'persiana')['en_funcionamiento']
        estado_persiana = self.valores_actuales_tomlHandler.obtener_valor('actuadores', 'persiana')['estado']

        print(f"Estado actual persiana: {estado_persiana}")
        print(f"Estado objetivo persiana: {estado_objetivo}")


        if estado_objetivo < 0 or estado_objetivo > 1:
            print(f"Los límites de la persiana son 0 y 1")
            return


        if estado_objetivo < estado_persiana:
            self.cambiar_estado(estado_objetivo)
            print(f"Bajando persiana...\nNuevo estado: {estado_objetivo}")
        else:
            print(f"No es posible bajar la persiana a un estado inferior al actual ({estado_persiana})")