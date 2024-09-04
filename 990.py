def diving_for_gold(t_w: tuple, num_treasures: int, list_treasures: list, lista: list, selected_treasures: list):
    if num_treasures <= 0:
        return 0, []

    if lista[num_treasures] >= 0:
        return lista[num_treasures], selected_treasures[num_treasures]

    t = t_w[0]
    w = t_w[1]
    q = 0
    best_combination = []
    
    for i in range(1, num_treasures+1):
        distancia = list_treasures[i - 1][0]
        gold = list_treasures[i - 1][1]
        t_res = t - w * distancia - 2 * w * distancia
        if t_res >= 0:
            current_gold, current_combination = diving_for_gold((t_res, w), num_treasures, list_treasures, lista, selected_treasures)
            if gold + current_gold > q:
                q = gold + current_gold
                best_combination = current_combination + [i  ]  

    lista[num_treasures] = q
    selected_treasures[num_treasures] = best_combination
    
    return q, best_combination


def lista(t_w, num, list_treasure):
    lista = [-10000000] * (num + 1)
    selected_treasures = [[] for _ in range(num + 1)]
    max_gold, treasures_selected = diving_for_gold(t_w, num, list_treasure, lista, selected_treasures)
    final = []
    for a in treasures_selected:
        final.append(list_treasure[a-1])
        
    return max_gold, len(treasures_selected),final



max_gold,cantidad, selected_combination = lista((210, 4), 3, [(40, 5),(10, 1), (7, 2)])
print(f"Máximo oro: {max_gold}")
print(f"Tamaño: {cantidad}")
for i in selected_combination:
    print("Selecciono " +str(i))
