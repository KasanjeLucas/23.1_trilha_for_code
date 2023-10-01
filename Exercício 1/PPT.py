# Jokenpô
from random import randint
import os

vencidas_jogador01 = 0
vencidas_computador = 0
empates = 0
opcoes_jogada = ['Pedra', 'Papel', 'Tesoura']
rodadas = 0
flag = 1 # Criação de uma flag de saída para análise de vencedor


def valida_opcao(valor: str) -> int or str:
    cleared_value = valor.strip(' []')
    try:
        valor_int = int(cleared_value)
        return valor_int
    
    except ValueError:
        print ('Insira apenas os VALORES especificados no menu (1, 2, 3 ou 4). Por favor, reinicie o programa.')
        return False
    


def analisa_opcao_valida(opcao: int) -> str or bool: # função que avalia o caso escolhido pelo user, isso dps da validação
    if opcao == 1:
        return '0'
    
    if opcao == 2:
        return '1'
    
    if opcao == 3:
        return '2'
    
    if opcao == 4:
        return False

def escolhe_opcao_user(opcao: int, lista_opcoes: list) -> str:
    for i in range(len(lista_opcoes)):
        if opcao == i:
            return lista_opcoes[i]

def escolhe_opcao_computador(lista_opcoes: list) -> str:
    opcao = randint(0, 2)
    for i in range(len(lista_opcoes)):
        if opcao == i:
            return lista_opcoes[i]

def calcula_vencedor_rodada(opcao_user: str, opcao_computador: str) -> str:
    global empates
    global vencidas_jogador01
    global vencidas_computador
    if opcao_user == 'Pedra' and opcao_computador == 'Pedra':
        empates += 1
        return 'Empate'

    elif opcao_user == 'Pedra' and opcao_computador == 'Papel':
        vencidas_computador += 1
        return 'Computador'

    elif opcao_user == 'Pedra' and opcao_computador == 'Tesoura':
        vencidas_jogador01 += 1
        return 'Usuário'

    elif opcao_user == 'Papel' and opcao_computador == 'Pedra':
        vencidas_jogador01 += 1
        return 'Usuário'
    
    elif opcao_user == 'Papel' and opcao_computador == 'Papel':
        empates += 1
        return 'Empate'
    
    elif opcao_user == 'Papel' and opcao_computador == 'Tesoura':
        vencidas_computador += 1
        return 'Computador'
    
    elif opcao_user == 'Tesoura' and opcao_computador == 'Pedra':
        vencidas_computador += 1
        return 'Computador'
    
    elif opcao_user == 'Tesoura' and opcao_computador == 'Papel':
        vencidas_jogador01 += 1
        return 'Usuário'
    
    elif opcao_user == 'Tesoura' and opcao_computador == 'Tesoura':
        empates += 1
        return 'Empate'


while flag and rodadas <= 4:
    answer_user = input('Digite a opção a qual deseja jogar: \n'
                        + '[1] Pedra \n'
                        + '[2] Papel \n'
                        + '[3] Tesoura \n'
                        + '[4] Sair do jogo\n')
    
    validated_answer = valida_opcao(answer_user)

    if validated_answer:
        escolha = analisa_opcao_valida(validated_answer)

        if escolha:
            escolha_int = int(escolha)
            escolha_user = escolhe_opcao_user(escolha_int, opcoes_jogada)
            escolha_computador = escolhe_opcao_computador(opcoes_jogada)

            resultado_rodada = calcula_vencedor_rodada(escolha_user, escolha_computador)
            os.system('cls')
            print(f'Sua escolha foi: {escolha_user}\n'
                  + f'A escolha do computador foi: {escolha_computador}\n'
                  + f'Vencedor da rodada: {resultado_rodada}\n'
                  + '+------------------------------------+\n'
                  + f'| Contagem de vitórias Usuário: {vencidas_jogador01}    |\n'
                  + f'| Contagem de vitórias Computador: {vencidas_computador} |\n'
                  + f'| Contagem de empates: {empates}             |\n'
                  + '+------------------------------------+')

            rodadas += 1

            if rodadas == 3: # Empate deu 3 vezes, jogador/computador ganhou direto
                if empates == 3:
                    print('O resultado da partida foi: Empate!\n')
                    flag = 0
                    break
                elif vencidas_jogador01 == 3:
                    print('O resultado da partida foi: Vitória para Usuário!\n')
                    flag = 0
                    break
                elif vencidas_computador == 3:
                    print('O resultado da partida foi: Vitória para o Computador!\n')
                    flag = 0
                    break
            
            elif rodadas == 4:
                if vencidas_computador == 3:
                    print('O resultado da partida foi: Vitória para o Computador!\n')
                    flag = 0
                    break
                elif vencidas_jogador01 == 3:
                    print('O resultado da partida foi: Vitória para Usuário!\n')
                    flag = 0
                    break
                elif empates == 3:
                    print('O resultado da partida foi: Empate!\n')
                    flag = 0
                    break

            elif rodadas == 5:
                if empates == 1 and vencidas_jogador01 == 2 and vencidas_computador == 2:
                    print('O resultado da partida foi: Empate!\n')
                elif empates == 2 and vencidas_jogador01 == 2 and vencidas_computador == 1:
                    print('O resultado da partida foi: Vitória para Usuário!\n')
                elif empates == 2 and vencidas_computador == 2 and vencidas_jogador01 == 1:
                    print('O resultado da partida foi: Vitória para o Computador!\n')
                elif vencidas_computador == 3:
                    print('O resultado da partida foi: Vitória para o Computador!\n')
                elif vencidas_jogador01 == 3:
                    print('O resultado da partida foi: Vitória para Usuário!\n')

            else:
                continue
        else:
            os.system('cls')
            print('Jogo encerrado com sucesso!')
            flag = 0
            break
            

    else:
        flag = 0
        break        

