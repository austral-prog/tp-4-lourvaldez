import math 
def line():
    A= float(input("Ingrese el coeficiente A:"))
    B= float(input("Ingrese el coeficiente B:"))
    X1=float(input("Ingrese el coeficiente X1:"))
    X2=float(input("Ingrese el coeficiente X2:"))
    a="A"
    b="B"
    x1="X1"
    x2="X2"
    verso3= "Para la siguiente ecuación:"
    verso2= "El coeficiente de su ecuación de la recta es:"
    P1= float(A*X1+B)
    P2= float(A*X2+B)
    Distancia= math.sqrt((X2 - X1) ** 2 + (P2 - P1) ** 2)
    print(f"{verso2[0:15]}{a} {verso2[15:]} {A}\n{verso2[0:15]}{b} {verso2[15:]} {B}\n{verso2[0:15]}{x1} {verso2[15:]} {X1}\n{verso2[0:15]}{x2} {verso2[15:]} {X2}\n\n{verso3}\n\tY = {A}X + {B}\n\nDados los siguientes puntos:\n\tP1 ({X1}, {P1})\n\tP2 ({X2}, {P2})")
    print(f"\nLa distancia entre ellos es: {Distancia}")
