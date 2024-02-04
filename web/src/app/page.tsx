"use client"
import "bootstrap/dist/css/bootstrap.min.css";
import React, { useEffect, useState } from 'react';
import { Badge, Container, Table, Button } from 'react-bootstrap';
import axios from 'axios';

interface Order {
  status: string;
}

interface Stock {
  status: string;
}

interface Payment {
  status: string;
}

const Home: React.FC = () => {
  const [orders, setOrders] = useState<Order[]>([]);
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [payments, setPayments] = useState<Payment[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const orderResponse = await axios.get<Order[]>('http://localhost:8080/order/api/v1/orders/');
        setOrders(orderResponse.data);

        const stockResponse = await axios.get<Stock[]>('http://localhost:8080/stock/api/v1/reservations/');
        setStocks(stockResponse.data);

        const paymentResponse = await axios.get<Payment[]>('http://localhost:8080/payment/api/v1/payments/');
        setPayments(paymentResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    const interval = setInterval(fetchData, 1000);

    return () => clearInterval(interval);
  }, []);

  const getStatusVariant = (status: string): string => {
    switch (status) {
      case 'payment_confirmed':
        return 'success';
      case 'reserved':
        return 'primary';
      case 'payment_denied':
        return 'danger';
      case 'out_of_stock':
        return 'warning';
      default:
        return 'secondary';
    }
  };

  const handleClick = async (amount: number, quantity: number) => {
    try {
      const response = await axios.post('http://localhost:8080/order/api/v1/orders/', {
        order_id: 1,
        customer_id: "1",
        product_id: "1",
        amount: amount,
        quantity: quantity,
      });
      console.log('API Response:', response.data);
    } catch (error) {
      console.error('Error making API request:', error);
    }
  };

  const handlePaymentConfirmedButtonClick = () => {
    handleClick(1, 1);
  };

  const handlePaymentDeniedButtonClick = () => {
    handleClick(1000, 1);
  };

  const handleOutOfStockButtonClick = () => {
    handleClick(1, 11);
  };

  return (
    <Container className="text-center">
      <h1>Saga Outbox Pattern</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Status</th>
            <th>Order</th>
            <th>Stock</th>
            <th>Payment</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order, index) => (
            <tr key={index}>
              <td>Current</td>
              <td><Badge bg={getStatusVariant(order.status)}>{order.status}</Badge></td>
              <td><Badge bg={getStatusVariant(stocks[index]?.status)}>{stocks[index]?.status}</Badge></td>
              <td><Badge bg={getStatusVariant(payments[index]?.status)}>{payments[index]?.status}</Badge></td>
            </tr>
          ))}
        </tbody>
      </Table>
      <div className="d-flex justify-content-center">
        <Button className="m-2" variant={getStatusVariant('payment_confirmed')} onClick={handlePaymentConfirmedButtonClick}>Confirmed Order</Button>
        <Button className="m-2" variant={getStatusVariant('payment_denied')} onClick={handlePaymentDeniedButtonClick}>Denied Payment</Button>
        <Button className="m-2" variant={getStatusVariant('out_of_stock')} onClick={handleOutOfStockButtonClick}>Out of Stock</Button>
      </div>
    </Container>
  );
};

export default Home;
