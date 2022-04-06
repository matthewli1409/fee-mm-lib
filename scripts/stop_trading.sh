#!/bin/bash

funding=$(kubectl get pods -l component=redis -o custom-columns=:metadata.name)
kubectl exec -it $funding -- redis-cli set BFX_FEE-stalker-trading-on 0