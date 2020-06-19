import random
dados_ataque = [0, 0, 0]
dados_defensa = [0, 0, 0]
cant_d_ataque = 3
cant_d_defensa = 2
for x in range(0, 3):
    if (x + 1) <= cant_d_ataque:
        dados_ataque[x] = random.randint(1, 6)
        print('ataque: ' + str(dados_ataque[x]))
    if (x + 1) <= cant_d_defensa:
        dados_defensa[x] = random.randint(1, 6)
        print('defensa: ' + str(dados_defensa[x]))

dados_ataque.sort(reverse=True)
dados_defensa.sort(reverse=True)
print(dados_ataque)
print(dados_defensa)
