# Dockerfile - Python 3.11 Slim
FROM python:3.11-slim

# Install Node.js 18.x
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Verify installations
RUN python3 --version && node --version && npm --version

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot files
COPY . .

# Create directories
RUN mkdir -p kelvin_uploads kelvin_data

EXPOSE 8080

CMD ["python3", "main.py"]
