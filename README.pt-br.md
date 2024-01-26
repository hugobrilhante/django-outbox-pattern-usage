# 🌐 Saga com Padrão Outbox: Orquestrando Transações Distribuídas em Microsserviços
[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt-br.md)

Este repositório demonstra o Padrão Outbox em microsserviços, aproveitando a biblioteca Django Outbox Pattern desenvolvida em [@juntossomosmais](https://github.com/juntossomosmais/django-outbox-pattern).

### 🎭 Cenário: Sistema de E-Commerce

Um sistema de e-commerce utiliza microsserviços (Pedido, Estoque e Pagamento) para gerenciar pedidos, estoque e pagamentos. O padrão Saga é implementado usando o padrão Outbox para comunicação consistente.

* **📦 Serviço de Pedido:**
    - Recebe e processa pedidos de clientes.
    - Cria registros de pedido no banco de dados após a recepção do pedido.

* **📦 Serviço de Estoque:**
    - Gerencia o estoque de produtos.
    - Recebe uma mensagem de pedido para reservar produtos em estoque.
    - Confirma a reserva, atualiza o banco de dados e registra uma mensagem na tabela Outbox.

* **💳 Serviço de Pagamento:**
    - Processa pagamentos de pedidos.
    - Recebe uma mensagem de pedido para autorização de pagamento.
    - Valida o pagamento, autoriza-o, atualiza o banco de dados e registra uma mensagem na tabela Outbox.

### ⚙️ Fluxo de Execução:

1. O cliente faz um pedido através do serviço de Pedido.
2. O serviço de Pedido cria um registro na tabela Outbox com os detalhes do pedido.
3. A mensagem é enviada para o serviço de Estoque para reservar produtos.
4. O serviço de Estoque confirma a reserva, atualiza seu banco de dados e registra uma mensagem na tabela Outbox.
5. A mensagem é enviada para o serviço de Pagamento para autorização de pagamento.
6. O serviço de Pagamento valida o pagamento, autoriza-o, atualiza seu banco de dados e registra uma mensagem na tabela Outbox.
7. O serviço de Pedido verifica periodicamente a tabela Outbox para processar mensagens pendentes.
8. Se bem-sucedido, o pedido é marcado como confirmado e o cliente é notificado.

![Fluxo](docs/flow.png)

### 🏗️ Infraestrutura

Este repositório fornece arquivos de configuração para implantar três serviços Django (Pedido, Estoque, Pagamento) no Kubernetes e Docker Compose. Cada serviço possui seu banco de dados PostgreSQL, e o RabbitMQ facilita a comunicação. Kong atua como gateway de API e camada de gerenciamento de microsserviços.

![Arquitetura](docs/architecture.png)

### 🛠️ Tecnologias Utilizadas

1. **Django:** Um framework web para desenvolvimento rápido de aplicativos Python.
2. **PostgreSQL:** Um robusto sistema de gerenciamento de banco de dados relacional.
3. **RabbitMQ:** Suporta comunicação assíncrona entre serviços.
4. **Kubernetes:** Orquestração de contêineres para automação de implantação e escalabilidade.
5. **Docker Compose:** Simplifica o gerenciamento de aplicativos Docker com vários contêineres.
6. **Kong:** Um gateway de API e camada de gerenciamento de microsserviços.

## 🚀 Instruções de Uso com Docker

### 🏁 Iniciando o Projeto

1. Navegue até o diretório raiz do projeto.

2. Execute o script de início:

    ```bash
    ./scripts/start.sh
    ```

3. Acesse os serviços via:
   - Administração de Pedido: [http://localhost:8000/admin](http://localhost:8000/admin)
   - Administração de Estoque: [http://localhost:8001/admin](http://localhost:8001/admin)
   - Administração de Pagamento: [http://localhost:8002/admin](http://localhost:8002/admin)
   - API: [http://localhost:8080](http://localhost:8080)
   - Administração do Kong: [http://localhost:8082](http://localhost:8082)
   - Interface de Gerenciamento do RabbitMQ: [http://localhost:15672](http://localhost:15672)

4. Use estas credenciais:
   - Administração do Django: admin/admin
   - RabbitMQ: guest/guest

### 🧪 Testando Cenários com Coleção do Postman

1. Instale o [Postman](https://www.postman.com/downloads/).

2. Importe a [coleção](docs/saga.postman_collection.json) do Postman.

3. A coleção contém cenários:
   - **Estoque Não Reservado:** Criar pedido com quantidade > 10.
   - **Pagamento Negado:** Criar pedido com valor > $1000.

4. Execute as requisições para observar o comportamento do sistema.

### 🛑 Parando o Projeto

1. Navegue até o diretório raiz do projeto.

2. Execute o script de parada:

    ```bash
    ./scripts/stop.sh
    ```

## 🚀 Instruções de Uso com Kubernetes

**Nota:** Instruções de implantação no Kubernetes em breve. Fique atento!