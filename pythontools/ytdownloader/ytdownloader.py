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