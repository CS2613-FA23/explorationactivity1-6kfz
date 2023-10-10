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

* Next you will select a resize scale, in this example I've chosen 0.7, this will lower the resolution to 70% of it's original size
```
Type in resize scale (type 1.0 to leave as is): 0.7
```
* In most cases "none" will be the appropriate input, if you want some more fine tuning on quality then play around with different values and see what works
```
Type in desired bitrate (ex:  1000000 is 1mbs, none is to leave unchanged): none
```


## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)