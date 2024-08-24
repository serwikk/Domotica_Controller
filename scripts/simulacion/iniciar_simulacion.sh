cd /home/scalian/Domotica_Controller

source .venv/bin/activate

echo Iniciando simulación...
python3 simulacion.py & 
python3 factores_externos.py & 
