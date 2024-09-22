import random as rd
soma_dados = rd.randint(1,6) + rd.randint(1,6)
jogo = []
print(soma_dados)
jogo.append(soma_dados)
if (soma_dados == 7 or soma_dados == 11):
    print("Voce venceu!")
elif (soma_dados == 2 or soma_dados == 3 or soma_dados == 12):
    print("Voce perdeu...")
else:
    soma_dados = rd.randint(1,6) + rd.randint(1,6)
    jogo.append(soma_dados)
    while(soma_dados != jogo[0] and soma_dados != 7):
        soma_dados = rd.randint(1,6) + rd.randint(1,6)
        jogo.append(soma_dados)
    if(soma_dados == jogo[0]):
        print("Voce venceu!")
    else:
        print("Voce perdeu...")
print("Resultado do jogo:")
for x in jogo:
    print(x)    
