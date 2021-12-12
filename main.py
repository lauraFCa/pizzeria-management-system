from classes import *


if __name__ == "__main__":
    autentico = False
    while not autentico:
        decisao = int(input("Digite 1 para Logar ou 2 para Cadastrar: "))
        query = 'SELECT * FROM cadastros;'
        resultado = Conexao().selectBD(query, 'Erro ao conectar no banco de dados')

        autentico, userMaster = Cadastro().logarCadastrar(decisao, resultado)

        print('Cadastros:\n', resultado)
        print('Autenticado: ', autentico,
              '\nStatus usuario master: ', userMaster)

    opcoes = 'Digite: 0 para Sair\n'\
        '1 para Cadastrar produto\n'\
        '2 para Listar Produtos cadastrados\n'\
        '3 para Listar os Pedidos\n'\
        '4 para Gerar Estatisticas\n'\
        '5 para Cadastrar novo Pedido (garçom)\n> '

    if autentico:
        mensagem("Autenticado!")
        if userMaster:
            decisaoUsuario = 1
            while decisaoUsuario != 0:
                decisaoUsuario = int(input(opcoes))
                if decisaoUsuario == 1:
                    Produto().cadastrarProduto()
                elif decisaoUsuario == 2:
                    Produto().listarProduto()
                    delete = int(
                        input("Digite 1 para excluir um produto\n2 para Sair\n"))
                    if delete == 1:
                        Produto().excluirProduto()
                elif decisaoUsuario == 3:
                    Pedido().listarPedido()
                elif decisaoUsuario == 4:
                    Estatistica().gerarEstatisticas()
                elif decisaoUsuario == 5:
                    Pedido().cadastrarPedidos()
