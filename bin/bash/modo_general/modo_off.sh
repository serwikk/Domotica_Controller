cd /home/scalian/Domotica_Controller

source .venv/bin/activate

python3 scripts/cambiar_modo_actuador.py --actuador climatizador --modo off
python3 scripts/cambiar_modo_actuador.py --actuador humidificador --modo off
python3 scripts/cambiar_modo_actuador.py --actuador luz --modo off
python3 scripts/cambiar_modo_actuador.py --actuador ventana --modo off
python3 scripts/cambiar_modo_actuador.py --actuador persiana --modo off