import os 
from time import sleep
os.system("clear||cls")

while True:

    print("DIGITE A SUA IDADE PARA UM MELHOR CONTROLE DO SITE!")
    print()

    n1 = int(input("digite sua idade: "))

    if n1 > 18:
        print("acesso permitido")
        sleep(1)
        os.system("clear||cls")
        break
    if n1 < 18:
        print("acesso negado")
        sleep(0.5)
        os.system("clear||cls")
       
while True:

    print("""
          
1- adiciopnar pessoas
2- Verificar pessoas
3- retirar pessoas             

""")
    
    n2 = int(input("digite uma das opçoes acima: "))
 
    if n2 == 1: 
        pessoa = str(input("Digite o nome da pessoa que deseja adicionar: "))
        idade = int(input("Digite a idade da pessoa: "))
        cpf = input("Digite o CPF da pessoa: ")
        acompanhante  = str(input("essa pessoa possui algum acompanhante?\nDigite : "))

    if acompanhante == :
        pessoa = str(input("Digite o nome da pessoa que deseja adicionar: "))
        idade = int(input("Digite a idade da pessoa: "))
        cpf = input("Digite o CPF da pessoa: ")     