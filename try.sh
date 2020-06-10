wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/config.json
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/nginx.conf

sudo docker pull nginx:latest
sudo docker pull rabbitmq:3
sudo docker pull fogflow/discovery:3.0
sudo docker pull fogflow/broker:3.0

sudo docker run rabbitmq:3
sudo docker run fogflow/discovery:3.0
sudo docker run fogflow/broker:3.0

sudo docker ps -a 

cd v2
pytest -s -v

sudo docker-compose down

