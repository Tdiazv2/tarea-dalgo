import sys

def dollars(monto: float):
    
    denoms = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
    monto *= 100
    monto = int(round(monto))
    maneras = [0]*(monto+1)
    maneras[0] = 1

    for denom in denoms:
        for i in range(1, monto + 1):
            if denom <= i:
                maneras[i] += maneras[i-denom]
            
    return maneras[monto]

if __name__ == "__main__":
    
    res = []
    dato = 2
    while True:
        if dato == 0.0:
            break
        dato = float(sys.stdin.readline())
        res.append(f"{dato}    {dollars(dato)}")
    print("")
    for i in res:
        print(i)