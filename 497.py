import sys


def SDI(alturas: list):
    
    lis = [1] * len(alturas)
    for i in range(1,len(alturas)):
        maxima = 0
        for j in range(i):
            if alturas[j] < alturas[i]:
                maxima =  max(maxima,lis[j])
        lis[i] = 1 + maxima
        
    maximo = max(lis)
    interceptados = []
    lis = lis[::-1]
    alturas = alturas[::-1]
    for i in range(0,len(lis)):
        if lis[i] == maximo:
            interceptados.append(alturas[i])
            maximo -= 1
            
    return interceptados[::-1]

if __name__ == "__main__":
    largo = int(sys.stdin.readline())
    final = []
    linea = sys.stdin.readline()
    for _ in range(largo):
        linea = sys.stdin.readline()
        values = []
        while linea != '\n':
            values.append(int(linea))
            linea = sys.stdin.readline()
        res = SDI(values)
        final.append((f"Max hits: {len(res)}", res))
        
    for i in final:
        print(i[0])
        for j in i[1]:
            print(j)
        