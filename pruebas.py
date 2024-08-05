from handlers.pvlib_handler import PVlibHandler


pvlibHandler = PVlibHandler(latitud=0, longitud=1, timezone='Europe/Madrid')

print(vars(pvlibHandler))