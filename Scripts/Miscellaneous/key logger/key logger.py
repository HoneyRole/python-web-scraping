#!/usr/bin/env python
import pynput.keyboard

def key_press(key):
	print(key)

def main():
    keyboard_listner = pynput.keyboard.Listener(on_press=key_press)
    with keyboard_listner:
        keyboard_listner.join()


if __name__ == "__main__":
    main()
