function dcu { docker compose up -d }
function dcd { docker compose down }
function dps { docker ps }
function dep { docker exec -it streaming-replication-postgres_primary-1 psql -U zuser -d zdb }
function der { docker exec -it streaming-replication-postgres_replica-1 psql -U zuser -d zdb }
function dlp { docker logs streaming-replication-postgres_primary-1 }
function dlr { docker logs streaming-replication-postgres_replica-1 }