'''
Just made it nice & clear so that it
will not hurt eyes... (￣▽￣* )

Old python file is still there for no reason

'''

import keyboard

def shortkey(hotkeys: str, event_name: str):
    keyboard.add_hotkey(hotkeys, lambda: keyboard.send(event_name), suppress=True)

shortkey('ctrl + shift + up', 'B') # Volume Up
shortkey('ctrl + shift + m', 'D') # Mute / Unmute
shortkey('ctrl + shift + down', 'C') # Volume Down
shortkey('ctrl + shift + left', 'Q') # Previous
shortkey('ctrl + shift + space', 'G') # Play / Pause
shortkey('ctrl + shift + right', 'P') # Next
shortkey('ctrl + alt + space', 'J') # Stop

keyboard.wait()
