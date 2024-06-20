import win32api
import win32con
import win32gui

# Константы для идентификаторов раскладок клавиатуры
LANG_ENGLISH = 0x0409
LANG_RUSSIAN = 0x0419


def get_keyboard_layout():
    # Получаем идентификатор раскладки клавиатуры для текущего окна
    hWnd = win32gui.GetForegroundWindow()
    thread_id = win32api.GetWindowThreadProcessId(hWnd)[0]
    layout_id = win32api.GetKeyboardLayout(thread_id)
    return layout_id & 0xFFFF


def set_keyboard_layout(lang_id):
    # Смена раскладки клавиатуры
    hwnd = win32gui.GetForegroundWindow()
    thread_id = win32api.GetWindowThreadProcessId(hwnd)[0]
    win32api.PostThreadMessage(thread_id, win32con.WM_INPUTLANGCHANGEREQUEST, 0, win32api.MAKELANGID(lang_id, 0))


def main():
    current_layout = get_keyboard_layout()

    if current_layout == LANG_ENGLISH:
        choice = input(
            'You are currently using English layout. Press "E" to keep English or "R" to switch to Russian: ').upper()
        if choice == 'R':
            set_keyboard_layout(LANG_RUSSIAN)
            print("Switched to Russian layout.")
        else:
            print("Keeping English layout.")
    elif current_layout == LANG_RUSSIAN:
        choice = input(
            'Вы используете русскую раскладку. Нажмите "А", чтобы переключиться на английскую, или "Р", чтобы оставить русскую: ').upper()
        if choice == 'А':
            set_keyboard_layout(LANG_ENGLISH)
            print("Переключено на английскую раскладку.")
        else:
            print("Оставлена русская раскладка.")
    else:
        print("Неизвестная раскладка клавиатуры.")


if __name__ == "__main__":
    main()