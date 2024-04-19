def leap_year():
    año=int(input("Ingrese un año: "))
    if (año%4==0) and (año%100==0) and (año%400==0):
        line_1=f"{año} es"
    else:
        line_1=f"{año} no es"

    print(f"El año {line_1} bisiesto")
