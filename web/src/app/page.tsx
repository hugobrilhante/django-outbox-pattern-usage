"use client";
import "bootstrap/dist/css/bootstrap.min.css";
import React, { useEffect, useState } from 'react';
import { Badge, Container, Table, Button, Form } from 'react-bootstrap';
import axios from 'axios';

interface Order {
    order_id: string;
    status: string;
}

interface Stock {
    status: string;
}

interface Payment {
    status: string;
}

interface Status {
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

        const interval = setInterval(fetchData, 500);

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
            case 'not_reserved':
                return 'warning';
            case 'created':
                return 'secondary';
            case 'payment not touch':
                return 'warning';
            default:
                return 'info';
        }
    };

    const findByID = (list: any[], order_id: string): Status => {
        const found = list.find(item => item.order_id == order_id);
        return found ? found : { status: "payment not touch" };
    }

    const handleClick = async (amount: number, quantity: number) => {
        try {
            const response = await axios.post('http://localhost:8080/order/api/v1/orders/', {
                order_id: 1,
                customer_id: "1",
                product_id: "1",
                amount: amount,
                quantity: quantity
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
            <h1>Microservice Actions</h1>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Order</th>
                        <th>Stock</th>
                        <th>Payment</th>
                    </tr>
                </thead>
                <tbody>
                    {orders.map((order, index) => {
                        let order_status = order.status === 'created' ? "Loading..." : findByID(stocks, order.order_id).status
                        let payment_status = order.status === 'created' ? "Loading..." : findByID(payments, order.order_id).status
                        return (
                            <tr key={index}>
                                <td><Badge bg={getStatusVariant(order.status)}>{order.status}</Badge></td>
                                <td><Badge bg={getStatusVariant(order_status)}>{order_status}</Badge></td>
                                <td><Badge bg={getStatusVariant(payment_status)}>{payment_status}</Badge></td>
                            </tr>
                        )
                    })}
                </tbody>
            </Table>
            <div className="d-flex justify-content-center">
                <Button className="m-2" variant={getStatusVariant('payment_confirmed')} onClick={handlePaymentConfirmedButtonClick}>Confirmed Order</Button>
                <Button className="m-2" variant={getStatusVariant('payment_denied')} onClick={handlePaymentDeniedButtonClick}>Denied Payment</Button>
                <Button className="m-2" variant={getStatusVariant('not_reserved')} onClick={handleOutOfStockButtonClick}>Out of Stock</Button>
            </div>
        </Container>
    );
};

export default Home;
