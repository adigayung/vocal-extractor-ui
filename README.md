# 🎤 Vocal Extractor UI

**Vocal Extractor UI** is a simple web-based interface for extracting vocals from `.mp3` or `.wav` audio files using [Demucs](https://github.com/facebookresearch/demucs) and [Gradio](https://www.gradio.app/).  
It lets you process entire folders of music files and isolates the vocals automatically — perfect for remixing, karaoke, or audio analysis.

---

## 🚀 Features

- ✅ Extract vocals using Demucs (deep learning model)
- ✅ Simple and intuitive Gradio-based interface
- ✅ Process all audio files in a folder at once
- ✅ Compatible with local machine or Google Colab (auto-detect)

---

## 📦 Requirements

Make sure you have:

- Python 3.8+
- pip
- [Demucs](https://github.com/facebookresearch/demucs)

Linux/macOS:

```bash
git clone https://github.com/adigayung/vocal-extractor-ui
cd vocal-extractor-ui
chmod +x install.sh
bash install.sh
source venv/bin/activate
```

Windows:
```bash
git clone https://github.com/adigayung/vocal-extractor-ui
cd vocal-extractor-ui
install.bat
```

🧪 Run :
```bash
python main.py
```

☁️ Run on Google Colab
Copy the script into a Google Colab notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adigayung/vocal-extractor-ui/main/colab.ipynb)

The app will automatically launch with a public URL using Gradio share=True

📜 License
This project is open-source under the MIT License.
