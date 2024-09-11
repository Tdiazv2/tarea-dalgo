import sys
def trainsorting(n,lista):
    r =[1]*n
    for i in range(1,n):
        q=0
        for k in range(i):
            if lista[k]<lista[i]:
                q = max(q,lista[k])

        r[i]=q+1
    
    return max(r)


print(trainsorting(3,[1,2,3]))


if __name__ == "__main__":
    
    
    
    caso = sys.stdin.readline().strip()
    contador = 0
    lista = []
    no = 0
    n = 0
    while caso != "":

        if contador == 0:
            no = caso
        elif contador ==1:
            n =map(int,caso)
        else:

            lista.extend(map(int, caso.split()))
        contador +=1
        caso = sys.stdin.readline().strip()
    print(trainsorting(n,lista))
