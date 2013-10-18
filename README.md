# WeeChat-DeaDBeeF
WeeChat-DeaDBeeF is a Python script for WeeChat. It implements commands to control the DeaDBeeF music player, directly from the text box.

###  How does it work?

XChat-DeaDBeeF implements a few commands that can be typed into the text box at any moment. 

Commands:

* **/db launch** - launches DeaDBeeF
* **/db np** - returns information about the current track (not displayed in channels)
* **/db saynp** - displays information about the current track in a channel
* **/db play** - resumes playback if track is paused, plays the selected song* if a track is already playing
* **/db pause** - pauses current track
* **/db next**, **/dbprev** - loads next/previous track in playlist
* **/db stop** - stops current track
* **/db exit** - closes DeaDBeeF

**N.B.**: the selected song is the one that is currently highlighted/clicked on in DeadBeeF.

### Requirements

WeeChat-DeaDBeeF has only been tested with Python 2.7.x, WeeChat 0.4.2, and DeaDBeeF 0.5.6. Older versions of WeeChat are not supported, and versions of DeaDBeeF older than 0.5 are not expected to work either. 

If your distribution does not provide packages for those softwares, compile them after you have fetched the sources:

* [WeeChat 0.4.2](http://weechat.org/download "WeeChat :: download") ([dependencies list](http://www.weechat.org/files/doc/stable/weechat_user.en.html#source_package "Weechat :: User's Guide"); python-dev is also required for WeeChat-DeaDBeeF!)
* [Python 2.7.x](http://www.python.org/getit/ "Download Python") (or 2.6.x)
* [DeaDBeeF 0.5.x](http://deadbeef.sourceforge.net/download.html "DeaDBeeF - Ultimate Music Player For GNU/Linux")

### Installation

Installing XChat-DeaDBeeF is pretty straightforward.

* Hard copy:
    1. Clone the Git repository to any folder (or, alternatively, download the source tarball).
    2. Move **WeeChat-DeaDBeeF.py** to **$HOME/.weechat/python/autoload/** (which contains all auto-loaded Python scripts when WeeChat launches).

* Symbolic link
    1. Clone the Git repository to any folder (or, alternatively, download the source tarball).
    2. Create a symbolic link to **WeeChat-DeaDBeeF.py** in **$HOME/.weechat/python/autoload/** (which contains all auto-loaded Python scripts when WeeChat launches).

WeeChat-DeaDBeeF will now be automatically loaded upon launching WeeChat.


### Contribution

If you wish to contribute to WeeChat-DeaDBeeF, please fork the main branch, commit and submit a pull request. As WeeChat-DeaDBeeF is still in its infancy, bug fixes are prioritized.

### License

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
```
