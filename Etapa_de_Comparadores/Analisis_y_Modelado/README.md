# Resultados de la Terminal

Los resultados del código previamente desarrollado mostraron la interacción entre el usuario y la interfaz de ejecución en Python, permitiendo ingresar parámetros fundamentales para el diseño de la etapa de comparadores.

El programa permite definir manualmente el valor de la resistencia R1 dependiendo de la serie comercial de resistencias utilizada. En este proyecto se emplearon resistores de precisión de la serie E96 con tolerancia del 1 %, permitiendo mejorar la estabilidad y precisión de las subventanas de voltaje generadas por los comparadores LM339N.

Además, el sistema automatiza los cálculos eléctricos a partir de parámetros definidos por el usuario, tales como:

- Voltaje de la fuente.
- Voltaje inicial del comparador.
- Resolución deseada del sistema.
- Valor de la resistencia R1.

A partir de estos datos, el programa calcula automáticamente:

- Resistencia requerida en R2.
- Voltaje de salida esperado.
- Impedancia equivalente (Rth).
- Clasificación de impedancia.
- Error producido por la corriente de bias del LM339N.
- Porcentaje de error respecto a la resolución del sistema.

Durante una de las ejecuciones realizadas con una fuente de 5 V, un comparador configurado a 0.7 V, una resolución de 200 mV y una resistencia R1 de 5.6 kΩ, se obtuvo una impedancia equivalente de 784 Ω clasificada como baja impedancia.

El sistema calculó automáticamente una resistencia R2 de 911.63 Ω, obteniendo un voltaje de salida de 0.70 V correspondiente a la subventana analizada.

Asimismo, se realizó el análisis del error producido por la corriente de polarización de entrada del LM339N, obteniendo un error de 19.6 µV a 25°C y 196 µV a 70°C. Los porcentajes de error respecto a la resolución del sistema permanecieron inferiores al 0.1 %, demostrando que la impedancia equivalente calculada no afecta significativamente la estabilidad ni la precisión de las subventanas de detección.

Debido a que el proceso se ejecuta iterativamente para cada comparador de ventana, el programa genera resultados distintos dependiendo de los niveles de voltaje configurados dentro del sistema indicador.

