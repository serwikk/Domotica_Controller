
source .venv/bin/activate

echo Iniciando simulación...
nohup python3 bin/python/simulacion_controlador.py & 
nohup python3 bin/python/factores_externos.py & 
