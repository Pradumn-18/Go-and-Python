
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/config.json
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/nginx.conf

sudo docker pull nginx:latest
sudo docker pull rabbitmq:3
sudo docker pull fogflow/discovery:3.0
sudo docker pull fogflow/broker:3.0
sudo docker pull fogflow/iotajson-mongo
sudo docker pull fogflow/worker
sudo docker pull fogflow/master

sudo docker run -d nginx:latest
sudo docker run -d rabbitmq:3
sudo docker run -d fogflow/iotajson-mongo
sudo docker run -d fogflow/master
sudo docker run -d fogflow/worker
sudo docker run -d fogflow/discovery:3.0
sudo docker run -d fogflow/broker:3.0

sudo docker ps -a 

cd v2
pytest -s -v



