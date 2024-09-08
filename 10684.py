def Jackpot(lista, maximo):
    momentanio = 0
    for i in lista:
        
        momentanio = momentanio+i
       
        maximo = max(maximo, momentanio)


    if maximo > 0:
        return f"La máxima ganancia posible es {maximo}"
    else:
        return "Losing streak"




print(Jackpot([5,12,-4,-10,4,9,3,-2,-1,-2,0],0))