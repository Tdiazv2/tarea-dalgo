import sys
def Jackpot(lista):
    maximo = 0
    momentanio = 0
    for i in lista:
        
        momentanio = momentanio+i
       
        maximo = max(maximo, momentanio)


    if maximo > 0:
        return f"La máxima ganancia posible es {maximo}"
    else:
        return "Losing streak"




print(Jackpot([12,-4,-10,4,9,3,-2,-1,-2,0]))

if __name__ == "__main__":
    
    terminal = "0"
    
    caso = sys.stdin.readline().strip()
    contador = 0
    lista = []
    while caso != terminal:
        if contador != 0:
            lista.extend(map(int, caso.split()))
        contador +=1
        caso = sys.stdin.readline().strip()
    print(Jackpot(lista))
