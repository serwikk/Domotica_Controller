cd /home/serwikk/Domotica_Controller

source .venv/bin/activate

echo Iniciando simulación...
python3 bin/python/simulacion_controlador.py & 
python3 bin/python/factores_externos.py & 
