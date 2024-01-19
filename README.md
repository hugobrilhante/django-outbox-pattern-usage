# 🌐 Saga with Outbox Pattern: Orchestrating Distributed Transactions in Microservices

This repository showcases the application of the Outbox Pattern in a microservices environment, specifically using the Django Outbox Pattern library developed at [@juntossomosmais](https://github.com/juntossomosmais/django-outbox-pattern).

### Scenario: Electronic Commerce System

Consider an e-commerce system adopting microservices (Order, Stock, and Payment) to manage orders, stock, and payments. The Saga pattern is implemented using the Outbox pattern for consistent communication between services.

* **Order (Order Service):**
    - Receives and processes customer orders.
    - Creates order records in the database upon order reception.

* **Stock (Stock Service):**
    - Manages product stock.
    - Receives a message from the Order service to reserve products in stock.
    - Confirms reservation, updates the database, and records a message in the Outbox table.

* **Payment (Payment Service):**
    - Processes order payments.
    - Receives a message from the Order service for payment authorization.
    - Validates payment, authorizes it, updates the database, and records a message in the Outbox table.

### Execution Flow:

1. Customer places an order through the Order service.
2. Order service creates a record in the Outbox table with order details.
3. Message is sent to the Stock service requesting product reservation.
4. Stock service checks availability, confirms reservation, updates its database, and records a message in the Outbox table.
5. Message is sent to the Payment service requesting payment authorization.
6. Payment service validates payment, confirms authorization, updates its database, and records a message in the Outbox table.
7. Order service periodically checks the Outbox table to process pending messages.
8. If all steps complete successfully, the order is marked as confirmed, and the customer is notified.

```mermaid
sequenceDiagram
    participant Customer
    participant Order
    participant Stock
    participant Payment

    Customer ->> Order: Create Order
    Order ->> Order: Create record in Outbox table
    Order ->> Stock: Reserve Products (message)
    Stock ->> Stock: Check Availability
    Stock ->> Stock: Update database and Outbox table
    Stock -->> Order: Reservation Confirmation (message)
    Order ->> Payment: Authorize Payment (message)
    Payment ->> Payment: Check Payment
    Payment ->> Payment: Update database and Outbox table
    Payment -->> Order: Authorization Confirmation (message)
    Order -->> Customer: Order Confirmed
```

### Infrastructure for Django Applications

This repository includes configuration files for deploying three Django services (Order, Stock, Payment) on both Kubernetes and Docker Compose, each with its PostgreSQL database, and a RabbitMQ service for communication between services.

### Technologies Used

1. **Django:**
    - Web framework for rapid development of Python applications.

2. **PostgreSQL:**
    - Relational database management system.

3. **RabbitMQ:**
    - Messaging system supporting asynchronous communication between services.

4. **Kubernetes:**
    - Container orchestration platform for automation, scalability, and application management.

5. **Docker Compose:**
    - Tool for defining and running multi-container Docker applications.


## Usage Instructions with Docker

### Starting the Project

1. Navigate to the project root directory.

2. Run the start script:

    ```bash
    ./start.sh
    ```

   This Docker-specific script automates the following tasks:
   - Execute database migrations.
   - Load fixtures for initial data.
   - Create an exchange in RabbitMQ.
   - Start the required services.

3. Once the script completes, you can access the Django services and RabbitMQ using the following URLs:
   - Django App 1: [http://localhost:8000](http://localhost:8000)
   - Django App 2: [http://localhost:8001](http://localhost:8001)
   - Django App 3: [http://localhost:8002](http://localhost:8002)
   - RabbitMQ Management UI: [http://localhost:15672](http://localhost:15672)

4. Use the following credentials for Django Admin and RabbitMQ:
   - Django Admin:
     - Username: admin
     - Password: admin
   - RabbitMQ:
     - Username: guest
     - Password: guest
### Testing Scenarios with Postman Collection

To test different scenarios, you can use the provided Postman collection.

1. Install [Postman](https://www.postman.com/downloads/) if you haven't already.

2. Import the Postman [collection](Saga%20with%20Outbox%20Pattern.postman_collection.json).

3. The collection contains two scenarios for testing:

   - **Unreserved Stock:**
     - Create an order with a quantity greater than 10 to simulate an unreserved stock.
   - **Denied Payment:**
     - Create an order with an amount greater than $1000 to simulate a denied payment.

4. Run the respective requests and observe the system's behavior based on the specified scenarios.

### Stopping the Project

1. Navigate to the project root directory.

2. Run the stop script:

    ```bash
    ./stop.sh
    ```

   This Docker-specific script will gracefully stop the project, remove associated volumes, and delete logs.

3. The project is now stopped, and resources have been cleaned up.

## Usage Instructions with Kubernetes

**Note:** Instructions for Kubernetes deployment will be available soon. Stay tuned for updates!