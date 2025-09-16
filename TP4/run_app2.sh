docker run -d \
  --name tp4-app2 \
  --network net-tp42 \
  -v "$(pwd)/srv/:/srv/" \
  -p 5000:5000 \
  im-tp42
