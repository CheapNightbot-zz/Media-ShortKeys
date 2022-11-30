# Media-ShortKeys <img src="https://cdn-icons-png.flaticon.com/512/4154/4154727.png"  width="50" height="50">

[![GitHub stars](https://img.shields.io/github/stars/CheapNightbot/Media-ShortKeys?style=social)](https://github.com/CheapNightbot/Media-ShortKeys/stargazers)
[![GitHub license](https://img.shields.io/github/license/CheapNightbot/Media-ShortKeys)](https://github.com/CheapNightbot/Media-ShortKeys/blob/main/LICENSE)
[![Github All Releases](https://img.shields.io/github/downloads/CheapNightbot/Media-ShortKeys/total.svg)]()

<B>POV</B>: Your keyboard doesn't have [Media keys](https://wiki.jriver.com/index.php/Keyboard_Media_Keys)...

### Todo list 〒▽〒
- [x] Create a GUI for Media-ShortKeys.
- [ ] Can set / change custom key combinations through GUI.
- [ ] Maybe add abbreviation feature through GUI.
- [ ] Update [Releases](https://github.com/CheapNightbot/Media-ShortKeys/releases) to the latest v2.0.0
- [ ] Update `README.md`

### Why you need this?
- Many keyboard comes with Media Keys, which can control any media playing on your device (like; play/pause & volume up/down) and it's Kool...
- <B>Best example</B>; you are listening to Spotify and you can't change track or simply play/pause songs without being focused to Spotify app window without Media Keys. Spotify shortcuts like 'Ctrl + Right Arrow' doesn't work if you are not focused to Spotify (or app is in system tray).

<p align="center"> <img src="assets/MediaShortKeys_GUI_Screenshot.png"> </p>

# Feature
> Tested on Windows 10 Pro (64-bit)<br>I'm not sure about any other Operating System.
- Basiclly it simulates *Media Keys* on keyboard (but if you want you can do anything xD).
- Control any media playing on your device by:
    - Play / Pause: ``Ctrl + Shift + Space``
    - Volume Up: ``Ctrl + Shift + Up Arrow``
    - Volume Down: ``Ctrl + Shift + Down Arrow``
    - Mute / Unmute: ``Ctrl + Shift + M``
    - Next: ``Ctrl + Shift + Right Arrow``
    - Previous: ``Ctrl + Shift + Left Arrow``
    - Stop: ``Ctrl + Alt + Space``
- You can add any key combinations you like.

# Usage
> <B>NOTE:</B> If you don't want to install all the packages and stuff, check [releases](https://github.com/CheapNightbot/Media-ShortKeys/releases/tag/v1.0.0). Download and extract .rar file anywhere you like (e.g. C:\Program Files) and follow from *Step 3.* [below](https://github.com/CheapNightbot/Media-ShortKeys#run-on-windows-startup-)

You can clone the repository or download and extract the zip into your project folder.
Make sure to install following packages:
- [![keyboard](https://img.shields.io/badge/keyboard-v0.13.5-blue)](https://pypi.org/project/keyboard/)

    - A Python library used to control keyboard -> register hotkeys, simulate key presses and much more.
```
pip install keyboard
```
- [![pyinstaller](https://img.shields.io/badge/pyinstaller-v5.5-blue)](https://pypi.org/project/pyinstaller/)
    - PyInstaller bundles a Python application and all its dependencies into a single package.
    - (Optional - only if you're going to build .exe file)
```
pip install pyinstaller
```

## Run on Windows Startup ?
If you want to be able to use it without having to run the script every time you open your PC, one solution I came up with is; we can make executable file using pyinstaller, fire the application up whenever you start your PC and let it run in the background. 🤌

1. You simply have to run following command in terminal:
```
pyinstaller -n "Media-ShortKeys" --noconsole --icon=keyboard.ico --add-data="keyboard.ico;." Media-ShortKeys.py
```
- ``-n "App_Name"`` for naming your .exe file.
- ``--noconsole`` will disable the console window for our application so that it can run in background without bothering.
- ``--icon=your_icon.ico`` will set the icon of application. You can add any image as icon, but make sure it's an `.ico` file.
- ``-add-data="your_icon.ico;."`` will add icon file into your application executable folder (without it, you will not be able to see application icon when it will run. Like icon in Task Manager).
- ``Media-ShortKeys.py`` is our python file name.
- For detailed information, check out [Pyinstaller Official Documantation](https://pyinstaller.org/en/stable/) 

2. Go to folder where your python file is, you will found ``dist`` folder. Go inside this folder.
3. There will be your application executable file with the name we give it before, in this case ``Media-ShortKeys.exe``. You can simply run it. Now press ``Ctrl + Shift + M``, you will see Windows overlay of volume; showing volume mute/unmute.
4. Now just copy the ``Media-ShortKeys.exe`` file and press ``win + r`` and type ``shell:startup``. An explorer window will open. Here you can see all your custom program that run on windows startup.
5. Right click anywhere in that folder and click on ``Paste shorcut`` (just rename it and remove "- shortcut" from the end of file name). Now it will run every time you'll open your PC. (you can cross-check it by opening Task Manager > Startup, you will found your application there with Status to Enabled).
