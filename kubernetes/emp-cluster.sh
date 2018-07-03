#!/bin/bash

# Delete Cluster
gcloud container clusters delete emp-cluster

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

# Install Kafka
#helm install --name my-kafka incubator/kafka





# Testing Kafka

#kubectl -n default exec testclient -- /usr/bin/kafka-topics --zookeeper my-kafka-zookeeper:2181 --topic test1 --create --partitions 1 --replication-factor 1

#kubectl -n default exec -ti testclient -- /usr/bin/kafka-console-consumer --bootstrap-server my-kafka:9092 --topic test1 --from-beginning







# OTHER

#gcloud beta compute disks create --zone europe-west1-b --size 10GB gce-disk-1


#gcloud compute disks create mysql-disk --size=10GB --zone=europe-west1-b --type=pd-standard --no-require-csek-key-create


#gcloud compute instances stop INSTANCE_NAMES --zone=europe-west1-b