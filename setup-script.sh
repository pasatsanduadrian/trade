#!/bin/bash

# Setup script pentru Google Colab
echo "🚀 Setting up Solana Pump.fun Trading Bot..."

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install gradio==4.19.2 Pillow>=9.0.0 -q

# Create app directory
mkdir -p solana-trading-bot
cd solana-trading-bot

# Download files from GitHub (înlocuiește cu URL-urile tale)
echo "📥 Downloading application files..."
wget -q https://raw.githubusercontent.com/YOUR_USERNAME/solana-pump-trading-bot/main/app.py
wget -q https://raw.githubusercontent.com/YOUR_USERNAME/solana-pump-trading-bot/main/index.html
wget -q https://raw.githubusercontent.com/YOUR_USERNAME/solana-pump-trading-bot/main/requirements.txt

echo "✅ Setup complete!"
echo "🎯 Running the application..."

# Run the app
python app.py