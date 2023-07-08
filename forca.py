import os
os.system("cls")

quantidade_letras = 0

forca = """
____
    |
    |
    -"""

vazio = """


"""

cabeca = """
    O
"""
braco_esquerdo = """
    O
   /|
"""
braco_direito = """
    O
   /|\\
"""
perna_esquerda = """
    O
   /|\\
   / 
"""
perna_direita = """
    O
   /|\\
   / \\

Você Perdeu!! :(
"""

chances_do_boneco = [
    vazio,
    cabeca,
    braco_esquerdo,
    braco_direito,
    perna_esquerda,
]

erros = 0
acertos = 0
dicas = 0
letras_acertadas = ""
letras_erradas = ""
conteudo = []

desafiante = input("Desafiante: ")
competidor = input("Competidor: ")

os.system("cls")

palavra = input("Palavra chave: ")
palavra = palavra.upper()

quantidade_letras = len(palavra)

dica1 = input("Dica 1: ")
dica2 = input("Dica 2: ")
dica3 = input("Dica 3: ")

dica = [dica1,dica2,dica3]

os.system("cls")

print("A palavra chave contém", quantidade_letras,
      "letras:", "_ " * quantidade_letras)

while erros != 5 and acertos != len(palavra):
    mensagem = ""

    if dicas != 3:

        print("\n(1) Jogar\n(2) Solicitar Dica\n")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":

            for letra in palavra:
                if letra in letras_acertadas:
                    mensagem += f"{letra} "
                else:
                    mensagem += "_ "
            print(forca+chances_do_boneco[erros])
            print(mensagem)


            letra = input("\nDigite uma letra: ").upper()

            if letra in letras_acertadas+letras_erradas:
                print("\nVocê ja tentou esta letra.")
                continue

            if letra in palavra:
                acertos += palavra.count(letra)
                if acertos == len(palavra):
                    print("\nVocê venceu, a palavra era",palavra)
                else:
                    print("\nVocê acertou a letra.")
                    letras_acertadas += letra
                
            else:
                erros += 1
                if erros == 5:
                    print(perna_direita)
                else:
                    print("\nVocê errou a letra.")
                    letras_erradas += letra
                
        elif escolha == "2":
            if dicas == 3:
                print("\nVocê não tem mais dicas.")
            else:
                print("\nDica:",dica[dicas])
                dicas += 1
        
        else:
            print("\nEscolha uma opção válida.")
    
    elif dicas == 3:
        for letra in palavra:
            if letra in letras_acertadas:
                mensagem += f"{letra} "
            else:
                mensagem += "_ "
        print(forca+chances_do_boneco[erros])
        print(mensagem)


        letra = input("\nDigite uma letra: ").upper()

        if letra in letras_acertadas+letras_erradas:
            print("\nVocê ja tentou esta letra.")
            continue

        if letra in palavra:
            acertos += palavra.count(letra)
            if acertos == len(palavra):
                print("\nVocê venceu, a palavra era",palavra)
            else:
                print("\nVocê acertou a letra.")
                letras_acertadas += letra
            
        else:
            erros += 1
            if erros == 5:
                print(perna_direita)
            else:
                print("\nVocê errou a letra.")
                letras_erradas += letra        
            
try:
    arquivo = open("historico.txt","a")
    conteudo = arquivo.readlines()
    arquivo.close()
except:
    arquivo = open("historico.txt","w")
    arquivo.close()
conteudo.append(competidor+"\n")
conteudo.append(desafiante+"\n")
arquivo = open("historico.txt","w")
arquivo.write(''.join(conteudo))
arquivo.close()
    