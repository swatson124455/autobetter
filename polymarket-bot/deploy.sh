#!/usr/bin/env bash
set -e

# Ensure .env exists
if [ ! -f .env ]; then
  echo ".env file not found—please create one based on .env.example"
  exit 1
fi

# Build images
echo "🔨 Building backend image..."
docker build -f backend/Dockerfile -t polymarket-backend .
echo "🔨 Building frontend image..."
docker build -f frontend/Dockerfile -t polymarket-frontend frontend/

# Launch services
echo "🚀 Starting services via docker-compose..."
docker-compose up -d

# Wait for backend health check
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

# Final status
if [[ "$STATUS" == *"ok"* ]]; then
  echo "🎉 All services are up!"
  echo "Visit http://localhost:3000 to open the Dashboard."
else
  echo "❌ Backend never became healthy. Check logs with: docker-compose logs -f"
  exit 1
fi
