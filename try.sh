wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/docker-compose.yml
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/config.json
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/nginx.conf
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/metricbeat.docker.yml

sudo docker-compose pull

sudo docker-compose up -d

sleep 30

sudo docker ps -a 

sudo docker logs fogflow/broker:3.0

cd v2
pytest -s -v

sudo docker-compose down

