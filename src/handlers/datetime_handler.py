import datetime

class DatetimeHandler:

    def __init__(self, fecha_completa = None) -> None:

        if not fecha_completa:
            self.fecha_completa = datetime.datetime.now()
        else:
            self.fecha_completa = self.fecha_string_a_datetime(fecha_completa)

        self.anyo = self.fecha_completa.year
        self.mes = self.fecha_completa.month
        self.dia = self.fecha_completa.day
        self.hora = self.fecha_completa.hour
        self.minuto = self.fecha_completa.minute
        self.segundo = self.fecha_completa.second
        self.microsegundos = self.fecha_completa.microsecond

    @staticmethod
    def fecha_string_a_datetime(fecha: str) -> datetime.datetime.strptime:

        return datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    
    @staticmethod
    def fecha_cambiar_formato_fecha(fecha: str, formato: str = '%Y%m%d'):

        return datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime(formato)

    @staticmethod
    def obtener_mes_string(indice_mes) -> str:

        meses_dictionario = {
            1: 'enero',
            2: 'febrero',
            3: 'marzo',
            4: 'abril',
            5: 'mayo',
            6: 'junio',
            7: 'julio',
            8: 'agosto',
            9: 'septiembre',
            10: 'octubre',
            11: 'noviembre',
            12: 'diciembre'
        }

        return meses_dictionario[indice_mes]