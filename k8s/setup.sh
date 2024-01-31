#!/bin/bash

# Check if k3d is installed
if ! command -v k3d &> /dev/null; then
    echo "🚀 Installing k3d..."
    # Install k3d based on the operating system
    if [[ "$(uname)" == "Darwin" ]]; then
        brew install k3d
    elif [[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]]; then
        curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash
    else
        echo "❌ Unsupported operating system"
        exit 1
    fi
fi

# Create k3d cluster
echo "🌟 Creating k3d cluster..."
k3d cluster create saga --port '8080:30000@loadbalancer'

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    echo "🚀 Installing kubectl..."
    # Install kubectl
    if [[ "$(uname)" == "Darwin" ]]; then
        brew install kubectl
    elif [[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]]; then
        curl -LO https://dl.k8s.io/release/v1.23.2/bin/linux/amd64/kubectl
        sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    else
        echo "❌ Unsupported operating system"
        exit 1
    fi
fi

# Check if helm is installed
if ! command -v helm &> /dev/null; then
    echo "🚀 Installing Helm..."
    # Install Helm
    if [[ "$(uname)" == "Darwin" ]]; then
        brew install helm
    elif [[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]]; then
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
        chmod 700 get_helm.sh
        ./get_helm.sh
    else
        echo "❌ Unsupported operating system"
        exit 1
    fi
fi


echo "✅ Setup completed successfully!"
