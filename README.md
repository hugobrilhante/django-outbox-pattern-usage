# 🌐 Saga with Outbox Pattern: Orchestrating Distributed Transactions in Microservices

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt-br.md)

This repository demonstrates the Outbox Pattern in microservices, leveraging the Django Outbox Pattern library developed
at [@juntossomosmais](https://github.com/juntossomosmais/django-outbox-pattern).

### 🎭 Scenario: E-Commerce System

An e-commerce system uses microservices (Order, Stock, and Payment) to manage orders, stock, and payments. The Saga
pattern is implemented using the Outbox pattern for consistent communication.

* **📦 Order Service:**
    - Receives and processes customer orders.
    - Creates order records in the database upon order reception.

* **📦 Stock Service:**
    - Manages product stock.
    - Receives an order message to reserve products in stock.
    - Confirms reservation, updates the database, and records a message in the Outbox table.

* **💳 Payment Service:**
    - Processes order payments.
    - Receives an order message for payment authorization.
    - Validates payment, authorizes it, updates the database, and records a message in the Outbox table.

### ⚙️ Execution Flow:

1. Customer places an order through the Order service.
2. Order service creates a record in the Outbox table with order details.
3. Message is sent to the Stock service to reserve products.
4. Stock service confirms reservation, updates its database, and records a message in the Outbox table.
5. Message is sent to the Payment service for payment authorization.
6. Payment service validates payment, authorizes it, updates its database, and records a message in the Outbox table.
7. Order service periodically checks the Outbox table to process pending messages.
8. If successful, the order is marked as confirmed, and the customer is notified.

![Flow](docs/flow.png)

### 🏗️ Infrastructure

This repository provides configuration files for deploying three Django services (Order, Stock, Payment) on Kubernetes
and Docker Compose. Each service has its PostgreSQL database, and RabbitMQ facilitates communication. Kong serves as an
API gateway and microservices management layer.

![Architecture](docs/architecture.png)

### 🛠️ Technologies Used

1. **Django:** A web framework for rapid Python application development.
2. **PostgreSQL:** A robust relational database management system.
3. **RabbitMQ:** Supports asynchronous communication between services.
4. **Kubernetes:** Container orchestration for automating deployment and scaling.
5. **Docker Compose:** Simplifies managing multi-container Docker applications.
6. **Kong:** An API gateway and microservices management layer.

## 🚀 Usage Instructions with Docker

### 🏁 Starting the Project

1. Navigate to the [docker](docker) directory.
    ```bash
       cd docker
    ```

2. Run the start script:

    ```bash
    ./scripts/start.sh
    ```

3. Access services via:
    - Order Admin: [http://localhost:8000/admin](http://localhost:8000/admin)
    - Stock Admin: [http://localhost:8001/admin](http://localhost:8001/admin)
    - Payment Admin: [http://localhost:8002/admin](http://localhost:8002/admin)
    - API: [http://localhost:8080](http://localhost:8080)
    - Kong Admin: [http://localhost:8082](http://localhost:8082)
    - RabbitMQ Management UI: [http://localhost:15672](http://localhost:15672)

4. Use these credentials:
    - Django Admin: admin/admin
    - RabbitMQ: guest/guest

### 🛑 Stopping the Project

1. Navigate to project root.

2. Run stop script:

    ```bash
    ./scripts/stop.sh
    ```

## 🚀 Usage Instructions with Kubernetes

This guide will walk you through setting up a Kubernetes cluster using k3d. Make sure you have Docker installed on your
system before proceeding.

### Kubernetes Cluster Setup

To set up the Kubernetes cluster, follow these steps:

1. Navigate to the [k8s](k8s) directory.
    ```bash
       cd k8s
    ```
2. Run the `setup.sh` script.
    ```bash
   ./setup.sh
    ```

This script will automatically:

🚀 Install k3d, kubectl, and Helm if not already installed.

🌟 Create a k3d cluster named "saga" with port mapping for load balancing.

After running the script, your Kubernetes cluster will be set up and ready to use.

### Install the Kong Ingress Controller

1. **Install the Gateway API CRDs before installing Kong Ingress Controller.**

    ```bash
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml
    ```

2. **Create a Gateway and GatewayClass instance to use.**

    ```bash
    kubectl apply -f kong/kong-gateway.yaml
    ```

3. **Helm Chart Installation**

    1. Add the Kong Helm charts:
    ```bash
       helm repo add kong https://charts.konghq.com
    ```
    2. Update repo:
    ```bash
       helm repo update
    ```
    3. Install Kong Ingress Controller and Kong Gateway with Helm:
    ```bash
       helm install kong kong/ingress -n kong --create-namespace --values kong/values.yaml
    ```

4. **Verify Installation**

   After installation, ensure that Kong Ingress Controller pods are running:

    ```bash
    curl -i 'localhost:8080'
    ```

   The results should look like this:
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
   **Note:**
   > If you encounter `curl: (52) Empty reply from server`, please wait a moment and try again.


5. **Create a RabbitMQ Cluster Kubernetes Operator.**

    1. Install the RabbitMQ Cluster Operator:
        ```bash
        kubectl rabbitmq install-cluster-operator
        ```
    2. Create a RabbitMQ cluster:
         ```bash
         kubectl apply -f rabbitmq/rabbitmq.yaml
         ```
    3. Create a saga exchange:
         ```bash
         kubectl exec svc/rabbitmq  -c rabbitmq -- rabbitmqadmin declare exchange name=saga type=topic -u guest -p guest
         ```
       The results should look like this:
         ```bash
         exchange declared
         ```
       **Note:**
       > RabbitMQ cluster should be running
    4. Access The Management UI (optional): 
        ```bash
        kubectl rabbitmq manage rabbitmq
        ```

### Installing order, stock and payment using Helm 📊

After setting up the Kubernetes cluster and installing the Kong Ingress Controller:

1. Use Helm to create the "order", "stock", and "payment" releases using the Saga chart and corresponding values:

   ```bash
   helm install order ./saga --values services/order/values.yaml
   helm install stock ./saga --values services/stock/values.yaml
   helm install payment ./saga --values services/payment/values.yaml
   ```

This creates three Helm releases, "order", "stock", and "payment", with configurations specified in their
respective `values.yaml` files.

Please note that each command creates a specific Helm release with its own configurations.

### 🛑 Stopping the Project

1. Run cluster delete command:

```bash
k3d cluster delete saga
```

## 🧪 Testing Scenarios with Postman Collection

1. Install [Postman](https://www.postman.com/downloads/).

2. Import the Postman [collection](docs/saga.postman_collection.json).

3. Collection contains scenarios:
    - **Unreserved Stock:** Create order with quantity > 10.
    - **Denied Payment:** Create order with amount > $1000.

4. Run requests to observe system behavior.