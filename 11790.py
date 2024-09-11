import sys


def murcia(alturas, anchos):
    
    lis = [0]*len(anchos)
    lisD = [0]*len(anchos)
    
    for i in range(len(anchos)):
        lis[i] = anchos[i]
        lisD[i] = anchos[i]
    
    for i in range(1, len(anchos)):
        for j in range(i):
            if alturas[j] < alturas[i]:
                lis[i] = max(lis[i], lis[j] + anchos[i])
    
    for i in range(1, len(anchos)):
        for j in range(i):
            if alturas[j] > alturas[i]:
                lisD[i] = max(lisD[i], lisD[j] + anchos[i])
    
    creciente = max(lis)
    decreciente = max(lisD)
    
    if creciente >= decreciente:
        return(f"Increasing ({creciente}). Decreasing ({decreciente}).")
    else:
        return(f"Decreasing ({decreciente}). Increasing ({creciente}).")

if __name__ == "__main__":
    largo = int(sys.stdin.readline())
    res = []
    for _ in range(largo):
        sys.stdin.readline()
        alturas = list(map(int, sys.stdin.readline().split()))
        anchos = list(map(int, sys.stdin.readline().split()))
        res.append(murcia(alturas, anchos))
    x = 1
    for i in res:
        print(f"Case {x}. {i}")
        x += 1
        