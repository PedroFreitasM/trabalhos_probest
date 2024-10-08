import random as rd

#1.a : definição do jogo em si
def jogo_craps():
    soma_dados = rd.randint(1,6) + rd.randint(1,6)
    jogo = []
    print(soma_dados)
    jogo.append(soma_dados)
    if (soma_dados == 7 or soma_dados == 11):
        print("Voce venceu!")
        jogo.append(1)
    elif (soma_dados == 2 or soma_dados == 3 or soma_dados == 12):
        print("Voce perdeu...")
        jogo.append(0)
    else:
        soma_dados = rd.randint(1,6) + rd.randint(1,6)
        jogo.append(soma_dados)
        while(soma_dados != jogo[0] and soma_dados != 7):
            soma_dados = rd.randint(1,6) + rd.randint(1,6)
            jogo.append(soma_dados)
        if(soma_dados == jogo[0]):
            print("Voce venceu!")
            jogo.append(1)
        else:
            print("Voce perdeu...")
            jogo.append(0)
    print("Resultado do jogo:")
    for x in jogo:
        print(x)   
    return jogo

#1.b : teste das 5 partidas
partidas = []
for x in range(5):
    res = jogo_craps()
    partidas.append(res)
print(partidas)

#1.c : probabilidade de vitória
soma = 0
for x in range(1000): #um número alto para garantir...
    jogo = jogo_craps()
    soma+=jogo[-1]
print("Probabilidade de vitoria:")
print((soma/1000))
