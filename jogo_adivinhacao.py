# Importa a biblioteca nativa 'random', usada para gerar números aleatórios
import random

def jogar_adivinhacao():
    # Solicita ao usuário que escolha a dificuldade e converte a resposta para um número inteiro (int)
    nivel = int(input("Escolha o nível de dificuldade (1- Fácil, 2- Médio, 3- Difícil): "))
   
    # Define o número máximo com base no nível usando uma estrutura condicional em linha (operador ternário)
    # Nível 1 = até 10 | Nível 2 = até 50 | Qualquer outro (Nível 3) = até 100
    max_numero = 10 if nivel == 1 else 50 if nivel == 2 else 100
   
    # Gera um número inteiro aleatório entre 1 e o valor máximo definido acima
    numero_secreto = random.randint(1, max_numero)
   
    # Define a quantidade de chances (tentativas) que o jogador terá dependendo do nível
    # Nível 1 = 10 chances | Nível 2 = 5 chances | Qualquer outro (Nível 3) = 3 chances
    tentativas = 10 if nivel == 1 else 5 if nivel == 2 else 3
   
    # Pontuação inicial do jogador
    pontos = 1000

    # Mensagens de boas-vindas e instruções na tela
    print(f"Jogo de Adivinhação - Nível {nivel}")
    print(f"Tente adivinhar o número que estou pensando, entre 1 e {max_numero}.")

    # Inicia um loop (laço de repetição) que vai de 1 até o limite máximo de tentativas
    for tentativa in range(1, tentativas + 1):
        # Exibe o status atual das tentativas (Ex: Tentativa 1 de 5)
        print(f"Tentativa {tentativa} de {tentativas}")
       
        # Recebe o palpite do jogador e o converte para número inteiro
        palpite = int(input("Digite seu palpite: "))

        # Validação: se o palpite estiver fora do intervalo permitido, avisa o jogador
        if palpite < 1 or palpite > max_numero:
            print(f"Digite um número entre 1 e {max_numero}.")
            continue # Pula o restante deste loop e vai direto para a próxima tentativa

        # Variáveis booleanas (True/False) que guardam o resultado das checagens
        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto

        # Se o palpite for igual ao número secreto
        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break # Interrompe o loop imediatamente, finalizando as tentativas
       
        # Se errou, calcula a penalidade e dá uma dica
        else:
            # Calcula a diferença absoluta (sem sinal negativo) entre o número e o palpite
            pontos_perdidos = abs(numero_secreto - palpite)
            # Subtrai esses pontos do total do jogador
            pontos -= pontos_perdidos
           
            # Fornece a dica se o palpite foi alto ou baixo
            if maior:
                print("Seu palpite foi maior do que o número secreto.")
            elif menor:
                print("Seu palpite foi menor do que o número secreto.")

    # Após sair do loop, verifica se o jogador perdeu (se a última tentativa não foi um acerto)
    if not acertou:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
   
    # Mensagem final padrão executada ao término do jogo
    print("Fim do jogo!")

# Garante que o jogo só rode se este arquivo for executado diretamente (e não importado por outro script)
if __name__ == "__main__":
    jogar_adivinhacao() # Note que adicionei a chamada da função aqui para o código funcionar ao rodar