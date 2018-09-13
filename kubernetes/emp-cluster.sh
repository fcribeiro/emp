#!/bin/bash

# Delete Cluster
#gcloud container clusters delete emp-cluster

# Config Project
gcloud config set project calcium-ember-185414
gcloud config set compute/region europe-west1
gcloud config set compute/zone europe-west1-b

# Create Pluster
gcloud container clusters create emp-cluster --num-nodes=3 --machine-type=n1-standard-2 --image-type=UBUNTU

# Get Cluster Configs
gcloud container clusters get-credentials emp-cluster


# Install Helm
kubectl create clusterrolebinding add-on-cluster-admin \
  --clusterrole=cluster-admin \
  --serviceaccount=kube-system:default

helm init --service-account default


#sleep 5

# Install Kafka
#helm install --name my-kafka incubator/kafka

# Testing Kafka
	#After Kafka is up and running

#kubectl create -f kafka_pod.yml
#kubectl -n default exec testclient -- /usr/bin/kafka-topics --zookeeper my-kafka-zookeeper:2181 --topic zipkin --create --partitions 1 --replication-factor 1
#kubectl -n default exec -ti testclient -- /usr/bin/kafka-console-consumer --bootstrap-server my-kafka:9092 --topic zipkin --from-beginning


#sh ./deploy.sh


