if docker container ls | grep -q "flask-app-"; then
  docker stop flask-app-invsys
  docker rm flask-app-invsys
  docker rmi flask-app-invsys-img
fi