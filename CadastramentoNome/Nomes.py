class ArmazemNomes:
    def __init__(self):  # Inicializa as listas de nomes e datas
        self.lista_nomes = []
        self.lista_data = []

    # Adicionar os nomes do usuario a lista  declaarada no init
    def adicionar_nome(self, nomeAluno):
        if not nomeAluno or nomeAluno.strip() == "":  # Usando not para caso NÂO tenha nada ou so espaços
            return "Nome inválido. Tente novamente."

        # Adicionado o nome a lista se tiver dentro dos padrões
        self.lista_nomes.append(nomeAluno)
        return f"Nome '{nomeAluno}' adicionado!"

    def listar_nomes_alunos(self):  # Returando a lista de nomes
        return self.lista_nomes

    def formatar_data(self, data_str):  # Formatando a data para o formato DD/MM/AAAA
        # Removendo os espaços e os separadores para facilitar a validação
        data_limpa = data_str.strip().replace("/", "").replace("-", "")
        # Usando o LEN para pegar o TAMANHO da data e verificar se é válida, e logo após o ISDIGIT para garantir que tenha os números
        if len(data_limpa) != 8 or not data_limpa.isdigit():
            return None  # Caso não tenha retorna NONE no caso NADA ! ou erro
        # Formatando a data no padrão DD/MM/AAAA
        data_formatada = f"{data_limpa[:2]}/{data_limpa[2:4]}/{data_limpa[4:]}"
        # No 1 parametro a da data_limpa, a cada 2 caractere colocar / e no segundo também a cada 2 caractere colocar / e no terceiro Pega o resto dos caracteres
        return data_formatada  # AQui retorna a data formatada corretamente

    def adicionar_data(self, dataCadastro):  # Adicionando a data a lista
        if not dataCadastro or dataCadastro.strip() == "":  # Verificando se a data é inválida
            return "Data inválida. Tente novamente."  # Caso esteja vazia ou só com espaços

        # Chamando a função formatar_data para formatar a data
        data_formatada = self.formatar_data(dataCadastro)
        if data_formatada is None:  # Se a data formatada for NONE, ou seja inválida
            # Retorna a mensagem de erro
            return "Data inválida. Use o formato DD/MM/AAAA ou DD-MM-AAAA."

        # Adiciona a data formatada a lista
        self.lista_data.append(data_formatada)
        # Retorna a mensagem de sucesso
        return f"Data '{data_formatada}' adicionada!"

    def listar_datas_cadastro(self):  # Retorna a lista de datas cadastradas
        return self.lista_data  # Retornando a lista de datas cadastradas


# Criando uma instância da classe ArmazemNomes para ser usada em outros módulos
armazemNomes = ArmazemNomes()
