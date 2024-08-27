# Datos generales
**Repositorio**: Domótica_Controller
**Proyecto**: CARE (Centralized Automation for Residential Efficinecy) - Personalización Inteliente para una Experiencia Eficiente en Hogares Automatizados

# Descripción
Este repositorio contiene la preparación e invocación de una infraestructura de controladores, sensores y actuadores simulados para la automatización de un sistema domótico centralizado.

# Contenido

## src
### dispositivos
- controlador.py
#### sensores
#### actuadores

## bin
### bash
#### config
#### modo_general
#### simulacion
### python
- factores_externos.py
- simulacion_controlador.py
#### aseo
#### cocina
#### comunes

## logs

## templates


# Instalación
## 1. Clonar el repositorio
```git clone https://github.com/serwikk/Domotica_Controller.git [nombre_carpeta]```  
cd *[nombre_carpeta]*

## 2. Creación de un entorno virtual
``python3 -m venv .venv``  

## 3. Activación del entorno virtual e instalación de dependencias
``source .venv/bin/activate``  
``pip install -r requirements.txt``

## 4. Establecer PYTHONPATH
``source bin/bash/config/establecer_pythonpath.sh``

## 5. Copiar archivos dentro del directorio *templates* a *toml* 
``cp templates toml``  
``cd toml``  
``mv config.template.toml config.toml``  
``mv valores_actuales.template.toml valores_actuales.toml``  

## 6. Cambiar config.toml según requirimientos

# USO

## Iniciar simulación
``bash bin/bash/simulacion/iniciar_simulación.sh``

## Detener simulación
``bash bin/bash/simulacion/detener_simulacion.sh``

## Poner en modo AUTO todos los actuadores
``bash bin/bash/modo_general/modo_auto.sh``

## Poner en modo OFF todos los actuadores
``bash bin/bash/modo_general/modo_off.sh``

CONTINUAR
