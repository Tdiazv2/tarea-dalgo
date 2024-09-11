import sys

def divide(m: int, monedas: list):
    
    buscado = sum(monedas)/2
    
    lis = [False]*(int(buscado)+1)
    
    lis[0] = True
    
    for moneda in monedas:
        modificados = []
        for i in range(moneda, int(buscado)+1):  
            if not(modificados.__contains__(i-moneda)): 
                lis[i] = lis[i-moneda] or lis[i]
                if lis[i]:
                    modificados.append(i)
    

    for i in range(len(lis)-1,0,-1):
        if lis[i]:
            ultimo = i
            break
    res = abs(ultimo-buscado)
    if res%1 != 0:
        res += 0.5
    return int(res)

if __name__ == "__main__":
    print("")
    number_of_cases = int(sys.stdin.readline().strip())
    res = []
    for _ in range(number_of_cases):
        m = int(sys.stdin.readline())
        values = list(map(int, sys.stdin.readline().split()))
        res.append(divide(m, values))
    
    for i in res:
        print(i)