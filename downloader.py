from pytube import YouTube
import os

def download_video(link):
    # save the video in 'downloads' folder after download
    save_path = os.path.join(os.getcwd(), "downloads")
    os.makedirs(save_path, exist_ok=True)  # create the folder if not created before

    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        print(f"Download completed successfully! Video saved to: {save_path}")
    except Exception as e:
        print(f"An error occurred during download: {e}")

# user input
link = input("Enter the YouTube video URL: ")
download_video(link)
