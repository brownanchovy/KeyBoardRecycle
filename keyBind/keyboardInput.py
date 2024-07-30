from pynput.keyboard import Listener, Key, Events

store = set()
save_store = set()

def uppertoLower(key):
    try:
        if hasattr(key, 'char') and key.char.isupper():
            key = key.char.lower()
    except AttributeError:
        pass
    return key

def handleKeyPress(key):
    key = uppertoLower(key)
    store.add(key)
    save_store.add(format(key))
    print('Press: {}'.format(store))

def handleKeyRelease(key):
    key = uppertoLower(key)
    print('Released: {}'.format(key))
    if key in store:
        store.remove(key)
        print(store)
        # 종료
    if key == Key.esc or not store:
        return False

def setHotkey():
    with Listener(
            on_press=handleKeyPress,
            on_release=handleKeyRelease) as listener:
        listener.join()
    print(save_store)

if __name__ == '__main__':
    setHotkey().run()
