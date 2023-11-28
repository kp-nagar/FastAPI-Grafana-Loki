# FastAPI-Grafana-Loki
In this repo I manage log of FastAPI using Grafana Loki.

### To setup grafana
```
docker compose -f grafana-docker-compose.yaml up
```

### To start FastAPI
```
docker compose -f fast-docker-compose.yaml up
```

###NOTE
```
FOR ERROR: no log driver named 'loki'
Run below cmd
docker plugin install  grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```