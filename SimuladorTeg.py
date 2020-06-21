import random
dados_ataque = [0, 0, 0]
dados_defensa = [0, 0, 0]
fichas_ataque = 6
fichas_defensa = 4
simulaciones = 10000
vict_ataque = 0
vict_defensa = 0
cant_d_defensa = 0
cant_d_ataque = 0


def jugar(fatq, fdef):

    global cant_d_ataque
    global cant_d_defensa
    comparar = 3
    while fatq > 1 and fdef > 0:
        if fatq > 3: cant_d_ataque = 3
        elif fatq == 3: cant_d_ataque = 2
        else: cant_d_ataque = 1

        if fdef >= 3: cant_d_defensa = 3
        elif fdef == 2: cant_d_defensa = 2
        else: cant_d_defensa = 1

        tirar_dados()
        if cant_d_ataque <= cant_d_defensa:
            comparar = cant_d_ataque
        else: comparar = cant_d_defensa

        for comp in range(0, comparar):
            if dados_ataque[comp] > dados_defensa[comp]:
                fdef -= 1
            else: fatq -= 1
    print(fatq)
    print(fdef)
    if fdef == 0: return "gana ataque"
    else: return "gana defensa "


def tirar_dados():
    global cant_d_ataque
    global cant_d_defensa
    global dados_ataque
    global dados_defensa
    dados_ataque = [0, 0, 0]
    dados_defensa = [0, 0, 0]
    for x in range(0, 3):
        if (x + 1) <= cant_d_ataque:
            dados_ataque[x] = random.randint(1, 6)
        if (x + 1) <= cant_d_defensa:
            dados_defensa[x] = random.randint(1, 6)
    dados_ataque.sort(reverse=True)
    dados_defensa.sort(reverse=True)
    print(dados_ataque)
    print(dados_defensa)


# EJECUCION ######
for simulacion in range(0, simulaciones):
    if jugar(fichas_ataque, fichas_defensa) == "gana ataque":
        vict_ataque += 1
    else:
        vict_defensa += 1
print('Simulaciones totales: ' + str(simulaciones))
print(vict_ataque)
print(vict_defensa)
