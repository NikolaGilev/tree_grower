kubectl apply -f namespace.yaml -f database.yaml -f deployment.yaml -f service.yaml -f ingress.yaml

kubectl get all -n kiii
kubectl get ingress -n kiii


kubectl rollout restart deployment kiii-project-deployment -n kiii
kubectl delete pod -n kiii --all
kubectl get pods -n kiii
