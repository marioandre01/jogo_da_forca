# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro) , lista com as imagens que o jogo possui
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.palavra = word
        self.numAcertos = 0
        self.numErros = 0
        self.terminou = False
        self.letrasCertas = []
        self.letrasErradas = []
        self.hide_word()

    # Método para adivinhar a letra
    def guess(self, letter):
        self.temLetra = self.palavra.count(letter) # Conta quantas letras tem a palavra, pela letra fornecida, se nao tivre a letra vai retornar zero

        if self.temLetra == 0:  # Se nao tiver a letra
            self.letrasErradas.append(letter)  # Adiciona a letra na lista de letras erradas
            self.numErros += 1  #Incrementa o numero de letras erradas
        else: # Se tiver a letra
            self.letrasCertas.append(letter)  # Adiciona a letra na lista de letras certas
            self.numAcertos += self.temLetra # Soma o numero de letras verificada da palavra na string numAcertos

            count = 0
            for c in self.palavra:
                if letter == c:
                    self.palavraEscondida[count*2] = c  # substitui o _ pela letra descoberta da palavra

                count += 1

        self.letrasOcultas = ""
        for i in self.palavraEscondida:
            self.letrasOcultas += i  # Sobreescreve a string com os _, agora com a letras encontradas


    # Método para verificar se o jogo terminou
    def hangman_over(self):  #Se o jogador venceu ou errou 6 vezes, o jogo termina
        return self.hangman_won() or self.numErros == 6

    # Método para verificar se o jogador venceu
    def hangman_won(self):  # Se o numero de letras acertadas for igual ao numero de letras da palavra, o jogador venceu
        return self.numLetras == self.numAcertos

    # Método para não mostrar a letra no board
    def hide_word(self):

        self.numLetras = len(self.palavra)  #Conta o numero de letras da palavra
        self.palavraEscondida = []  # cria uma lista vazia

        for i in range(0,self.numLetras*2):  # Para i na faixa de 0 ao dobro do numero de letras da palavra faz
            if i % 2:  # se for par faz
                self.palavraEscondida.append(" ") # adiciona espaço na lista
            else:  # se for impar
                self.palavraEscondida.append("_")  # adiciona _ na lista

        self.letrasOcultas = ""
        for j in self.palavraEscondida: # pega o conteudo da lista e coloca na string
            self.letrasOcultas += j


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.numErros])
        print("Palavra: " + self.letrasOcultas)
        print("")

        print("Letras erradas:")
        for c in self.letrasErradas:
            print(c)

        print("")

        print("Letras certas:")
        for i in self.letrasCertas:
            print(i)

        print("")


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f: #Abre o arquivo "palavras.txt" em modo leitura de texto. r-> modo leitura t->modo texto
        bank = f.readlines() # readlines() -> retorna uma lista contendo as linhas do arquivo palavras.txt
    return bank[random.randint(0, len(bank)-1)].strip()  # metodo random sorteia um numero de 0 ao numero de palavras da lista -1, e esse valor define a palavra a ser selecionada na lista
    # strip() -> remove espaços no inicio e no final da string

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    naoAcabou = True

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while (naoAcabou):
        # Verifica o status do jogo
        game.print_game_status()

        if not game.hangman_over(): # Se o jogo não terminou faz
            letra = input("Digite uma letra: ") #Pese-se pra digitar uma letra
            game.guess(letra)  # Chama o método para adivinhar a letra
        else:
            naoAcabou = False

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won(): # Se o jogador venceu a partida faz
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa (O programa começa aqui)
if __name__ == "__main__":
    main()
