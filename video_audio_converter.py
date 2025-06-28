"""
A simple file for converting a video to an audio file.
If the library is missing, run 'pip install pytube'
"""
from pytube import YouTube

video_url = 'https://[INSERT HERE]'

def extract_audio(video_url, filename) -> str:
   try:
      video = YouTube(video_url)
      stream = video.streams.get_highest_resolution()
      stream.download(filename=filename)
      return filename
   except Exception:
      print('Could not extract audio')
      return None
   
def download_video(video_url, filename) -> str:
   try:
      video = YouTube(video_url)
      stream = video.streams.get_highest_resolution()
      stream.download(filename=filename)
   except Exception as ex:
      print(f'Could not extract audio: {ex}')
      print(ex)
      
def main():
   filename = 'video_file.mp4'
   output_file = extract_audio(video_url, filename)
   print(d'Audio file {output_file} created.')

   
if __name__ == '__main__':
   main()
      