import keyboard

'''
Media Keys' keyboard event name:

B = Volume up
D = Mute
C = Volume down
Q = Previous Track
G = Play / Pause
P = Next Track
J = Stop

'''

# Volume Up = Ctrl + Shift + ↑
keyboard.add_hotkey('ctrl + shift + up', lambda: keyboard.send("B"), suppress=True)

# Mute / Unmute = Ctrl + Shift + M
keyboard.add_hotkey('ctrl + shift + m', lambda: keyboard.send("D"), suppress=True)

# Volume Down = Ctrl + Shift + ↓
keyboard.add_hotkey('ctrl + shift + down', lambda: keyboard.send("C"), suppress=True)

# Previous Track = Ctrl + Shift + ←
keyboard.add_hotkey('ctrl + shift + left', lambda: keyboard.send("Q"), suppress=True)

# Play / Pause = Ctrl + Shift + Space
keyboard.add_hotkey('ctrl + shift + space', lambda: keyboard.send("G"), suppress=True)

# Next Track = Ctrl + Shift + →
keyboard.add_hotkey('ctrl + shift + right', lambda: keyboard.send("P"), suppress=True)

# Stop = Ctrl + Alt + Space
keyboard.add_hotkey('ctrl + alt + space', lambda: keyboard.send("J"), suppress=True)

keyboard.wait()

# pyinstaller -n "Media-ShortKeys" --noconsole --icon=keyboard.ico --add-data="keyboard.ico;." Media-ShortKeys.py
