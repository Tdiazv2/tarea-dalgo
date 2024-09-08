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