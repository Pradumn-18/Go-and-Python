wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/docker-compose.yml
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/config.json
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/nginx.conf
wget https://raw.githubusercontent.com/smartfog/fogflow/master/docker/core/http/metricbeat.docker.yml

sudo docker-compose pull

sudo docker-compose up -d

sleep 30

sudo docker ps -a 

curl http://localhost:8080
curl http://127.0.0.1:8080
curl http://0.0.0.0:8080
curl http://localhost:8070/v2/entities
curl http://127.0.0.1:8070/v2/entities
curl http://0.0.0.0:8070/v2/entities

cd v2
pytest -s -v

sudo docker-compose down

