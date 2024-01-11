## Simplified Step-by-Step Procedure to Deploy a Project on a Kubernetes Cluster:

### 1. Create a Kubernetes Cluster:

- Set up a Kubernetes cluster using a platform like Minikube, kind, or a cloud provider like AWS, GKE, or Azure.

### 2. Create a Pod Manifest:

- Write a Pod manifest file (`pod.yaml`) specifying the container image, ports, and any other configurations needed for your application.

### 3. Create a Deployment Manifest:

- Write a Deployment manifest file (`deployment.yaml`) to manage and scale your Pods. Specify the desired number of replicas, pod template details, and image information.

### 4. Apply Deployment:

- Use `kubectl apply -f deployment.yaml` to create or update the deployment, resulting in the desired number of running Pods.

### 5. Create a Service Manifest:

- Write a Service manifest file (`service.yaml`) to expose your Pods. Define the service type (e.g., LoadBalancer, ClusterIP), ports, and the selector to match your Pod labels.

### 6. Apply Service:

- Use `kubectl apply -f service.yaml` to create or update the service, providing a stable endpoint for accessing your application.

### 7. Verify Deployment:

- Use `kubectl get pods`, `kubectl get services`, and `kubectl get deployments` to verify the status of your deployment and services.

### 8. Access Application:

- If using a LoadBalancer service, check for the external IP assigned (`kubectl get services`). Access your application using this external IP.


### From stackoverflow - 

**Kubernetes has three Object Types** you should know about:

- Pods - runs one or more closely related containers
- Services - sets up networking in a Kubernetes cluster
- Deployment - Maintains a set of identical pods, ensuring that they have the correct config and that the right number of them exist.

**Pods:**
    - Runs a single set of containers
    - Good for one-off dev purposes
    - Rarely used directly in production

**Deployment:**
    - Runs a set of identical pods
    - Monitors the state of each pod, updating as necessary
    - Good for dev
    - Good for production

Forget about Pods and just use Deployment. Why? Look at the second bullet point, it monitors the state of each pod, updating as necessary.
So, instead of struggling with error messages such as this one:

`Forbidden: pod updates may not change fields other than spec.containers[*].image`

**So just refactor or completely recreate your Pod into a Deployment that creates a pod to do what you need it to do**. With `Deployment` you can change any piece of configuration you want to and you need not worry about seeing that error message.

### commands -
- create a pod using pod manifest file `kubectl apply -f custom-pod.yaml`
- delete pod `kubectl delete pod <pod-name>`
- cleanup/delete deplpyments `kubectl delete deployments --all`
- delete all nodes `kubectl delete nodes --al`