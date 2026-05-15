# Indicador-Voltaje-LM339N

Sistema indicador de voltaje basado en comparadores LM339N, lógica digital y modelado en Python para el análisis y procesamiento de señales analógicas.

# Objetivo del Proyecto

Diseñar e implementar un sistema indicador de voltaje basado en comparadores de ventana y lógica digital, capaz de identificar diferentes rangos de voltaje mediante el procesamiento de señales analógicas y generación de estados lógicos, complementándolo con modelado y visualización en Python para el análisis del comportamiento eléctrico del sistema.


# Características Principales

- Diseño e implementación de una etapa de comparación analógica basada en comparadores LM339N.
- Generación de ventanas y subventanas de voltaje para la detección de diferentes niveles eléctricos.
- Cálculo de impedancia equivalente (Rth) para analizar la estabilidad eléctrica de cada etapa del sistema.
- Clasificación automática de impedancia en baja, media y alta impedancia.
- Modelado del sistema en Python para automatizar cálculos eléctricos y validación de resultados.
- Generación de gráficas utilizando Matplotlib para visualizar:
- Ventanas de comparación
- Variación de impedancia
- Comportamiento del sistema
- Desarrollo de una etapa de procesamiento lógico basada en lógica RTL/DTL para la generación de estados digitales.
- Representación lógica y decodificación de señales para visualización mediante display.
- Validación física del sistema mediante implementación y pruebas en protoboard.

# Tecnologías y Herramientas

## Hardware
- Comparador cuádruple LM339N
- Redes de divisores de voltaje
- Transistores BJT
- Diodos
- Display de 7 segmentos
- Protoboard

## Software
- Python 3
- Matplotlib
- Proteus

# Estructura del Proyecto
- Etapa_de_Comparadores
- Etapa_de_Procesamiento
- Decodificacion_y_Visualizacion

Cada etapa contiene:
- Diagramas electrónicos
- Implementación física
- Código de programacion
- Gráficas y documentación técnica
- 
# Gráficas del Sistema


<img width="1280" height="612" alt="Grafica de los rangos de voltaje del  siguiente indicador de voltaje" src="https://github.com/user-attachments/assets/6c71013c-3124-4165-8713-166b20de52ba" />

<img width="1280" height="612" alt="Grafica_impedancias" src="https://github.com/user-attachments/assets/c1e7e5b7-f6e5-474f-ad23-35b47477fe89" />


# Implementación Física

<img width="1429" height="415" alt="Captura de pantalla 2026-05-14 210249" src="https://github.com/user-attachments/assets/59da3a61-4586-4e7e-88c0-886c7909dda6" />


<img width="350" height="285" alt="WhatsApp Image 2026-05-14 at 9 00 48 PM" src="https://github.com/user-attachments/assets/d73b47ec-a677-418e-aa17-cc0e4b40e2e3" />

https://youtu.be/c8F_aoYE-h8?si=y7JQgG75URBMtlrI

# PCB Design
Actualmente el diseño de PCB se encuentra en proceso de desarrollo.
