# %%
# write a method to download the YouTube video from url and save it to the specified path
import pytube
import os

def download_video(url,path):
    # create a YouTube object
    yt = pytube.YouTube(url)
    
    # get the highest resolution video
    video = yt.streams.get_highest_resolution()
    
    # download the video
    video.download()

    # get the video file name
    video_file = os.path.join(path, video.default_filename)
    print(video_file)
    # rename the file to the desired name
    os.rename(video_file, os.path.join(path, "video.mp4"))
    
    print("Video downloaded successfully!")

# test the method
download_video("https://www.youtube.com/watch?v=LZ34LlaIk88&list=RDKZeI9I875Ig&index=3",'C:\GitHub\VS\ProGitForProgrammers\pythontools\ytdownloader')
# %%
# write a method to download the YouTube audio from url and save it to the specified path
import pytube
import os

def download_audio(url, path):
    # create a YouTube object
    yt = pytube.YouTube(url)

    # get the highest resolution audio
    audio = yt.streams.get_audio_only()

    # download the audio
    audio.download()

    # get the audio file name
    audio_file = os.path.join(path, audio.default_filename)
    print(audio_file)
    # rename the file to the desired name
    os.rename(audio_file, os.path.join(path, "audio.mp3"))

    print("Audio downloaded successfully!")

# test the method
download_audio("https://www.youtube.com/watch?v=LZ34LlaIk88&list=RDKZeI9I875Ig&index=3",'C:\GitHub\VS\ProGitForProgrammers\pythontools\ytdownloader')