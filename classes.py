from os import system
import pymysql.cursors
from time import sleep
import matplotlib.pyplot as plt


class Conexao:
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost',  # IP
            user='root',
            password='',
            db='pizzaria',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def commitBD(self, query, msgSucesso, msgFalha):
        '''Operacoes de acesso ao BD com commit (INSERT)

        Args:
            query (string): query a ser executada no BD
            msgSucesso (string): Mensagem para indicar sucesso na execucao
            msgFalha (string): Mensagem para indicar falha na execucao
        '''

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                self.conexao.commit()
                mensagem(msgSucesso)
        except Exception as e:
            print(msgFalha, '\n', e)

    def selectBD(self, query, msgFalha):
        '''Obter dados do BD com fetchall (SELECT)

        Args:
            query (string): query a ser executada no BD
            msgFalha (string): Mensagem para indicar falha na execucao

        Returns:
            [dicionario]: resultado - resposta do select
        '''

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            print(msgFalha, '\n', e)


class Cadastro:
    def __init__(self):
        self.__nome, self.__senha, self.__nivel = '', '', 1

    ### GETs e SETs ###
    @property  # GET
    def nome(self):
        return self.__nome

    @nome.setter  # SET
    def nome(self, nome):
        self.__nome = nome

    @property  # GET
    def senha(self):
        return self.__senha

    @senha.setter  # SET
    def senha(self, nome):
        self.__senha = senha

    @property  # GET
    def nivel(self):
        return self.__nivel

    @nivel.setter  # SET
    def nivel(self, nivel):
        self.__nivel = nivel

    ### Metodos ###
    def logarCadastrar(self, decisao, resultado):
        '''Funcao para gerenciar operacao de login e cadastro de novos usuarios

        Returns:
            [bool, bool]: autenticado, usuarioMaster (status da autenticacao e se eh usuario master)
        '''

        usuarioExistente = False
        autenticado = False
        usuarioMaster = False

        # global decisao = xxx --> crio a variavel dentro da funcao mas funciona em todo programa
        if decisao == 1:  # LOGIN (verifica se usuario ja existe)
            self.__nome = input("Digite o nome de usuario: ")
            self.__senha = input("Digite a senha: ")

            for linha in resultado:
                if self.__nome == linha['nome'] and self.__senha == linha['senha']:
                    if linha['nivel'] == 1:
                        usuarioMaster = False
                    elif linha['nivel'] == 2:
                        usuarioMaster = True
                    autenticado = True
                    break  # para de executar assim que encontra nome e senha igual
                else:
                    autenticado = False

            if not autenticado:
                print("Usuario ou senha errados")

        elif decisao == 2:
            print("\nFaca seu cadastro")
            self.__nome = input("Digite um nome de usuario: ")
            self.__senha = input("Digite uma senha: ")

            for linha in resultado:
                if self.__nome == linha['nome'] and self.__senha == linha['senha']:
                    usuarioExistente = True

            if usuarioExistente:
                print(
                    'Usuario e senha ja cadastrados no sistema!\nTente um nome ou senha diferente\n')

            elif usuarioExistente == False:
                query = 'INSERT INTO cadastros(nome, senha, nivel) VALUES ("{}", "{}", {})'.format(
                    self.__nome, self.__senha, 1)
                Conexao().commitBD(query, 'Usuario cadastrado com sucesso!',
                                   'Erro ao inserir os dados no banco!')

        return autenticado, usuarioMaster


class Produto:
    def __init__(self):
        self.__nome, self.__grupo, self.__ingredientes, self.__preco = '', '', '', 0

    ### GETs e SETs ###
    @property  # GET
    def nome(self):
        return self.__nome

    @nome.setter  # SET
    def nome(self, nome):
        self.__nome = nome

    @property
    def grupo(self):
        return self.__grupo

    @grupo.setter
    def grupo(self, grupo):
        self.__grupo = grupo

    @property
    def ingredientes(self):
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self, ingredientes):
        self.__ingredientes = ingredientes

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    ### Metodos ###
    def cadastrarProduto(self):
        '''Usuario adm pode cadastrar produtos no sistema
        '''

        self.__nome = input("Digite o nome do produto: ")
        self.__ingredientes = input("Digite os ingredientes do produto: ")
        self.__grupo = input("Digite o grupo pertencente ao produto: ")
        self.__preco = float(input("Digite o preco do produto: "))

        query = 'INSERT INTO produtos(nome, ingredientes, grupo, preco) VALUES ("{}", "{}", "{}", {});'.format(
            self.__nome, self.__ingredientes, self.__grupo, self.__preco)
        Conexao().commitBD(query, "Produto cadastrado com sucesso!",
                           "Erro ao inserir produto no banco")

    def listarProduto(self):
        '''Funcao para usuario visualizar produtos ja cadastrados no sistema
        '''

        produtos = []
        query = 'SELECT * FROM produtos'
        produtosCadastrados = Conexao().selectBD(
            query, 'Erro ao conectar com banco de dados')

        for i in produtosCadastrados:
            produtos.append(i)
        if len(produtos) != 0:
            for i in range(0, len(produtos)):
                print("Produto {}\n".format(round(i, 2)), produtos[i], "\n")
        else:
            print("Nenhum produto cadastrado!")

    def excluirProduto(self):
        '''Permite ao usuario excluir um dos produtos ja cadastrados
        '''

        idDeletar = int(input("Digite o ID do produto que deseja apagar: "))
        query = 'DELETE FROM produtos WHERE id = {}'.format(idDeletar)
        Conexao().commitBD(query, "Produto apagado com sucesso!",
                           "Erro ao apagar o produto")


class Pedido:
    def __init__(self):
        self.__nome, self.__grupo, self.__ingredientes, self.__localEntrega, self.__observacoes = '', '', '', '', ''

    ### GETs e SETs ###
    @property  # GET
    def nome(self):
        return self.__nome

    @nome.setter  # SET
    def nome(self, nome):
        self.__nome = nome

    @property
    def grupo(self):
        return self.__grupo

    @grupo.setter
    def grupo(self, grupo):
        self.__grupo = grupo

    @property
    def ingredientes(self):
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self, ingredientes):
        self.__ingredientes = ingredientes

    @property
    def localEntrega(self):
        return self.__localEntrega

    @localEntrega.setter
    def localEntrega(self, localEntrega):
        self.__localEntrega = localEntrega

    @property
    def observacoes(self):
        return self.__observacoes

    @observacoes.setter
    def observacoes(self, observacoes):
        self.__observacoes = observacoes

    ### Metodos ###
    def excluirPedido(self):
        '''Permite ao usuario dar como entregue um dos pedidos feitos.
        Move pedido para estatistica de vendas
        '''

        grupo, indice = None, 0
        idDeletar = int(input("Digite o ID do pedido que deseja Entregar: "))

        query = 'SELECT nome FROM pedidos WHERE id = {};'.format(idDeletar)
        nome = Conexao().selectBD(query, "Nao foi possivel obter o nome do pedido!")
        nome = nome[0]['nome']

        queryProdutos = 'SELECT * FROM produtos;'
        produtos = Conexao().selectBD(
            queryProdutos, "Nao foi possivel obter os produtos!")

        for p in produtos:
            indice += 1
            if nome == p['nome']:
                grupo = p['grupo']
                preco = p['preco']
                break

        if grupo != None:
            queryEstatisticas = 'INSERT INTO estatisticavendido(nome, grupo, preco) VALUES ("{}", "{}", {});'.format(
                nome, grupo, preco)
            Conexao().commitBD(queryEstatisticas, "O pedido esta contabilizado!",
                               "Nao foi possivel contabilizar o pedido")

            queryDelete = 'DELETE FROM pedidos WHERE id = {};'.format(
                idDeletar)
            Conexao().commitBD(queryDelete, "Pedido entregue com sucesso!",
                               "Erro ao acessar o banco")
        else:
            print("Nao foi possivel dar o pedido como entregue.\nProduto nao encontrado.")

    def listarPedido(self):
        '''Permite usuario acessar lista com pedidos feitos \nPemite tambem excluir pedidos entregues
        '''
        pedidos = []
        decisaoPedido = 0

        while decisaoPedido != 2:
            pedidos.clear()  # sempre limpa variavel para na acumular (quando pedido eh entregue ele eh apagado)
            query = 'SELECT * FROM pedidos'
            listaPedidos = Conexao().selectBD(query, "Falha ao conectar ao banco")

            for i in listaPedidos:
                pedidos.append(i)

            if len(pedidos) != 0:
                for i in range(0, len(pedidos)):
                    print(pedidos[i])

            else:
                print("Nao ha pedidos feitos")

            decisaoPedido = int(
                input("Digite 1 para dar pedido como Entregue\n2 para Voltar\n"))
            if decisaoPedido == 1:
                self.excluirPedido()

    # FUNCAO NO CELULAR DOS GARCONS (aqui apenas para fins didaticos)
    def cadastrarPedidos(self):
        '''Garcons cadastram pedidos feitos no sistema
        '''
        grupo = None
        indice = 0
        nome = input("Digite o nome do pedido: ")

        query = 'SELECT * FROM produtos'
        produtos = Conexao().selectBD(
            query, "Nao foi possivel obter os produtos cadastrados!")

        for p in produtos:
            indice += 1
            if nome == p['nome']:
                ingredientes = p['ingredientes']
                grupo = p['grupo']
                preco = p['preco']
                break
            elif indice == len(produtos):
                print(
                    "Nao ha produto cadastrado!\nCadastre primeiro o produto para depois fazer o pedido.")

        if grupo != None:
            localEntrega = input(
                "Digite a mesa ou local de entrega do pedido: ")
            observacoes = input("Digite as observacoes do pedido: ")

        query1 = 'INSERT INTO pedidos(nome, ingredientes, grupo, localEntrega, observacoes) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(
            nome, ingredientes, grupo, localEntrega, observacoes)
        Conexao().commitBD(query1, "Pedido cadastrado com sucesso!", "Erro ao realizar pedido!")


class Estatistica:
    def __init__(self):
        self.__nome, self.__grupo, self.__preco = '', '', 0
        x = Conexao().selectBD('SELECT * FROM estatisticavendido',
                               "Nao foi possivel obter os dados para os calculos")
        print('x= ', x)
        for i in x:
            print(i)

    ### GETs e SETs ###
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def grupo(self):
        return self.__grupo

    @grupo.setter
    def grupo(self, grupo):
        self.__grupo = grupo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    ### Metodos ###
    def gerarEstatisticas(self):
        '''Permite gerar graficos com relacao a quantidade e/ou valor dos produtos vendidos
        '''
        chaveProdutos = []
        chaveProdutos.clear()  # reseta toda vez que a funcao eh executada

        # Pegar dados de produto
        querySelecionar = 'SELECT * FROM produtos'
        listaProdutos = Conexao().selectBD(
            querySelecionar, "Nao foi possivel acessar os produtos do sistema")
        # Pegar dados da estatistica
        queryEstatistica = 'SELECT * FROM estatisticaVendido'
        listaVendido = Conexao().selectBD(
            queryEstatistica, "Erro ao fazer a consulta das estatisticas de vendas")

        estado = (input(
            "Digite 0 para Sair\n1 para Analisar por Nome\n2 para Analisar por Grupo\n> "))
        if estado == "1":
            decisao = int(input(
                "Digite 1 para analisar por Dinheiro\n2 para analisar por Quantidade unitaria\n> "))
            if decisao == 1:
                for i in listaProdutos:
                    chaveProdutos.append(i['nome'])

                valores = []
                valores.clear()
                for h in range(0, len(chaveProdutos)):
                    somaValor = -1
                    for i in listaVendido:  # para cada nome faz varredura da lista completa
                        if i['nome'] == chaveProdutos[h]:
                            somaValor += i['preco']  # pesquisa por dinheiro
                    if somaValor == -1:
                        valores.append(0)
                    elif somaValor > 0:
                        valores.append(somaValor+1)
                print(valores)
                plt.plot(chaveProdutos, valores)  # eixoX, eixoY
                plt.ylabel('Quantidade vendida em reais')
                plt.xlabel('Produtos')
                plt.show()
            elif decisao == 2:
                grupoUnico = []
                grupoUnico.clear()

                for i in listaProdutos:
                    grupoUnico.append(i['nome'])

                # elimina duplicados e ordena lista
                grupoUnico = sorted(set(grupoUnico))

                qntFinal = []
                qntFinal.clear()

                for h in range(0, len(grupoUnico)):
                    qntUnitaria = 0
                    for i in listaVendido:
                        if grupoUnico[h] == i['nome']:
                            qntUnitaria += 1
                    qntFinal.append(qntUnitaria)

                plt.plot(grupoUnico, qntFinal)
                plt.ylabel("Quantidade unitaria vendida")
                plt.xlabel("Produtos")
                plt.show()

        elif estado == "2":
            decisao = int(input(
                "Digite 1 para analisar por Dinheiro\n2 para analisar por Quantidade unitaria\n> "))
            if decisao == 1:
                for i in listaProdutos:
                    chaveProdutos.append(i['grupo'])

                valores = []
                valores.clear()
                for h in range(0, len(chaveProdutos)):
                    somaValor = -1
                    for i in listaVendido:  # para cada nome faz varredura da lista completa
                        if i['grupo'] == chaveProdutos[h]:
                            somaValor += i['preco']  # pesquisa por dinheiro
                    if somaValor == -1:
                        valores.append(0)
                    elif somaValor > 0:
                        valores.append(somaValor+1)
                print(valores)
                plt.plot(chaveProdutos, valores)  # eixoX, eixoY
                plt.ylabel('Quantidade vendida em reais')
                plt.xlabel('Produtos')
                plt.show()
            elif decisao == 2:
                grupoUnico = []
                grupoUnico.clear()
                for i in listaProdutos:
                    grupoUnico.append(i['grupo'])

                # elimina duplicados e ordena lista
                grupoUnico = sorted(set(grupoUnico))

                qntFinal = []
                qntFinal.clear()

                for h in range(0, len(grupoUnico)):
                    qntUnitaria = 0
                    for i in listaVendido:
                        if grupoUnico[h] == i['grupo']:
                            qntUnitaria += 1
                    qntFinal.append(qntUnitaria)

                plt.plot(grupoUnico, qntFinal)
                plt.ylabel("Quantidade unitaria vendida")
                plt.xlabel("Produtos")
                plt.show()


def mensagem(msg):
    system("cls")
    print(msg)
    sleep(3)
    system("cls")
