import pynput
from pynput.keyboard import Key,Listener

def press(key):
    print("{0} pressed",format(key))

def release(key):
    if key==key.esc:
        return False


