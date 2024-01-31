# Setting Up a Kubernetes Cluster with k3d 😎

This guide will walk you through setting up a Kubernetes cluster using k3d. Make sure you have Docker installed on your system before proceeding.

# Kubernetes Cluster Setup

To set up the Kubernetes cluster along with Gateway API and Kong Ingress Controller, follow these steps:

1. Navigate to the `k8s` directory.
2. Run the `setup.sh` script.

This script will automatically:

🚀 Install k3d, kubectl, and Helm if not already installed.

🌟 Create a k3d cluster named "saga" with port mapping for load balancing.

🌟 Install the Gateway API and apply Kong gateway configuration.

🌟 Add the Kong Helm repository and update Helm repositories.

🌟 Install the Kong Ingress Controller.

After running the script, your Kubernetes cluster will be set up and ready to use with Kong as the Ingress Controller.

## Installing order, stock and payment using Helm 📊

After setting up the Kubernetes cluster and installing the Kong Ingress Controller:

1. Use Helm to create the "order", "stock", and "payment" releases using the Saga chart and corresponding values:

   ```bash
   helm install order ./saga --values order/values.yaml
   helm install stock ./saga --values stock/values.yaml
   helm install payment ./saga --values payment/values.yaml
   ```

This creates three Helm releases, "order", "stock", and "payment", with configurations specified in their respective `values.yaml` files.

Please note that each command creates a specific Helm release with its own configurations.