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

1. Navegue até o diretório [docker](docker).
    ```bash
    cd docker
    ```

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

### 🛑 Parando o Projeto

1. Navegue até o diretório [docker](docker).
    ```bash
    cd docker
    ```

2. Execute o script de parada:

    ```bash
    ./scripts/stop.sh
    ```

## 🚀 Instruções de Uso com Kubernetes

Este guia irá orientá-lo na configuração de um cluster Kubernetes usando k3d. Certifique-se de ter o Docker instalado no seu sistema antes de prosseguir.

### Configuração do Cluster Kubernetes

Para configurar o cluster Kubernetes, siga estas etapas:

1. Navegue até o diretório [k8s](k8s).
    ```bash
       cd k8s
    ```
2. Execute o script `setup.sh`.
    ```bash
   ./setup.sh
    ```

Este script automaticamente:

🚀 Instala k3d, kubectl, Krew e Helm se ainda não estiverem instalados.

🌟 Cria um cluster k3d chamado "saga" com mapeamento de portas para balanceamento de carga.

Após executar o script, seu cluster Kubernetes estará configurado e pronto para uso.

### Instalando o Kong Ingress Controller

1. **Instale os CRDs do Gateway API antes de instalar o Kong Ingress Controller.**

    ```bash
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml
    ```

2. **Crie uma instância de Gateway e GatewayClass para usar.**

    ```bash
    kubectl apply -f kong/kong-gateway.yaml
    ```

3. **Instalação do Helm Chart**

    1. Adicione os charts do Helm do Kong:
    ```bash
       helm repo add kong https://charts.konghq.com
    ```
    2. Atualize o repositório:
    ```bash
       helm repo update
    ```
    3. Instale o Controlador de Ingress do Kong e o Gateway do Kong com Helm:
    ```bash
       helm install kong kong/ingress -n kong --create-namespace --values kong/values.yaml
    ```

4. **Verificar Instalação**

   Após a instalação, verifique se os pods do Controlador de Ingress do Kong estão em execução:

    ```bash
    curl -i 'localhost:8080'
    ```

   Os resultados devem se parecer com isso:
   ```bash
   HTTP/1.1 404 Not Found
   Date: Sun, 28 Jan 2024 19:14:45 GMT
   Content-Type: application/json; charset=utf-8
   Connection: keep-alive
   Content-Length: 103
   X-Kong-Response-Latency: 0
   Server: kong/3.5.0
   X-Kong-Request-Id: fa55be13bee8575984a67514efbe224c
   
   {
     "message":"no Route matched with those values",
     "request_id":"fa55be13bee8575984a67514efbe224c"
   }   
   ```
   **Observação:**
   > Se encontrar `curl: (52) Empty reply from server`, aguarde um momento e tente novamente.


5. **Crie um Operador de Kubernetes RabbitMQ Cluster.**

    1. Instale o Operador de Cluster RabbitMQ:
        ```bash
        kubectl rabbitmq install-cluster-operator
        ```
    2. Crie um cluster RabbitMQ:
         ```bash
         kubectl apply -f rabbitmq/rabbitmq.yaml
         ```
    3. Crie uma exchange saga:
         ```bash
         kubectl exec svc/rabbitmq  -c rabbitmq -- rabbitmqadmin declare exchange name=saga type=topic -u guest -p guest
         ```
       Os resultados devem ser semelhantes a isto:
         ```bash
         exchange declared
         ```
       **Observação:**
       > O cluster RabbitMQ deve estar em execução
    4. Acesse a Interface de Gerenciamento (opcional):
        ```bash
        kubectl rabbitmq manage rabbitmq
        ```

### Instalando os serviços de pedido, estoque e pagamento usando Helm 📊

Após configurar o cluster Kubernetes e instalar o Controlador de Ingress do Kong:

1. Use o Helm para criar os releases "order", "stock" e "payment" usando o chart Saga e os valores correspondentes:

   ```bash
   helm install order ./saga --values services/order/values.yaml
   helm install stock ./saga --values services/stock/values.yaml
   helm install payment ./saga --values services/payment/values.yaml
   ```

Isso cria três releases do Helm, "order", "stock" e "payment", com as configurações especificadas em seus respectivos arquivos `values.yaml`.

Por favor, note que cada comando cria um release do Helm específico com suas próprias configurações.

### 🛑 Parando o Projeto

1. Execute o comando de exclusão do cluster:

```bash
k3d cluster delete saga
```

## 🧪 Testando Cenários com a Coleção do Postman

1. Instale o [Postman](https://www.postman.com/downloads/).

2. Importe a [coleção](docs/saga.postman_collection.json) do Postman.

3. A coleção contém cenários:
    - **Estoque Não Reservado:** Criar pedido com quantidade > 10.
    - **Pagamento Negado:** Criar pedido com valor > $1000.

4. Execute as solicitações para observar o comportamento do sistema.