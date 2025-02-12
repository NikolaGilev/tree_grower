kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/database.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml

kubectl get all -n kiii
kubectl get ingress -n kiii
