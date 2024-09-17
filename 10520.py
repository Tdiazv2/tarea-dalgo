import sys

#Para correr el programa cuando ingresen los datos de prueba por favor presionar enter 2 veces para que imprima los resultados
def determine(n, an1):
    
    a = [0] * (n+1)
    for i in range(n+1):
        a[i] = [0] * (n+1)
    a[n][1] = an1

    for i in range(n,0,-1):  
        for j in range(n+1):   
            if i < j:
                maximo = 0
                for k in range(i, j):
                    if a[i][k] + a[k+1][j] > maximo:
                        maximo = a[i][k] + a[k+1][j]
                a[i][j] = maximo
            else:
                
                maximo1 = 0
                maximo2 = 0
                if i < n:
                    for k in range(i, n+1):
                        if a[k][1] + a[k][j] > maximo1:
                            maximo1 = a[k][1] + a[k][j]
                if j > 0:
                    for k in range(1, j):
                        if a[i][k] + a[n][k] > maximo2:
                            maximo2 = a[i][k] + a[n][k]
                if i != n or j != 1:
                    a[i][j] = maximo1 + maximo2

    return a[1][n]

if __name__ == "__main__":
    
    res = []
    linea =  sys.stdin.readline()
    while linea != '\n':
        datos = list(map(int, linea.split()))
        res.append(determine(datos[0], datos[1]))
        linea =  sys.stdin.readline()
    print("")
    for i in res:
        print(i)
   


