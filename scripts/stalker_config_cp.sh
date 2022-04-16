#!/bin/bash

bellagio=$(kubectl get pods -l component=bellagio -o custom-columns=:metadata.name)
kubectl cp ~/code/bfx-bellagio/config/stalker_priority_orders.json $bellagio:/usr/src/app/config/stalker_priority_orders.json