def costo_minimo_cortes(longitud_madera, posiciones_cortes):
    num_cortes = len(posiciones_cortes)
    cortes = [0] + posiciones_cortes + [longitud_madera]
    dp = [[0] * (num_cortes + 2) for _ in range(num_cortes + 2)]

    for tamaño in range(2, num_cortes + 2):
        for inicio in range(num_cortes + 2 - tamaño):
            fin = inicio + tamaño
            dp[inicio][fin] = 10000000000
            for punto_corte in range(inicio + 1, fin):
                dp[inicio][fin] = min(dp[inicio][fin], dp[inicio][punto_corte] + dp[punto_corte][fin] + cortes[fin] - cortes[inicio])
    
    return dp[0][num_cortes + 1]

def principal():
    import sys
    entrada = sys.stdin.read
    datos = entrada().strip().split()
    
    indice = 0
    resultados = []
    while indice < len(datos):
        longitud = int(datos[indice])
        if longitud == 0:
            break
        
        indice += 1
        cantidad_cortes = int(datos[indice])
        indice += 1
        cortes = list(map(int, datos[indice:indice + cantidad_cortes]))
        indice += cantidad_cortes
        
        costo = costo_minimo_cortes(longitud, cortes)
        resultados.append(f"El costo mínimo de corte es {costo}.")
    
    for resultado in resultados:
        print(resultado)
