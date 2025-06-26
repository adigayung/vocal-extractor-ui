#!/bin/bash
echo "🔧 Creating virtual environment in ./venv..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Installing PyTorch with CUDA 11.8..."
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

echo "📦 Installing project requirements..."
pip install -r requirements.txt

echo "✅ Setup complete. To activate venv later, run: source venv/bin/activate"
