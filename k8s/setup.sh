#!/bin/bash

# Function to install k3d
install_k3d() {
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
}

# Function to create k3d cluster
create_k3d_cluster() {
    echo "🌟 Creating k3d cluster..."
    k3d cluster create saga --port '8080:30000@loadbalancer'
}

# Function to install kubectl
install_kubectl() {
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
}

# Function to install krew
install_krew() {
    echo "🚀 Installing krew..."
    (
      set -x; cd "$(mktemp -d)" &&
      OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
      ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
      KREW="krew-${OS}_${ARCH}" &&
      curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
      tar zxvf "${KREW}.tar.gz" &&
      ./"${KREW}" install krew
    )

    # Add krew to PATH in shell configuration
    if [[ -d "$HOME/.krew/bin" ]]; then
        if [[ ":$PATH:" != *":$HOME/.krew/bin:"* ]]; then
            echo 'export PATH="$HOME/.krew/bin:$PATH"' >> "$shell_config"
            export PATH="$HOME/.krew/bin:$PATH"
        fi
    fi
}

# Function to install RabbitMQ plugin for kubectl
install_rabbitmq_plugin() {
    echo "🚀 Installing kubectl RabbitMQ plugin..."
    kubectl krew install rabbitmq
}

# Function to install Helm
install_helm() {
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
}

# Function to choose shell
choose_shell() {
    PS3="Please select your preferred shell: "
    select option in "bash" "zsh" "quit"; do
        case "$option" in
            "bash")
                shell_config="$HOME/.bashrc"
                break
                ;;
            "zsh")
                shell_config="$HOME/.zshrc"
                break
                ;;
            "quit")
                exit
                ;;
            *)
                echo "Invalid option. Please select again."
                ;;
        esac
    done
}

# Main script

# Install k3d if not installed
if ! command -v k3d &> /dev/null; then
    install_k3d
fi

# Create k3d cluster
create_k3d_cluster

# Install kubectl if not installed
if ! command -v kubectl &> /dev/null; then
    install_kubectl
fi

# Choose shell
choose_shell

# Install krew
install_krew

# Install RabbitMQ plugin for kubectl
install_rabbitmq_plugin

# Install Helm if not installed
if ! command -v helm &> /dev/null; then
    install_helm
fi

echo "✅ Setup completed successfully!"
