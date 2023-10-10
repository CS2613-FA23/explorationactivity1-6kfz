# Quick Clip Editor


## Description

QCE is python program that implements [MoviePy](https://github.com/Zulko/moviepy), a video editing library that offers a variety of different ways to quickly edit and create video files. QCE is designed for quickly editing short video clips (gameplay from games such as CS, Rocket League, Valorant) and sharing them to popular social media platforms, many of which have file size limits. With multiple options for reducing video fidelity and trimming video length QCE allows you to quickly share videos with friends without being bothered by any annoying upload limits (Ex: discord 25mb upload limit)

## Getting Started

### Dependencies

* Minimum requirements: Windows 10, [Python 2.7](https://www.python.org/download/releases/2.7/) ([Python 3.12](https://www.python.org/downloads/) is recommended)
* Additional requirements: [pip](https://pip.pypa.io/en/stable/) (easiest way to install MoviePy) 

### Executing program

* After downloading open your terminal and open the directory containing QCE.py, then run
```
python QCE.py
```
* You'll be first greeted with the following message
```
Usage: Choose a folder that only contains video files you'd like to edit
```
* Then you will be prompted for a folder path ex: C:\Users\6kfz\Desktop\VideoFolder\ (for windows)
```
What folder would you like to process?
```

* Next you will select a resize scale, in this example I've chosen 0.7, this will lower the resolution to 70% of it's original size.
```
Type in resize scale (type 1.0 to leave as is): 0.7
```
* In most cases "none" will be the appropriate input, if you want some more fine tuning on quality then play around with different values and see what works.
```
Type in desired bitrate (ex:  1000000 is 1mbs, none is to leave unchanged): none
```
* This will allow you to take a section of your video instead of the whole thing (in case you just had 5s seconds of important video in a 30s clip). This isn't recommended if you're trying to edit multiple clips at once as it will trim all videos in the folder.
```
Would you like to trim the videos? (WARNING this will apply to all videos in folder!) (y or n): y
```
* If you selected "y" in the previous prompt you will be asked to input a starting time and an ending time of your trimmed clip. Here if I had a 30s clip I would set start to 0 and end to 15 to get only the first half.
```
Please select start time (seconds): 0
```
```
Please select start time (seconds): 15
```
###Example

We start with this video:

[![](https://img.youtube.com/vi/stVc8Qd0RmQ/0.jpg)](https://www.youtube.com/watch?v=stVc8Qd0RmQ)

Run the program with this input: 

![This](https://lh3.googleusercontent.com/pw/ADCreHeweoRBT1G1E0lqyt3v8P1ABlMPfN4R-FoYaE-yO_tcp4KrHJsYd-PW2ZPlYLKToFUDLtnfHrze1WIc2vJCmjtDpj6397MsxXtKnPhYMfCaKCld5cUU=w2400)

And we get this:

[![](https://img.youtube.com/vi/ID1PWyKfb_s/0.jpg)](https://www.youtube.com/watch?v=ID1PWyKfb_s)

## Help

* If you run into: 

```
module 'PIL.Image' has no attribute 'ANTIALIAS'
```
when trying to run refer to [this](https://github.com/Zulko/moviepy/issues/2002) for help

## Authors

Rusty Harker  
@6kfz (Discord)




## Acknowledgments

* [MoviePy Documentation](https://zulko.github.io/moviepy/)
* [zip() code snippets](https://www.geeksforgeeks.org/zip-in-python/)
* [Python OS Module Documentation](https://docs.python.org/3/library/os.html)