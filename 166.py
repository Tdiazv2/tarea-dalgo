import sys
from decimal import Decimal

def cambio(p,monedas,maximo_cambio):

    matriz = [[100000] * (len(monedas) + 1) for _ in range(maximo_cambio + 1)]
    matriz[0] = [0] * (len(monedas) + 1)

    for valor in range(1, maximo_cambio+1):
        for moneda in range(1,len(monedas)+1):
            matriz[valor][moneda]= matriz[valor][moneda-1]
            if valor >= monedas[moneda-1]:
                matriz[valor][moneda] = min(matriz[valor][moneda],matriz[valor-monedas[moneda-1]][moneda-1]+1)

    pagar= organizar(p, maximo_cambio, matriz, True)

    cambio=[1000000]*(1+maximo_cambio)
    cambio[0]=0
    valores_mon = [5, 10, 20, 50, 100, 200]
    for i in range(maximo_cambio+1):
        for j in valores_mon:
            if i >= j:
                cambio[i]=min(cambio[i],cambio[i-j]+1)


    vueltas = organizar(p, maximo_cambio, cambio, False)

    minimo = 10000000000
    for i in range(0,len(vueltas)):
        momento = vueltas[i]+pagar[i]
        if minimo > momento:
            minimo = momento

    
                    
    
    return minimo



def organizar(p, maximo_cambio, matriz, true):
    lista = []
    for i in range(p, maximo_cambio, 5):
        if true:
            lista.append(min(matriz[i]))
        else:
            lista.append(matriz[i])

    return lista




def auxiliar(input):
    valores_mon = [5, 10, 20, 50, 100, 200]

    monedas = list(map(int, input.split()[:6]))
    change = Decimal(input.split()[6])
    p = int(change * 100)
    x=0
    todas_mon =[]
    for i in range(len(valores_mon)):
        todas_mon+= [valores_mon[i]]*monedas[i]

    maximo_cambio=p+max(todas_mon)


    q = cambio(p,todas_mon,maximo_cambio)
    return q



if __name__ == "__main__":
    
    terminal = "0 0 0 0 0 0"
    
    caso = sys.stdin.readline().strip()
    while caso != terminal:
        print(caso)
        caso = sys.stdin.readline().strip()

