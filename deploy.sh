#!/usr/bin/env bash
set -e

# Auto-copy .env from example if missing
if [ ! -f .env ] && [ -f .env.example ]; then
  echo "Creating .env from .env.example"
  cp .env.example .env
fi

# Build images
echo "🔨 Building backend image..."
docker build -f Dockerfile -t polymarket-bot .
 
# Launch container
echo "🚀 Running container..."
docker run -d -p 8000:8000 --env-file .env polymarket-bot

# Health check
echo -n "⏳ Waiting for backend health to be OK"
for i in {1..10}; do
  STATUS=$(curl -s http://localhost:8000/health || echo "")
  if [[ "$STATUS" == *"ok"* ]]; then
    echo " ✅"
    break
  else
    echo -n "."
    sleep 1
  fi
done

if [[ "$STATUS" == *"ok"* ]]; then
  echo "🎉 App is live at http://localhost:8000 (React served at root)"
else
  echo "❌ Backend never became healthy."
  docker logs $(docker ps -q --filter ancestor=polymarket-bot)
  exit 1
fi
