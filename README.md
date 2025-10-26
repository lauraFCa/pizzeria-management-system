# Sistema de Gerenciamento de Pizzaria 🍕

## Descrição

O **Sistema de Gerenciamento de Pizzaria** é uma aplicação desktop desenvolvida em Python que permite gerenciar operações de um restaurante de pizzas. O sistema oferece funcionalidades para controle de produtos, pedidos, usuários e estatísticas de vendas.

Originada do Curso: [Python do básico ao avançado + inteligência artificial](https://www.udemy.com/course/python-do-basico-ao-avancado-inteligencia-artificial/)


## Funcionalidades Principais

### 👤 Autenticação e Registro
- Login de usuários existentes
- Registro de novos usuários
- Dois níveis de acesso:
  - **Nível 1**: Garçom (pode registrar pedidos)
  - **Nível 2**: Administrador (acesso completo)

### 📦 Gerenciamento de Produtos
- **Registrar Produtos**: Administradores podem adicionar novos produtos com nome, ingredientes, categoria e preço
- **Listar Produtos**: Visualizar todos os produtos cadastrados
- **Deletar Produtos**: Remover produtos do sistema

### 📋 Gerenciamento de Pedidos
- **Registrar Pedidos**: Garçons podem criar novos pedidos selecionando produtos já registrados
- **Listar Pedidos**: Visualizar todos os pedidos pendentes
- **Marcar como Entregue**: Confirmar entrega de pedidos e movê-los para estatísticas de vendas

### 📊 Estatísticas de Vendas
- Análise de vendas por nome do produto ou categoria
- Visualização de dados por:
  - Valor monetário total vendido
  - Quantidade de itens vendidos
- Gráficos interativos usando Matplotlib

## Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: Interface gráfica
- **PyMySQL**: Conexão com banco de dados MySQL
- **Matplotlib**: Geração de gráficos de estatísticas

Intalação
- ``pip install PyMySQL``
- ``pip install matplotlib``

## Estrutura do Banco de Dados

### Tabelas Principais

**users**
- Armazena informações de usuários (nome, senha, nível de acesso)

**products**
- Catalogo de produtos (nome, ingredientes, categoria, preço)

**orders**
- Pedidos em andamento (nome, ingredientes, categoria, endereço de entrega, observações)

**soldStatistics**
- Histórico de vendas para gerar estatísticas

## Como Usar

### 1. Configuração Inicial
- Certifique-se de que o MySQL está instalado e rodando
- Execute o arquivo [restaurant.sql](restaurant.sql) para criar o banco de dados
- Atualize as credenciais de conexão em [connection.py](connection.py) se necessário

### 2. Executar a Aplicação
```bash
python main.py
```

### 3. Fluxo de Uso

**Para Administradores:**
1. Faça login com usuário "admin" e senha "admin"
2. Acesse o menu principal com todas as opções
3. Gerencie produtos, visualize pedidos e crie relatórios

**Para Garçons:**
1. Faça login ou registre-se como novo usuário
2. Registre novos pedidos selecionando produtos disponíveis
3. Visualize pedidos em andamento

## Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| [main.py](main.py) | Arquivo principal da aplicação |
| [connection.py](connection.py) | Gerenciamento de conexão com banco de dados |
| [register.py](register.py) | Autenticação e registro de usuários |
| [product.py](product.py) | Operações com produtos |
| [order.py](order.py) | Gerenciamento de pedidos |
| [stats.py](stats.py) | Geração de estatísticas e gráficos |
| [restaurant.sql](restaurant.sql) | Script SQL para criar o banco de dados |

## Estrutura de Classes

- **[Connection](connection.py)**: Gerencia conexões com o banco de dados
- **[Register](register.py)**: Controla login e registro de usuários
- **[Product](product.py)**: Operações CRUD de produtos
- **[Order](order.py)**: Operações CRUD de pedidos
- **[Stats](stats.py)**: Análise e visualização de estatísticas

## Notas

- A aplicação usa validação básica - considere melhorias de segurança para produção
- Implemente tratamento de exceções mais robusto
- Considere adicionar mais funcionalidades como autenticação com hash de senha

## Licença

Este projeto é fornecido como está para fins educacionais.