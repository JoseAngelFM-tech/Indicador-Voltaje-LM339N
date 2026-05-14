#Etapa de comparadores
import matplotlib.pyplot as plt
unidad="V"
V_fuente=float(input("El voltaje de la fuente en (V) : "))
print(V_fuente,unidad)
com=float(input("Ingrese el voltaje del comparador en(V):"))
print(com,unidad)
voltajes=[]
impedancias=[]

def calculo_comparador(V_fuente,com,Rk):
    R1=Rk*1000
    V=((V_fuente/com)-1)
    R2=(R1/V)
    Vout=(R2/(R1+R2))*V_fuente
    Z=((R1*R2)/(R1+R2))
    return R2,Vout,Z

def clasificar_impedancia(Z):

    if(Z<10000):
        print(F"El valor de impedancia es Baja: {Z:.3f} Ω")
    elif(Z>=10000 and Z<100000):
        print(f"El valor de impedancia es Media: {Z:.3f} Ω")
    elif(Z>=100000):
        print(f"El valor de impedancia es Alta: {Z:.3f} Ω")

def Error_Corriente(Z):
    I_min=(25/1000000000)
    I_max=(250/1000000000)
    V_min=I_min*Z
    V_max=I_max*Z
    return V_min,V_max,I_min,I_max
def Porcentaje_Error(Vout,V_min,V_max):
    Error_min=(V_min/Vout)*(100)
    Error_max=(V_max/Vout)*(100)
    return Error_min,Error_max

Resolucion=float(input("Dime la resolución en mV: "))
print(Resolucion,"mV")

def Porcentaje_Resolucion(V_min,V_max,Resolucion):
 Res=Resolucion/1000
 Res_min=(V_min/Res)*(100)
 Res_max=(V_max/Res)*(100)
 return Res_min,Res_max,Res
while(com<2.3):

    voltajes.append(com)
    R="kΩ"
    Rk=float(input("Ingrese el valor de R1 en (KΩ): "))
    print(Rk,R)

    # Llamada a la funcion
    R2, Vout, Z = calculo_comparador(V_fuente, com, Rk)

    impedancias.append(Z)
    # Clasificacion de impedancia
    clasificar_impedancia(Z)

    print(f"La resistencia requerida en R2 es: {R2:.2f} Ω")

    print(f"El voltaje de salida es: {Vout:.2f} V")
    
    V_min,V_max,I_min,I_max=Error_Corriente(Z)
    Error_min,Error_max=Porcentaje_Error(Vout,V_min,V_max)
    Res_min,Res_max,Res=Porcentaje_Resolucion(V_min,V_max,Resolucion)

    print(f"Error a 25°C (Ib=25nA): {(V_min*1000000):.4f} µV")
    print(f"El porcentaje de Error a 25°C(Ib=25nA):{Error_min:.6f}%")
    print(f"Error respecto a la resolución: {Res_min:.6f}%")
    print(f"Error a 70°C (Ib=250nA): {(V_max*1000000):.4f} µV")
    print(f"El porcentaje de Error a 70°C(Ib=250nA):{Error_max:.6f}%")
    print(f"Error respecto a la resolución: {Res_max:.6f}%")

    com += 0.2


def grafica_ventana(voltajes):

    plt.figure(figsize=(14,7))
    # VENTANA PRINCIPAL
    
    plt.barh(
        y=0,
        width=1.4,
        left=0.7,
        height=0.6,
        edgecolor='black',
        alpha=0.8
    )

    # SUBVENTANAS

    for i, v in enumerate(voltajes):

        plt.barh(
            y=i+1,
            width=0.2,
            left=v,
            height=0.5,
            edgecolor='black',
            alpha=0.8
        )

    plt.title("Gráfica del Indicador de Voltaje")
    plt.xlabel("Rango de Voltaje (V)")
    plt.ylabel("Comparadores")

    plt.xticks([0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1])

    # etiquetas del eje Y
    etiquetas = ["General"]
    for i in range(len(voltajes)):
        etiquetas.append(f"C{i+1}")

    plt.yticks(range(0, len(voltajes)+1), etiquetas)

    plt.grid(True)
    plt.show()
    


def grafica_impedancias(voltajes,impedancias):

    plt.plot(voltajes,impedancias,marker="o")

    plt.title("Variación de la Impedancia Equivalente (Rth) en función del Voltaje")
    plt.xlabel("Nivel de Voltaje de cada Comparador(V)")
    plt.ylabel("Impedancia Equivalente  Rth(Ω)")
    plt.plot([], [], color='Green', linestyle='-', label=' Impedancia Baja < 10,000 Ω')
    plt.plot([], [], color='yellow', linestyle='-', label='Impedancia Media >= 10,000 Ω y <= 100,000 Ω')
    plt.plot([], [], color='Red', linestyle='-', label='Impedancia Alta  >= 100,000 Ω')
    plt.legend()
  
    plt.grid(True)
    
    plt.show()

# LLAMAR GRAFICA
grafica_ventana(voltajes)
grafica_impedancias(voltajes,impedancias)



