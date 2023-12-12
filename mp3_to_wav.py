import os
from pydub import AudioSegment
import subprocess 
  
# Path to the folder containing the MP3 files
folder_path = "/Users/hugo/Desktop/hugo_copy"
output_path = f"{folder_path}/wav_files"

# Iterate over all files in the directory
for filename in os.listdir(folder_path):
    # Check if the file is an MP3
    if filename.endswith(".mp3"):
        
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, filename.replace(".mp3", ".wav"))
        print(src,dst)
        # convert mp3 to wav file 
        subprocess.call(['ffmpeg', '-i', src, 
                        dst])

# # Path to the folder containing the MP3 files
# folder_path = "/Users/hugo/Desktop/hugo_copy"

# # Iterate over all files in the directory
# for filename in os.listdir(folder_path):
#     # Check if the file is an MP3
#     if filename.endswith(".mp3"):
#         # Full path for source and destination
#         src = os.path.join(folder_path, filename)
#         dst = os.path.join(folder_path, filename.replace(".mp3", ".wav"))
#         print(src,dst)
#         # Convert MP3 to WAV
#         sound = AudioSegment.from_mp3(src)
#         sound.export(dst, format="wav")
