cd /home/scalian/Domotica_Controller

source .venv/bin/activate

python3 scripts/cambiar_modo_actuador.py --actuador climatizador --modo auto
python3 scripts/cambiar_modo_actuador.py --actuador humidificador --modo auto
python3 scripts/cambiar_modo_actuador.py --actuador luz --modo auto
python3 scripts/cambiar_modo_actuador.py --actuador ventana --modo auto
python3 scripts/cambiar_modo_actuador.py --actuador persiana --modo auto

