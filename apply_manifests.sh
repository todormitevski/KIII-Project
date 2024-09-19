#!/bin/bash

K8S_DIR="./k8s"

kubectl apply -f $K8S_DIR/namespace.yaml \
              -f $K8S_DIR/configmap-secret-app.yaml \
              -f $K8S_DIR/configmap-secret-db.yaml \
              -f $K8S_DIR/deployment-service-app.yaml \
              -f $K8S_DIR/statefulset-service-db.yaml \
              -f $K8S_DIR/ingress.yaml

echo "All Kubernetes manifests applied successfully."
