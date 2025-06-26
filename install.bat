@echo off
echo 🔧 Creating virtual environment in .\venv...
python -m venv venv
call venv\Scripts\activate

echo 📦 Installing PyTorch with CUDA 11.8...
python -m pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

echo 📦 Installing project requirements...
pip install -r requirements.txt

echo ✅ Setup complete. To activate venv later, run: venv\Scripts\activate
pause
