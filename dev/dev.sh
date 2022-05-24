helm uninstall development
docker build -t localhost:5000/cl-data-dashboard:registry ../src
docker push localhost:5000/cl-data-dashboard:registry
helm install --values ../helm/values/dev.yaml development ../helm/cl-data-dashboard