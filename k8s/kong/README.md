# Kong Ingress Controller Installation Guide

This guide will walk you through the steps to install Kong Ingress Controller on your Kubernetes cluster.

### Prerequisites

- [Access to a Kubernetes cluster](../k3d/README.md)
- `kubectl` configured to communicate with your cluster
- [Helm installed](https://helm.sh/docs/intro/install/)

### Installation Steps

## Install the Gateway APIs

1. **Install the Gateway API CRDs before installing Kong Ingress Controller.**

    ```bash
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml
    ```

2. **Create a Gateway and GatewayClass instance to use.**

    ```bash
    kubectl apply -f k8s/kong/kong-gateway.yaml
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
       helm install kong kong/ingress -n kong --create-namespace --values k8s/kong/values.yaml
    ```

4. **Verify Installation**

   After installation, ensure that Kong Ingress Controller pods are running:

    ```bash
    curl -i 'localhost:8000'
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
   
   If you encounter `curl: (52) Empty reply from server`, please wait a moment and try again. 

### Uninstallation

To uninstall Kong Ingress Controller, simply delete the Helm release:

```bash
helm uninstall kong -n kong
```