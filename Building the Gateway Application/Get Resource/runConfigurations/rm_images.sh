if docker container ls | grep -q "flask-app-"; then
  echo "THERE"

  docker stop flask-app-gateway
  docker rm flask-app-gateway
  docker rmi flask-app-gateway-img
  docker stop flask-app-invsys
  docker rm flask-app-invsys
  docker rmi flask-app-invsys-img

fi