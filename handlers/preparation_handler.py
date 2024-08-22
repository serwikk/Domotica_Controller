

def preparar_datos(datetime_handler, controlador):

    datos = dict()

    variables = vars(controlador)


    #### FECHA ####

    datos['fecha'] = datetime_handler.fecha_completa # Igual el formato de ES es yyyy-MM-dd'T'HH:mm:ss


    #### ESPACIO ####

    datos['espacio'] = variables['espacio']

    #### ID CONTROLADOR ####

    datos['id_controlador'] = variables['id']

    #### SENSORES ####

    sensores = variables['sensores']

    datos['sensores'] = dict()

    for sensor_str in sensores:

        sensor = sensores[sensor_str]
        variables_sensor = vars(sensor)

        datos_sensor = dict()

        datos_sensor['id'] = variables_sensor['id']
        datos_sensor['magnitud'] = variables_sensor['magnitud']
        datos_sensor['unidad'] = variables_sensor['unidad']
        datos_sensor['en_funcionamiento'] = variables_sensor['en_funcionamiento']
        datos_sensor['valor'] = sensor.obtener_valor()

        datos['sensores'][sensor_str] = datos_sensor


    #### ACTUADORES ####

    actuadores = variables['actuadores']

    datos['actuadores'] = dict()

    for actuador_str in actuadores:

        datos_actuador = dict()

        actuador = actuadores[actuador_str]
        variables_actuador = vars(actuador)

        datos_actuador['id'] = variables_actuador['id']
        datos_actuador['tipo_actuador'] = variables_actuador['tipo_actuador']
        datos_actuador['en_funcionamiento'] = variables_actuador['en_funcionamiento']
        datos_actuador['estado'] = variables_actuador['estado']

        datos['actuadores'][actuador_str] = datos_actuador


    #### MODOS ####

    modos = variables['config_tomlHandler'].obtener_valores_seccion('modos')

    datos['modos'] = modos

    return datos