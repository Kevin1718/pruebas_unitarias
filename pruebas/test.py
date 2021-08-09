def Orden(orden):
    orden.sort()
    return orden

def Mayor(desc):
    mayor = 0
    for i in desc:
        if i.get("Age") >=18:
            mayor = mayor +1
    print ("Las personas mayores de edad son: ",mayor,"    ")
    return mayor