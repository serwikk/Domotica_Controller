
source .venv/bin/activate

echo Deteniendo simulación...

PID1=$(ps aux | grep python3 | grep simulacion_controlador.py | grep -v grep | awk '{print $2}')
PID2=$(ps aux | grep python3 | grep factores_externos.py | grep -v grep | awk '{print $2}')

if [ -n "$PID1" ]; then
    echo "Deteniendo simulacion.py"
    kill $PID1
else
    echo "simulacion.py ya está detenida"

fi


if [ -n "$PID2" ]; then
    echo "Deteniendo factores_externos.py"
    kill $PID2
else
    echo "factores_externos.py ya está detenida"

fi