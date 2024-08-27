
source .venv/bin/activate

python3 bin/python/comunes/cambiar_modo_actuador.py --actuador climatizador --modo auto
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador humidificador --modo auto
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador luz --modo auto
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador ventana --modo auto
python3 bin/python/comunes/cambiar_modo_actuador.py --actuador persiana --modo auto

