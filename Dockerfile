FROM python:3.11-slim

# Working directory သတ်မှတ်မယ်
WORKDIR /app

# System dependencies (ffmpeg, zip, curl စသဖြင့် လိုအပ်တာတွေ)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    ffmpeg \
    imagemagick \
    zip \
    unzip \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# requirements ကို အရင် copy လုပ်ပြီး cache သုံးမယ်
COPY requirements.txt .

# Python packages တွေ install
RUN pip install --no-cache-dir -r requirements.txt

# ကျန်တဲ့ ဖိုင်တွေ အားလုံး copy
COPY . .

# ဘော့က လိုအပ်တဲ့ folder တွေ ဖန်တီးမယ်
RUN mkdir -p kelvin_uploads kelvin_data

# Flask keep-alive အတွက် port expose
EXPOSE 8080

# Environment variable
ENV PORT=8080

# Bot စတင်မယ်
CMD ["python", "main.py"]
