# Stage 1: Build React frontend
FROM node:20-alpine AS frontend-build
RUN apk update && apk add --no-cache git python3 make g++
WORKDIR /app
COPY frontend/package.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Install Python dependencies & copy backend
FROM python:3.11-slim AS backend-build
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/app ./app

# Copy built frontend into backend static folder
COPY --from=frontend-build /app/build ./app/frontend_build

# Stage 3: Final runtime image
FROM python:3.11-slim
WORKDIR /app
COPY --from=backend-build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=backend-build /app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
