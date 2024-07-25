import keyboard
import time
def no_keys_pressed():
    # 모든 알파벳, 숫자, 수정 키에 대해 검사
    keys_to_check = list(keyboard.all_modifiers) + list(map(str, range(10))) + list('abcdefghijklmnopqrstuvwxyz')
    # 하나라도 눌려있다면 False 반환
    for key in keys_to_check:
        if keyboard.is_pressed(key):
            return False
    # 아무 키도 눌려있지 않다면 True 반환
    return True

def keyInput():
    key_input = set()
    def on_key_event(event):
        if event.event_type == 'down':  # 키를 눌렀을 때
            key_input.add(event.name)
    while True:
        keyboard.hook(on_key_event)
        if key_input is True and no_keys_pressed():
            print("key is selected")
            return key_input