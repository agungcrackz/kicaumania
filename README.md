# kicaumania 🎵

Putar video sebagai ASCII art langsung di terminal, lengkap dengan audio.

## Demo

```
..:-=+*#%@@@#*+=-:..
.:-=+*##@@@@@@##*+=-:.
:-=+*#@@@@@@@@@@#*+=-:
```

## Requirements

- Python 3.8+
- Terminal yang support ANSI escape codes

Install dependencies:

```bash
pip install opencv-python ffpyplayer numpy
```

## Cara Pakai

1. Taruh file video di folder yang sama dengan `kicau.py`
2. Edit bagian konfigurasi di `kicau.py`:

```python
# === KONFIGURASI ===
VIDEO_FILE  = "nama_video.mp4"
ASCII_CHARS = " .:-=+*#%@"  # bisa diganti sesuai selera
# ===================
```

3. Jalankan:

```bash
python kicau.py
```

Tekan `Ctrl+C` untuk berhenti.

## Fitur

- Auto-detect lebar terminal
- Sinkronisasi FPS dengan video asli
- Audio berjalan bersamaan dengan video
- Rendering cepat menggunakan numpy (tanpa loop per pixel)
- Tidak ada flicker — menggunakan ANSI cursor positioning

## Catatan

- Gunakan terminal yang support truecolor dan unicode untuk hasil terbaik
- Disarankan fullscreen terminal sebelum menjalankan
