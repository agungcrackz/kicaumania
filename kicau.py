import cv2
import sys
import os
import time
import numpy as np
from ffpyplayer.player import MediaPlayer

# === KONFIGURASI ===
VIDEO_FILE  = "kicau2.mp4"
ASCII_CHARS = " .:-=+*#%@"
# ===================

ASCII_ARRAY = np.array(list(ASCII_CHARS))

def frame_to_ascii(frame, term_w, term_h):
    h, w = frame.shape[:2]
    out_h = 39
    out_w = term_w

    img  = cv2.resize(frame, (out_w, out_h))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.clip(gray * 0.85, 0, 255).astype(np.uint8)

    indices = np.clip(
        (gray.astype(np.float32) / 256 * len(ASCII_CHARS)).astype(np.int32),
        0, len(ASCII_CHARS) - 1
    )
    chars = ASCII_ARRAY[indices]
    return "\n".join("".join(row) for row in chars)

def play_ascii_video(video_path):
    # Baca ukuran terminal saat runtime langsung dari stdout
    try:
        ts = os.get_terminal_size(sys.stdout.fileno())
    except OSError:
        ts = os.terminal_size((117, 39))
    term_w = ts.columns
    term_h = ts.lines - 1

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frame_duration = 1.0 / fps

    player = MediaPlayer(video_path)

    sys.stdout.write("\033[?25l\033[2J\033[H")
    sys.stdout.flush()

    start_time  = time.time()
    frame_index = 0

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            sys.stdout.write("\033[H" + frame_to_ascii(frame, term_w, term_h))
            sys.stdout.flush()

            frame_index += 1
            sleep_time = (start_time + frame_index * frame_duration) - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)

            player.get_frame()

    finally:
        sys.stdout.write("\033[?25h\033[0m\n")
        sys.stdout.flush()
        cap.release()

play_ascii_video(VIDEO_FILE)
