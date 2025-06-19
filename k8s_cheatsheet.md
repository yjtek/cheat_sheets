# Manage AWS SSO profiles
- See in `~/.aws/config`

# Login to AWS CLI
- The export is needed because kubectl references environment variable `AWS_PROFILE`, so even if you're logged in you may not have access to cluster

- `aws sso login --profile ffds`
- `export AWS_PROFILE=ffds`

# Confirm that you're using the right AWS account
- `aws sts get-caller-identity`

# Find clusters available to you based on your caller identity
- `aws eks list-clusters`

# Add aws cluster to kubernetes
- Writes to ~/.kube/config
- `aws eks --region ap-southeast-1 update-kubeconfig --name prd-tiger --alias prd-tiger`

# Manage the added contexts
- `kubectl config get-contexts`
- `kubectl config delete-context`

# Swap to use the appropriate AWS cluster context
- `kubectl config use-context prd-tiger`

# Filter pods to specific namespace
- Obviously for shared clusters, you won't have access to all pods, only those within a specific namespace (see "find pods" below)
- To avoid having to filter to a namespace with every query, you can set the default `--namespace` to use
- `kubectl config set-context --current --namespace=mkpl-mle`

# Find pods
- `kubectl get pods` 
- `kubectl get pods -namespace mkpl-mle`

# See all containers in a pod. Most pods will have 1 container, some may have more
- `kubectl get pod flink-transport-surge-redis-taskmanager-6849d78c87-82vbz -o jsonpath="{.spec.containers[*].name}"`

# Check logs from pods
- If a pod has multiple containers, and container name is not specified, it returns the first one
- `kubectl logs flink-transport-surge-redis-taskmanager-6849d78c87-82vbz --namespace mkpl-mle`
- `kubectl logs flink-transport-surge-redis-taskmanager-6849d78c87-82vbz --namespace mkpl-mle -c grabx`

# Describe pod
- `kubectl describe pod flink-transport-surge-redis-taskmanager-6849d78c87-82vbz --namespace mkpl-mle`

# Check pod's resource usage
- `kubectl top pod flink-transport-surge-redis-taskmanager-6849d78c87-82vbz --namespace mkpl-mle`

# Delete pod
- The behaviour of `delete` differs depending on how the pod is set up. 
    - if created manually, `delete` simply removes the pod, no new pod will take its place
    - if created via some controller (e.g. Deployment, ReplicaSet, StatefulSet, Job), then a new one will be spun up. So `delete` is more of a `restart` in this case
- `kubectl delete pod flink-transport-surge-redis-taskmanager-6849d78c87-82vbz --namespace mkpl-mle`

# Enter the pod via command line
- `kubectl exec -it flink-transport-surge-redis-taskmanager-6849d78c87-82vbz --namespace mkpl-mle -- /bin/sh`

# If pod doesn't have command line built in, attach an ephemeral command line
- `kubectl debug -it flink-transport-surge-redis-taskmanager-6849d78c87-82vbz -n mkpl-mle --image=busybox --target=<container-name>`

# Expose a port for a pod, so you can hit an API
- `kubectl port-forward pod/<pod-name> 8080:80 -n <namespace>`

# Copy something into the pod
- `kubectl cp <namespace>/<pod-name>:/app/log.txt ./log.txt`

# StatefulSet vs Deployment vs Job
- **StatefulSet** is needed when your application needs permanent name so it can be referred to specifically. 
    - For example, when you have a distributed database that is sharded across multiple pods. Then Statefulset maintains the names of the pods, so even if there is a shutdown, the restarted pod has the same reference

- **Deployment** is for everything else that is stateless

- **Job** is for shortlived tasks. It conveniently shuts down once job is done, and retries if job is failed
