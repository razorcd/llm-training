#### Run elasticsearch

```
docker run -it --rm --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enable=false" docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

#### Run Qdrant

```
docker run --rm -p 6333:6333 -p 6334:6334 -v "$(pwd)/h2/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```