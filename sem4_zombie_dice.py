'''
IDENTIFICAÇÃO DO ALUNO
NOME: RODRIGO MARCONDES DELA PENA
CURSO: BIG DATA E INTELIGÊNCIA ANALÍTICA
'''
# Pacotes utilizados no programa
import random
import time

# Inicio do programa
print('\nZOMBIE DICE - PROTOTIPO SEMANA 4')
print('Que comecem os jogos!!!\n')

#Validação das informações validas inseridas pelo usuário
while True:
    try:
        # Solicitando o número de jogadores, com validação de valor minímo
        n_players = 0
        while (n_players < 2):
            n_players = int(input('Informe o numero de jogadores -> '))
            if n_players < 2:
                print('\033[1;31mO número mínimo de jogadores é 2!\nInforme um número valido!\033[m\n')
        break
    except ValueError:
        print('\033[1;31mATENÇÃO - Informe um valor com formato valido!\033[m')
           

# Adicionando o nome dos jogadores em um lista
list_players = []
time.sleep(0.2)
for n in range(n_players):
    name_players = input(f'Informe o nome do {n + 1}º Jogador: ').upper().strip()
    list_players.append(name_players)

# Adicionando os dados que seram utilizados
d_green = ['C','P','C','T','P','C'] # Faces dos dados Verdes
d_yellow = ['T','P','C','T','P','C'] # Faces dos dados Amarelos
d_red = ['T','P','T','C','P','T'] # Faces dos dados Vermelhos
list_dices = [d_green, d_green, d_green, d_green, d_green, d_green,
   d_yellow, d_yellow, d_yellow, d_yellow,
   d_red, d_red, d_red]

print('INICIANDO O JOGO - PROTÓTIPO...')
time.sleep(0.66)

current_player = 0 # Jogador da vez [valor de acordo com posição - list_players[29]]
dices_drawn = [] # Dados Sorteados
# Pontuação dos jogadores
brain = 0
shot = 0
move = 0

# Criando o laço de repetição para rolagem e seleção dos dados
while True:
    # Informando o jogar do turno - current_player[46]
    print(f'\nTURNO DO JOGADOR -> {list_players[current_player]}\n')
    print('RETIRANDO OS DADOS DO COPO...')
    time.sleep(0.66)

    # Sorteando os Dados da list_dices[33]
    for i in range(0,3):
        num_drawn = random.randint(0,12) # Escolhendo número aleatório 
        dice_drawn = list_dices[num_drawn] # Dado selecionado de acordo com valor gerado aleatoriamente 

        # Informando ao jogador a cor do dado selecionado
        if dice_drawn == ['C','P','C','T','P','C']:
            color_dice = '\033[1;32mVERDE\033[m'
        elif dice_drawn == ['T','P','C','T','P','C']:
            color_dice = '\033[1;33mAMARELO\033[m'
        elif dice_drawn == ['T','P','T','C','P','T']:
            color_dice = '\033[1;31mVERMELHO\033[m'
        
        print(f'{i + 1}º dado retirado -> {color_dice}')
        time.sleep(0.35)

        dices_drawn.append(dice_drawn) # Adicionando a lista de dados sorteados - dices_drawn[40]
    print('\nARREMESSANDO OS DADOS NA MESA\n')
    time.sleep(0.66)

    # Sorteando as faces dos dados selecionados na lista 
    for dice_drawn in dices_drawn: # Para cada dice_drawn[55] na dices_drawn[40] sera sorteado uma face
        num_face_dice = random.randint(0, 5)

        # Inserindo a pontuação de acordo com o num_face_dice[72] do dice_drawn[55]
        if dice_drawn[num_face_dice] == 'C':
            print('- CÉREBRO - (Você comeu um cérebro)')
            time.sleep(0.35)
            brain += 1
        elif dice_drawn[num_face_dice] == 'T':
            print('- TIRO - (Você levou um tiro)')
            time.sleep(0.35)
            shot += 1
        else:
            print('- PASSO - (A vítima escapou)')
            time.sleep(0.35)
            move += 1
    
    # Informando a pontuação total da rodada atual + rodadas anteriores
    print(f'\n==PONTUAÇÃO DA RODADA==\nCEREBROS: {brain}\nTIROS: {shot}\nPASSO: {move}\n')

    # Jogador informando se vai ou não continuar jogando os dados
    continue_turn = str(input('QUER CONTINUAR JOGANDO OS DADOS? [S/N] ')).strip().upper()[0]
    
    # Passando condições para dar continuidade ao jogo
    # Se não der continuidade, todos os parametros de pontuação e dices_drawn[40] seram resetados e o próximo jogador da list_player realizar sua jogada.
    if continue_turn == 'N':
        current_player += 1
        dices_drawn = []
        brain = 0
        shot = 0
        move = 0
        # Condição para verificar se todos os jogadores jogaram, assim finalizando programa
        if current_player == len(list_players):
            print('\nFinalizando Protótipo - ZOMBIE DICE\n')
            break
    else:
        print('\nComeçando uma nova rodada com o jogador atual... ')
        time.sleep(1)
        dices_drawn = []
        move = 0