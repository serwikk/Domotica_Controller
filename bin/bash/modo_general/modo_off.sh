
source .venv/bin/activate
source bin/bash/config/establecer_pythonpath.sh

python3 bin/python/comunes/cambiar_modo_actuador.py --actuador climatizador --modo off
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador humidificador --modo off
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador luz --modo off
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador ventana --modo off
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador persiana --modo off