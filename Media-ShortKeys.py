import keyboard

'''
Keyboard event names are case sensitive as 'b' and 'B' both are different.
Try running following code (where 1st will type 'd', but 2nd will mute system audio):

keyboard.send("d")
keyboard.send("D")
----------------------------------
Media Keys' keyboard event name:

B = Volume up
D = Mute
C = Volume down
Q = Previous Track
G = Play / Pause
P = Next Track
J = Stop

'''
# ______________________________ #

'''
add_hotkey() function with anonymous lambda function.
You can also add named functions.
'''

# Volume Up = Ctrl + Shift + ↑
keyboard.add_hotkey('ctrl + shift + up', lambda: keyboard.send("B"), suppress=True)

# Mute / Unmute = Ctrl + Shift + M
keyboard.add_hotkey('ctrl + shift + m', lambda: keyboard.send("D"), suppress=True)

# Volume Down = Ctrl + Shift + ↓
keyboard.add_hotkey('ctrl + shift + down', lambda: keyboard.send("C"), suppress=True)

# Previous = Ctrl + Shift + ←
keyboard.add_hotkey('ctrl + shift + left', lambda: keyboard.send("Q"), suppress=True)

# Play / Pause = Ctrl + Shift + Space
keyboard.add_hotkey('ctrl + shift + space', lambda: keyboard.send("G"), suppress=True)

# Next = Ctrl + Shift + →
keyboard.add_hotkey('ctrl + shift + right', lambda: keyboard.send("P"), suppress=True)

# Stop = Ctrl + Alt + Space
keyboard.add_hotkey('ctrl + alt + space', lambda: keyboard.send("J"), suppress=True)

'''
If the program finishes, the hotkey is not in effect anymore
and program will close
It will prevent the program from closing
'''
keyboard.wait()
