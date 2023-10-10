
import os
from moviepy.editor import *


def process_video(vid_input, output, start, end): #Create video object and perform operations
    if(start and end != -1):
        clip = VideoFileClip(vid_input).subclip(start, end) 
        clip.resize(float(resize_scale)).write_videofile(output, fps=30, codec='libx264', bitrate = bit_in)
    else:
        clip = VideoFileClip(vid_input).resize(float(resize_scale)).write_videofile(output, fps=30, codec='libx264', bitrate = bit_in)


def get_video_paths(folder): #create directory lists and names for new videos
    file_name_list = os.listdir(folder)
    path_name_list = []
    final_name_list = []
    for name in file_name_list:
        path_name_list.append(folder + name)
        final_name_list.append(folder+ "(Edited)" + name)
    return path_name_list, final_name_list

start = -1
end = -1

print("Usage: Choose a folder that only contains video files you'd like to edit")
folder = input("What folder would you like to process? ")
resize_scale = input("Type in resize scale (type 1.0 to leave as is): ")
bit_in = input("Type in desired bitrate (ex:  1000000 is 1mbs, none is to leave unchanged): ")
path_list, final_name_list = get_video_paths(folder)
deck = input("Would you like to trim the videos? (WARNING this will apply to all videos in folder!) (y or n) ")
if(deck == "y"):
    start = int(input("Please select start time (seconds): "))
    end = int(input("Please select end time (seconds): "))

for path, video in zip(path_list, final_name_list):
    process_video(path, video, start, end)

print("Video(s) processed, if output quality is too low try tweaking the resize scale and bitrate :) ")