#!/usr/bin/env bash
set -e

# Build frontend and backend images
echo "🔨 Building backend image..."
docker build -f backend/Dockerfile -t polymarket-backend .
echo "🔨 Building frontend image..."
docker build -f frontend/Dockerfile -t polymarket-frontend frontend/
echo "Done!"
