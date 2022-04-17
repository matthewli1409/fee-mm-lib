#!/bin/bash

bellagio=$(kubectl get pods -l component=bellagio -o custom-columns=:metadata.name)
kubectl attach $bellagio