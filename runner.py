import os
import colorama
from time import sleep
from pyttsx3 import speak
colorama.init()

RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
BLUE = colorama.Fore.BLUE
YELLOW = colorama.Fore.YELLOW
PURPLE = colorama.Fore.MAGENTA
RESET = colorama.Fore.RESET

def cmd(c):
    return os.system(c)

dirs = os.listdir()
if 'venv' not in dirs:
    print(f'{YELLOW}Virtual Environment not Present')
    print(f'{PURPLE}Making the Virtual Environment')
    try:
        if cmd('python -m venv venv') == 0:
            if cmd('pip install -r requirements.txt') == 0:
                raise "Error"
        else:
            raise "Error"
    except:
        print(f'{RED}Virtual Environment can\'t be made, please make it manually{RESET}')

if cmd('start "" launch.bat') == 0:
    print(f'{GREEN}Server Running')
    launch_time = 20
    print(f'{BLUE}Launching the app in {launch_time} secs{RESET}')
    speak(f'launching app in {launch_time} seconds')
    sleep(launch_time)
    cmd('start "" http://127.0.0.1:7860')
else:
    print(f'{RED}Some Error in Launching the App')