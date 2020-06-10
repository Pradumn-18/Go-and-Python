wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/config.json
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/nginx.conf

sudo docker pull nginx:latest
sudo docker pull rabbitmq:3
sudo docker pull fogflow/discovery:3.0
sudo docker pull fogflow/broker:3.0

sudo docker run fogflow/discovery:3.0 -c "/home/travis/gopath/src/github.com/Pradumn-18/Go-and-Python/config.json"
sudo docker run -p 8070:8070 fogflow/broker:3.0 -c "/home/travis/gopath/src/github.com/Pradumn-18/Go-and-Python/config.json"

sudo docker ps -a 

cd v2
pytest -s -v

sudo docker-compose down

