from settings import *
from transcribe import download, transcribe
import json
import whisper

#from text_rank import apply_textrank

import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()


model_name = "small"
model = whisper.load_model(model_name)

if __name__=='__main__':

    parser.add_argument("-t", "--transcribe", action="store_true", help="Transcribe")
    parser.add_argument("-s", "--summarize", action="store_true",help="Summarize")

    args = parser.parse_args()


    if args.summarize:
        with open(os.path.join(TRANSCRIPTIONS_DIR,'output.json'), mode='r') as f:
            document = json.load(f)['transcription']
        
        summary = apply_textrank(document)
        print(summary)


    elif args.transcribe:
        url = input('url: ')
        audio = download(url, 360, AUDIO_DIR)

        if audio is not None:
            audio_path = os.path.join(AUDIO_DIR, audio["filename"])
            transcript = transcribe(model, audio_path,save=True)
            data = {
                "title":audio["title"],
                "url":url,
                "transcription":transcript,
                }

            with open(os.path.join(TRANSCRIPTIONS_DIR,'output.json'), 'w+', encoding='UTF-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)