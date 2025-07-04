{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🚀 Solana Pump.fun Trading Bot - Google Colab Setup\n",
    "\n",
    "This notebook will help you deploy the Solana trading bot with AI integration using Gradio on Google Colab."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Clone the GitHub Repository"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Clone your repository (înlocuiește cu repo-ul tău)\n",
    "!git clone https://github.com/YOUR_USERNAME/solana-pump-trading-bot.git\n",
    "%cd solana-pump-trading-bot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Install Requirements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Install required packages\n",
    "!pip install -r requirements.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Check Files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Verify files are present\n",
    "!ls -la"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Run the Gradio App"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run the application\n",
    "!python app.py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Alternative: Run Everything in One Cell"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# One-click deployment\n",
    "!git clone https://github.com/YOUR_USERNAME/solana-pump-trading-bot.git\n",
    "%cd solana-pump-trading-bot\n",
    "!pip install -r requirements.txt\n",
    "!python app.py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 📝 Notes:\n",
    "\n",
    "1. **Public URL**: După rulare, Gradio va genera un link public (ex: `https://xxxxx.gradio.live`)\n",
    "2. **Phantom Wallet**: Asigură-te că ai Phantom Wallet instalat în browser\n",
    "3. **OpenAI API Key**: Vei avea nevoie de un API key de la OpenAI pentru funcționalitatea AI\n",
    "4. **Persistence**: Datele nu sunt persistente în Colab. Pentru producție, consideră un hosting dedicat\n",
    "\n",
    "## 🔧 Troubleshooting:\n",
    "\n",
    "- Dacă linkul Gradio nu funcționează, încearcă să rulezi din nou celula\n",
    "- Pentru erori de CORS, verifică că browser-ul permite iframe-uri\n",
    "- Phantom wallet poate să nu funcționeze în unele iframe-uri din cauza securității"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}