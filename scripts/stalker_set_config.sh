#!/bin/bash

bellagio=$(kubectl get pods -l component=bellagio -o custom-columns=:metadata.name)
kubectl cp ~/code/bfx-bellagio/config/settings.json $bellagio:/usr/src/app/config/settings.json