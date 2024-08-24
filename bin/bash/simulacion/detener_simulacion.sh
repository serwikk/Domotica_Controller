cd /home/scalian/Domotica_Controller

source .venv/bin/activate

echo Deteniendo simulación...

PID1=$(ps aux | grep python3 | grep simulacion.py | grep -v grep | awk '{print $2}')
PID2=$(ps aux | grep python3 | grep factores_externos.py | grep -v grep | awk '{print $2}')

kill $PID1
kill $PID2