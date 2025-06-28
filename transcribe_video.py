"""
Transcribes the text of the specified YouTube video.
"""
import whisper
from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=fqAcwoO0ftc"

def extract_audio(video_url) -> str:
    try:
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        filename = f"{video.title}.mp3"
        stream.download(filename=filename)
        return filename
    except Exception:
        print('Could not extract audio: {ex}')
        return None
    
def transcribe_with_whisper(audio_filename) -> bool:
    try:
        model = whisper.load_model("base")
        print(audio_filename)
        result = model.transcribe(audio_filename)
        with open("transcription_whisper.txt", "w", encoding="utf-8") as txt:
            txt.write(result["text"])
        return True
    except Exception as ex:
        print(ex)
        return False

def main():
    audio_filename = extract_audio(video_url)
    if audio_filename:
        transcribe_with_whisper(audio_filename)

if __name__ == '__main__':
    main()