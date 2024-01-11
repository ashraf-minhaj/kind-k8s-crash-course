# 0. build and push the docker image
docker build -t ashraftheminhaj/testbackend:v1 .

# docker login -u ashraftheminhaj

# 1. create the cluster
kind create cluster --config kind-config.yaml --name stage-cluster

# 2. load the docker image to the cluster
kind load docker-image ashraftheminhaj/testbackend:v1 --name stage-cluster

# 3. create deployment, it will deplioy pods with replicaset as specified
kubectl apply -f deployment.yaml

# 4. create a load balancer service
## 4.1. install MetalLb
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/namespace.yaml
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/metallb.yaml

## 4.2. create config map for metallb
kubectl create -f metallb.yaml

## 4.3. verify metallb installation
kubectl get pods -n metallb-system

# 5. create a service 
kubectl apply -f service.yaml