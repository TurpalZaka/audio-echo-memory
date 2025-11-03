# Audio Echo Memory (Simon-style, Audio-Only)

An accessible audio memory game. Listen to a growing sequence of tones (mapped to keys **1–4**) and repeat it correctly.

## Features
- Pure audio gameplay (no graphics required)
- Tutorial that teaches each key with tones
- Score and persistent high score
- Clean modular structure

## Quick Start
```bash
pip install numpy sounddevice
python main.py
```

> Headphones recommended.

## Controls
- **Menu**: `1` Tutorial, `2` Play, `q` Quit
- **Game**: Press `1–4` to repeat the sequence after it finishes playing

## Modules
- `audio.py` – sine-wave tone generation + feedback
- `game.py` – sequence logic (playback, input check, scoring)
- `tutorial.py` – onboarding loop teaching keys 1–4
- `storage.py` – read/write local high score
- `main.py` – minimal CLI menu (audio-first)
