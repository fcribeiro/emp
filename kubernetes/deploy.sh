#!/bin/bash

#helm install --name my-kafka incubator/kafka

cd zipkin/
docker build -t fcribeiro/zipkin-emp .
docker push fcribeiro/zipkin-emp

cd ..

kubectl create -f zipkin_emp.yaml

kubectl create -f songs_deployment.yaml

kubectl get services
