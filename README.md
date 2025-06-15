#### Run elasticsearch

```
docker run -it --name elasticsearch -p 9200:9200 -p 9300:93000 -e "discovery.type=single-n
ode" -e "xpack.security.enable=false" docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```