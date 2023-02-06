'''
Just made it nice & clear so that it
will not hurt eyes... (￣▽￣* )

'''
import keyboard

def shortkey(hotkeys: str, event_name: str):
    keyboard.add_hotkey(hotkeys, lambda: keyboard.send(event_name), suppress=True)
