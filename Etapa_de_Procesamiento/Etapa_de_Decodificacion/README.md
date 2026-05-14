# Etapa de Decodificación

En la etapa de decodificación, los comparadores de ventana previamente configurados generaron un código de umbrales en estados lógicos, permitiendo establecer comunicación entre la etapa analógica y la etapa digital del sistema.
A partir de las señales digitales provenientes de la etapa de procesamiento, se desarrolló la lógica de decodificación encargada de interpretar cada combinación lógica correspondiente a las diferentes ventanas de voltaje detectadas por el sistema.

Durante el desarrollo se realizó el análisis lógico para la activación de segmentos mediante compuertas lógicas NOR, OR y NOT, determinando las condiciones necesarias para cada estado digital.
Se desarrollaron tablas de visualización para displays de siete segmentos, donde cada combinación lógica activa segmentos específicos correspondientes a las unidades y decenas del sistema indicador.

Cada función lógica fue validada mediante tablas de verdad y análisis de estados lógicos, permitiendo verificar el comportamiento correcto del sistema de decodificación.
Finalmente, la implementación física se realizó utilizando lógica DTL/RTL, permitiendo validar experimentalmente el funcionamiento de la etapa de decodificación, la correcta generación de salidas digitales y la visualización de los diferentes rangos de voltaje detectados por el sistema.
