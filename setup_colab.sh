#!/bin/bash

# Setup script for Google Colab
set -e

echo "🚀 Setting up Solana Pump.fun Trading Bot..."

# Install Python dependencies
pip install gradio==4.44.1 Pillow>=9.0.0 -q

# Create app directory
mkdir -p solana-trading-bot
cd solana-trading-bot

# Download files from GitHub (replace USERNAME with your repo)
wget -q https://raw.githubusercontent.com/YOUR_USERNAME/solana-pump-trading-bot/main/app.py
wget -q https://raw.githubusercontent.com/YOUR_USERNAME/solana-pump-trading-bot/main/index.html
wget -q https://raw.githubusercontent.com/YOUR_USERNAME/solana-pump-trading-bot/main/requirements.txt

echo "✅ Setup complete!"

# Run the app
python app.py
