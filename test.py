
from termcolor import cprint
import emoji

print('Hello from CMD!')
# Hi Sensei!
cprint("Hello, World!", "green", "on_red", attrs=["bold", "underline"])
print(emoji.emojize('Python is :thumbs_up:'))