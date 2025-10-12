from modelos import Baralho, Jogador
import random

# TO-DO

# Logica do jogo:
# Criar partida com dois jogogadores identificados por nomes
# Atribuir um baralho para cada jogador
# Controlar numero de rodadas e placar
# Melhor de 3 rodadas
# Vencedor da rodada ganha 1 ponto
# Vence partida quem tiver mais pontos

# Logica da rodada:
# Exibir as cartas do jogador (humano)
# Jogador (humano) escolhe para rodada se PAR ou IMPAR
# Exibir as cartas do computador (apenas a quantidade, não as cartas)
# Jogador (humano) joga uma carta numerica. Opcional jogar uma carta efeito
# Computador joga uma carta numerica. Opcional jogar uma carta efeito
# Computador resultado: aplica-se o efeito (se houver) na carta numerica
# Soma-se os valores das cartas numericas
# Verifica se o resultado é PAR ou IMPAR
# Se o resultado for igual a escolha do jogador (humano) ele ganha a rodada
# Se o resultado for diferente da escolha do jogador (humano) o computador ganha a rodada  
# Computar placar, incrementar numero de rodadas
# Próxima rodada, trocam-se o tipo numerico jogado (PAR ou IMPAR) em relação a rodada anterior, segue revesando ate o final da partida
# Se rodadas = 3 ou jogador atingir 2 pontos, encerra-se a partida
# Exbir o vencedor da partida e sua pontuação
count_rodadas = 0
pontos_jogador = 0
pontos_computador = 0

print("Bem vindo ao jogo de Par ou Ímpar!")
jogador = Jogador(input("Digite seu nome: "))
computador = Jogador("Computador")
baralho_jogador = Baralho()
baralho_computador = Baralho()

while count_rodadas < 3 and (pontos_jogador < 2 or pontos_computador < 2):
    vez_de = jogador if count_rodadas % 2 == 0 else computador
