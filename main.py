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
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 🔹 Fungsi ekstrak vokal dari satu file
def extract_vocals_single(file):
    if file is None:
        return None, "❌ Tidak ada file dipilih."

    filename = os.path.splitext(os.path.basename(file.name))[0]

    command = [
        "demucs",
        "--two-stems", "vocals",
        "--out", OUTPUT_DIR,
        file.name
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return None, f"❌ Gagal memproses file: {file.name}\n\n{str(e)}"

    src = os.path.join(OUTPUT_DIR, "htdemucs", filename, "vocals.wav")
    dest = os.path.join(OUTPUT_DIR, f"{filename}.wav")
    if os.path.exists(src):
        shutil.move(src, dest)
        return dest, f"✅ Vokal berhasil diekstrak: {dest}"
    else:
        return None, "❌ File vokal tidak ditemukan setelah proses."


# 🔹 Fungsi ekstrak dari folder path (bulk)
def extract_vocals_from_folder(folder_path):
    if not os.path.isdir(folder_path):
        return "❌ Folder tidak ditemukan."

    audio_files = [f for f in os.listdir(folder_path) if f.endswith((".mp3", ".wav"))]
    if not audio_files:
        return "⚠️ Tidak ada file audio di folder tersebut."

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

        src = os.path.join(OUTPUT_DIR, "htdemucs", filename, "vocals.wav")
        dest = os.path.join(OUTPUT_DIR, f"{filename}.wav")
        if os.path.exists(src):
            shutil.move(src, dest)
            processed += 1

    return f"✅ Berhasil memproses {processed} file audio.\nHasil disimpan di folder `./{OUTPUT_DIR}`"

# 🔹 UI Gradio
with gr.Blocks(title="🎤 Vocal Extractor UI") as demo:
    gr.Markdown("## 🎶 Vocal Extractor UI")

    with gr.Tabs():
        with gr.TabItem("🎧 Single File Extractor"):
            audio_input = gr.File(label="Upload audio file (.mp3 / .wav)", type="filepath")
            single_audio = gr.Audio(label="🔊 Hasil Vokal (preview)", type="filepath")
            single_output = gr.Textbox(label="Status")
            extract_btn = gr.Button("Ekstrak Vokal")
            extract_btn.click(fn=extract_vocals_single, inputs=audio_input, outputs=[single_audio, single_output])

        with gr.TabItem("📂 Folder Bulk Extractor"):
            folder_path = gr.Textbox(label="Path Folder Audio")
            bulk_output = gr.Textbox(label="Status")
            bulk_btn = gr.Button("Ekstrak Semua")
            bulk_btn.click(fn=extract_vocals_from_folder, inputs=folder_path, outputs=bulk_output)

# Jalankan Gradio UI
demo.launch(share=IS_COLAB)
