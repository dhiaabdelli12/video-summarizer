import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_DIR = os.path.join(ROOT_DIR, 'models')

DATA_DIR = os.path.join(ROOT_DIR, 'data')

VIDEOS_DIR = os.path.join(DATA_DIR, 'videos')
AUDIO_DIR = os.path.join(DATA_DIR, 'audio')

TRANSCRIPTIONS_DIR = os.path.join(DATA_DIR, 'transcriptions')