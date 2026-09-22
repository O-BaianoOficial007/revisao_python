Nomes= ["Dipirona", "Paracetamol", "Loratadina"]
Precos= [12.50, 9.90, 18.75]
Estoques= [20, 15, 8]

#funcao pesquisa
# variavel com pergunta de qual palavra quer perguntar
# vetor para armazenar
# for indice in range(len(nomes)):
# condição para comparar o valor digitado é igual ao nome armazenado naquele indice
# vetor append nome, vetor append preco, vetor append. estoque
# retorno vetor

def pesquisa(nomes):
    p = input("Digite qual medicamento quer pesquisar:")
    pesq = []
    for indice in range(len(nomes)):
        print("")

while True:
    print("\n","="*10,"MENU","="*10,"\n")
    print("\n1 - Listar medicamentos\n2 - Pesquisar medicamento\n3 - Registrar venda\n4 - Repor estoque\n5 - Mostrar estoque baixo\n6 - Encerrar\n")

    escolha = int(input("Digite a opção que deseja: "))

    if escolha == 1:
        print("\n")
        for i in range(0,3):
            print(f"Medicamento: {Nomes[i]}\nPreços: R$ {Precos[i]}\n")

    elif escolha == 6:
        break

    else:
        print("Valor inválido")
