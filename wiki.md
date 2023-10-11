# Package/Library Overview

## What is MoviePy?

#### Purpose
 MoviePy is a comprehensive Python library [created in 2014](https://github.com/Zulko/moviepy/releases?page=2) that specializes in video editing and manipulation. It offers an array of functionalities to help users process, modify, and enhance video files through code, making it a versatile and powerful tool for video editing tasks. Whether you are a content creator, video editor, data scientist, or a Python enthusiast, MoviePy can be used to automate video-related tasks, create custom video effects, or generate video content programmatically.

#### How do you use it?
* ##### Cut and Concatenate Video Clips:
    * MoviePy makes easy work of cutting and concatenating video clips. You can specify the start and end times for video segments you want to extract and combine them to create a new video. This is handy for creating highlight reels or trimming unnecessary content [[ref](https://pypi.org/project/moviepy/)].

* ##### Add Text and Graphics Overlays:
    * You can overlay text, images, or other graphics onto your videos. For example, you can add subtitles, watermark your videos, or create engaging title sequences. MoviePy provides tools to define the text content, font properties, position, and duration of these overlays [[ref](https://pypi.org/project/moviepy/)].

* ##### Apply Video Effects:
    * MoviePy supports a variety of video effects that can be applied to your videos. You can rotate, resize, and crop videos, adjust their brightness and contrast, apply color filters, and even create custom effects [[ref](https://pypi.org/project/moviepy/)].

* ##### Audio Manipulation:
    * MoviePy allows you to extract, replace, or process audio tracks within videos. You can mute or adjust the volume of specific sections or synchronize audio with video [[ref](https://pypi.org/project/moviepy/)]. 

* ##### Export Videos:
    * Once you've edited your video, MoviePy makes it easy to export the final result in various video file formats [[ref](https://pypi.org/project/moviepy/)]. 

#### In Action ->

##### The video we will be using and abusing:

[![](https://img.youtube.com/vi/UsfGvwqZkAw/0.jpg)](https://www.youtube.com/watch?v=UsfGvwqZkAw)

* .subclip() -> Trim your video down, let's use 10s to 18s
```
VideoFileClip(video_in).subclip(10, 18)
```
Our outout will be:

[![](https://img.youtube.com/vi/dIk3UwDGtV4/0.jpg)](https://www.youtube.com/watch?v=dIk3UwDGtV4)

* .resize() -> change the resolution of your video, let's make it 50% of it;s original size
```
VideoFileClip(video_in).resize(0.5)
```
Our output will be:

[![](https://img.youtube.com/vi/NzRGIbJyMqE/0.jpg)](https://www.youtube.com/watch?v=NzRGIbJyMqE)

* .fx( vfx.speedx, float) -> change the speed of the video (and audio), let's make it twice as fast
```
VideoFileClip(video_in).fx( vfx.speedx, 2) 
```
Our final output is:

[![](https://img.youtube.com/vi/kGO77z4ExRE/0.jpg)](https://www.youtube.com/watch?v=kGO77z4ExRE)

* .write_videofile() -> export the final video, there's tons of options when exporting, some include the frame rate, codec and the bitrate.

```
.write_videofile(output, fps=30, codec='libx264', bitrate = bit_in)
```


## My Experience

#### Why did I choose MoviePy?
 I play lots of video games and end up having lots of fun moments I like to capture and share with my friends. However in most cases if I want to edit those video before sending them I have to download an entire video editor and usually make an account to use their services (if they're free). I thought using a python library that allowed video manipulation could take care of that problem for me.

 #### So, what did I learn?
 MoviePy wasn't very difficult to use and understand, however you need to be able to input files efficiently for MoviePy to process. I ended up learning a lot about Python's OS module and how to create lists of files in a directory and gave me some insight on some useful functions in Python that can be used outside of just the scope of this project (zip() is a great example) 

 #### Final thoughts
 Overall I'd say MoviePy is a pretty neat and useful module. I'd recommend it to anyone who needs a simple yet powerful automated video editing tool, or just wants to have some good old fashion fun and mess around with videos. I'd probably continue using MoviePy as there's many more functions that I haven't used yet, however I may search around for a more recent module as currently MoviePy isn't being maintained as often as it should be and is having problems with deprecated dependencies.

