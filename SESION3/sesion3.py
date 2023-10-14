def numero_es_divisible_entre_2(numero):
    if not numero % 2 == 0:
        return True



numeros = [3, 7, 9, 34, 72, 90, 87, 34, 99, 56, 12, 18]

print(list(filter(numero_es_divisible_entre_2, numeros)))