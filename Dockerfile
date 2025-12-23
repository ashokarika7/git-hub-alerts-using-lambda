# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Create a non-root user to avoid pip warnings
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /home/app

# Set working directory in container
WORKDIR /home/app

# Install system dependencies (if needed for your app)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Switch to non-root user
USER app

# Copy requirements first (for better Docker layer caching)
COPY --chown=app:app requirements.txt .

# Install Python dependencies as non-root user
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the rest of the application code
COPY --chown=app:app . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Add user local bin to PATH
ENV PATH="/home/app/.local/bin:$PATH"

# Run the FastAPI application with uvicorn (remove --reload for production)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
