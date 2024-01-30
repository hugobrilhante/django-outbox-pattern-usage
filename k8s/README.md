# Setting Up a Kubernetes Cluster with k3d 😎

This guide will walk you through setting up a Kubernetes cluster using k3d. Make sure you have Docker installed on your system before proceeding.

## Getting Started 🚀

Follow these steps to create a Kubernetes cluster using k3d:

1. Make sure you are in the `k8s` directory:

   ```bash
   cd k8s
   ```

2. Follow the instructions in the README.md file located in the `k3d` directory to create a Kubernetes cluster using k3d.

## Installing Kong Ingress Controller 🦍

To install the Kong Ingress Controller for managing external access to services in your Kubernetes cluster:

1. Make sure you are still in the `k8s` directory.

2. Follow the instructions in the README.md file located in the `kong` directory to install the Kong Ingress Controller.

## Installing Chart using Helm 📊

After setting up the Kubernetes cluster and installing the Kong Ingress Controller:

1. Navigate to the directory containing the `order` chart and its `values.yaml` file.

2. Use Helm to create a release named "order" using the Saga chart and values from `order/values.yaml`:

   ```bash
   helm install order ./saga --values order/values.yaml
   ```

This creates a Helm release named "order" with the configurations specified in `order/values.yaml`.