#!/bin/bash

kubectl apply -f k8s/configmap.yaml
kubectl rollout restart deployment/neuron