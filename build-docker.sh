#!/bin/bash

# Gmail Alerter Docker Build Script

echo "🏗️  Building Gmail Alerter Docker Image..."

# Build the Docker image
docker build -t gmail-alerter .

echo "✅ Docker image built successfully!"

echo ""
echo "🚀 To run the container:"
echo "   docker run -p 8000:8000 --env-file .env gmail-alerter"
echo ""
echo "📚 API Documentation will be available at:"
echo "   http://localhost:8000/docs"
echo ""
echo "💡 Or use docker-compose:"
echo "   docker-compose up -d"
