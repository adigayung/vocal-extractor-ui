import gradio as gr
import os
import subprocess
import shutil

# Deteksi apakah di Colab
try:
    import google.colab
    IS_COLAB = True
except ImportError:
    IS_COLAB = False

OUTPUT_DIR = "output"

def extract_vocals_from_folder(folder_path):
    if not os.path.isdir(folder_path):
        return "❌ Folder tidak ditemukan."

    audio_files = [f for f in os.listdir(folder_path) if f.endswith((".mp3", ".wav"))]
    if not audio_files:
        return "⚠️ Tidak ada file audio di folder tersebut."

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    processed = 0
    for file in audio_files:
        full_path = os.path.join(folder_path, file)
        filename = os.path.splitext(file)[0]

        command = [
            "demucs",
            "--two-stems", "vocals",
            "--out", OUTPUT_DIR,
            full_path
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            return f"❌ Gagal memproses file: {file}\n\n{str(e)}"

        # Move hasil vokal ke direktori output utama
        src = os.path.join(OUTPUT_DIR, "htdemucs", filename, "vocals.wav")
        dest = os.path.join(OUTPUT_DIR, f"{filename}.wav")
        if os.path.exists(src):
            shutil.move(src, dest)
            processed += 1

    return f"✅ Berhasil memproses {processed} file audio.\nHasil disimpan di folder `./{OUTPUT_DIR}`"

# Setup Gradio UI
demo = gr.Interface(
    fn=extract_vocals_from_folder,
    inputs=gr.Textbox(label="Path Folder Audio"),
    outputs=gr.Textbox(label="Status"),
    title="🎤 Vocal Extractor UI",
    description="Masukkan path ke folder berisi file .mp3/.wav untuk mengekstrak vokal saja."
)

# Jalankan dengan atau tanpa share tergantung platform
demo.launch(share=IS_COLAB)
