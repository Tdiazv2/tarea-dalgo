def SDI(alturas: list):
    
    LIS = [1] * len(alturas)
    for i in range(1,len(alturas)):
        max_lis_sub = 0
        for k in range(i):
            if alturas[k] < alturas[i]:
                max_lis_sub =  max(max_lis_sub,LIS[k])
        LIS[i] = 1 + max_lis_sub
        
    maximo = max(LIS)
    interceptados = []
    LIS = LIS[::-1]
    alturas = alturas[::-1]
    for i in range(0,len(LIS)):
        if LIS[i] == maximo:
            interceptados.append(alturas[i])
            maximo -= 1
            
    return (len(interceptados),interceptados[::-1])

print(SDI([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))