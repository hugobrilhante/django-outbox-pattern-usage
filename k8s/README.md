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

## Applying Manifests with kubectl 💻

After setting up the Kubernetes cluster and installing the Kong Ingress Controller, you can apply manifests to deploy and manage your applications:

1. Make sure you are still in the `k8s` directory.

2. Use `kubectl` to apply all the manifests located in the `order` directory:

   ```bash
   kubectl apply -f order/
   ```

That's it! You've now set up a Kubernetes cluster with k3d, installed the Kong Ingress Controller, and applied all manifests from the `order` directory using `kubectl`. You're ready to deploy and manage your applications. 🎉