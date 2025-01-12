def binary_search_iterative(sorted_list: list, target: int) -> int:
    index_inf = 0 #indice inferiore
    index_sup = len(sorted_list) - 1 #indice superiore
    while index_inf <= index_sup:
        print(f"Searching between indices {index_inf} and {index_sup}.")
        index_mid = (index_inf + index_sup) // 2 #calcolo indice el. centrale, arrotondo per difetto per vett. pari
        if sorted_list[index_mid] == target:
            return index_mid  #restituisco la pos. dell'elemento centrale
        elif sorted_list[index_mid] < target:
            index_inf = index_mid + 1 #scorro in avanti
        else: index_sup = index_mid - 1 #posso escludere gli elementi a dx
    return -1
    pass


def binary_search_recursive(sorted_list: list, target: int, left: int, right: int) -> int:
    if(left>right):
        return -1 #non trovato
    else:
        mid = (left + right) // 2
        print(f"Searching between indices {left} and {right}.")
        if sorted_list[mid] == target:
            return mid #trovato subito
        elif sorted_list[mid] < target:
            return binary_search_recursive(sorted_list, target, mid+1, right) #mi sposto a dx
        else:
            return binary_search_recursive(sorted_list, target, left, mid-1)  #mi sposto a sx

    pass
