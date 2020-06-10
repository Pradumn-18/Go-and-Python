wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/config.json
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/nginx.conf

sudo docker pull nginx:latest
sudo docker pull rabbitmq:3
sudo docker pull fogflow/discovery:3.0
sudo docker pull fogflow/broker:3.0

sudo docker run -d nginx:latest
sudo docker run -d rabbitmq:3
sudo docker run -d fogflow/discovery:3.0
sudo docker run -d fogflow/broker:3.0

sudo docker ps -a 

cd v2
pytest -s -v

sudo docker stop -d nginx:latest
sudo docker stop -d rabbitmq:3
sudo docker stop -d fogflow/discovery:3.0
sudo docker stop -d fogflow/broker:3.0


