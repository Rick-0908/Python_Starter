import Nomes

print("Olá, Bem-Vindo ao cadastramento de nomes de alunos")

while True:  # Loop infinito para cadastrar nomes até o usuário decidir sair
    nome = input(
        "Digite o nome do aluno ou 'sair' para encerrar: ").lower().strip()

    if nome == "sair":
        print("Encerrando o cadastramento de nomes.")
        break

    if nome == "":
        print("Nome inválido. Tente novamente.")
        continue

    data = input("Digite a data de cadastro do aluno (DD/MM/AAAA): ").strip()

    if data.lower() == "sair":
        print("Encerrando o cadastramento.")
        break

    if data == "":
        print("Data inválida. Tente novamente.")
        continue

    # Armazenando o retorno da função na variavel MENSAGEM
    mensagem = Nomes.armazemNomes.adicionar_nome(nome)
    print(mensagem)  # Mostrando a mensagem retornada pela função
    # Armazenando o retorno da função na variavel MENSAGEM_DATA
    mensagem_data = Nomes.armazemNomes.adicionar_data(data)
    print(mensagem_data)  # Mostrando a mensagem retornada pela função
    print("-" * 30)  # Separador visual para melhor leitura

# Pegando a lista de nomes cadastrados
alunos = Nomes.armazemNomes.listar_nomes_alunos()
# Pegando a lista de datas cadastradas
datas = Nomes.armazemNomes.listar_datas_cadastro()

print("\n--- Lista Completa de Alunos Cadastrados ---")
# Usando o ENUMERATE para numerar a lista e o ZIP para juntar as duas listas
for indice, (nome_aluno, data_cadastro) in enumerate(zip(alunos, datas), 1):
    # Mostrando o nome com a primeira letra maiúscula e a data de cadastro
    print(f"{indice}. {nome_aluno.title()} - Cadastrado em: {data_cadastro}")

# Fim do programa
# Utilizamentos de funções novas,listas ao objeto
# ZIP é utilizado para juntar duas listas em uma somente, utilizando tuplas para cada par de elementos das listas originais
# ENUMERATE é utilizando para numerar os elementos de uma lista, retornando o índice e o valor do elemento em cada iteração
# O tittle é utilizado para colocar a primeira letra de cada palavra em maiúscilas
# Lower utilizado para colocar todas as letras em minúsculas
# Strip utilizado para remover os espaços em branco no início e no final da string
# None utilizado para caso a data seja inválida, retornando nada ou erro mesma coisa com o nome
# O continue é usado para pular para a próxima iteração do loop, útil para quando o usuário digita um valor inválido
# O break é usado para sair do loop quando o usuário digita "sair"
