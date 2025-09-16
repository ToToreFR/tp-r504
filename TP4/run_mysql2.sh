docker run --rm -d \
  -p 3307:3306 \
  -v vol-sql-demo:/var/lib/mysql \
  --name tp4-sql \
  --env MYSQL_ROOT_PASSWORD=foo \
  --network net-tp42 \
  mysql:8.0
