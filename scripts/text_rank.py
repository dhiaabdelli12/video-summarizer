from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
import whisper_timestamped as whisper
from settings import *
import json

import os

def summarize_text_with_textrank(text, num_sentences=3):
    summarizer = TextRankSummarizer()
    parser = HtmlParser.from_string(text, '', Tokenizer('english'))
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(s) for s in summary)


audio = whisper.load_audio(os.path.join(AUDIO_DIR,"CqndlPZkjqY.mp3"))

model = whisper.load_model("tiny", device="cpu")

result = whisper.transcribe(model, audio)

print(json.dumps(result, indent = 2, ensure_ascii = False))