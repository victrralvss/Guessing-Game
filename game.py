

import random


NUM_DIGITOS = 3
MAX_TENTATIVAS = 10

game = " PICO FERMI BAGELS "
rules = f"""
    {game.center(60,"=")}
    Estou penasndo em número... Consegue adivinhar qual?
    Fique atento!

    Quando eu falar:    Significa:
    PICO                Um dígito está correto mas na posição errada!
    FERMI               Um dígito está correto mas na posição certa!
    BAGELS              Nenhum dígito está correto!
    {"".center(60,"=")}
    """

def main():
    print(rules)

    while True:
        numero_secreto = get_numero_secreto()
        print(f"""  {"".center(60, "=")}""")
        print("Pensei em número... HAHAHA")
        print(f"Consegue adivinhar?\nVocê tem {MAX_TENTATIVAS} chances")

        numero_tentativas = 1
        while numero_tentativas <= MAX_TENTATIVAS:
            tentativa = ""
            while len(tentativa) != NUM_DIGITOS or not tentativa.isdecimal():
                print(f"{numero_tentativas}° TENTATIVA", end = ": ")
                tentativa = input("Que número estou pensando? ")

            dicas = get_dicas(tentativa, numero_secreto)
            print(dicas)
            numero_tentativas += 1

            if tentativa == numero_secreto:
                break
            if numero_tentativas > MAX_TENTATIVAS:
                print("Parece que suas tentaivas acabaram! HAHAHAHA EU GANHEI!")
                print(f"O número secreto era {numero_secreto}!")
    
        print("Deseja jogar novamente?\n[S] SIM ou [N] NÃO")
        if not input(' > ').lower().startswith("s"):
            break
    print("Obrigado por jogar!")




def get_dicas(tentativa, numero_secreto):
    if tentativa == numero_secreto:
        return "Você conseguiu!"

    dicas = []
    
    for digito in range(len(tentativa)):
        if tentativa[digito] == numero_secreto[digito]:
            dicas.append("FERMI")
        elif tentativa[digito] in numero_secreto:
            dicas.append("PICO")
    if len(dicas) == 0:
        return "BAGELS"
    else:
        dicas.sort()
        return ' '.join(dicas)




def get_numero_secreto():
    numeros = list('0123456789')
    random.shuffle(numeros)

    numero_secreto = ""
    for digitos in range(NUM_DIGITOS):
        numero_secreto +=(numeros[digitos])
    return numero_secreto

main()