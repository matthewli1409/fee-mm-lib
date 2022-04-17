#!/bin/bash

hm=$(kubectl get pods -l component=hatchet-man -o custom-columns=:metadata.name)
kubectl attach $hm