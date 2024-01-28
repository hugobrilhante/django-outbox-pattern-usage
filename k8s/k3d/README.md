# k3d - Lightweight Kubernetes Distribution

k3d is a tool designed to easily create, manage, and operate Kubernetes clusters. It is lightweight, efficient, and provides a seamless way to work with Kubernetes clusters for development and testing purposes.

## Installation

### Linux:

```bash
curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash
```

### macOS:

```bash
brew install k3d
```

### Windows:

You can download the latest executable from the [official GitHub releases page](https://github.com/rancher/k3d/releases) and add it to your PATH.

## Creating a Cluster

You can create a cluster with or without specifying the number of server nodes. Below are two methods:

### Method 1: Creating a Cluster with Server Nodes

To create a cluster with server nodes, you can use the following command:

```bash
k3d cluster create saga --servers 3 --agents 3 --port '8000:30000@loadbalancer'
```

This command creates a Kubernetes cluster named "saga" with port forwarding configured to forward traffic from port 8000 on the host to port 30000 on the load balancer, along with three server nodes and three agent nodes, providing a comprehensive environment for your Kubernetes development and testing needs.

### Method 2: Creating a Cluster without Agent Nodes

If you don't need agent nodes and only want server nodes, you can create a cluster without specifying the number of agent nodes. Here's how:

```bash
k3d cluster create saga --port '8000:30000@loadbalancer'
```

This command creates a Kubernetes cluster named "saga" with port forwarding configured to forward traffic from port 8000 on the host to port 30000 on the load balancer, along with three server nodes. This setup is suitable for scenarios where you only require server nodes for your Kubernetes environment.