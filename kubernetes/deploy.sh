#!/bin/bash

cd zipkin/
docker build -t fcribeiro/zipkin-emp .
docker push fcribeiro/zipkin-emp

cd ..

kubectl create -f zipkin_emp.yaml

kubectl get services
