from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import useful_functions as uf
from time import sleep
import re


bot = ChatBot('AI')
ai = ChatBot('BOT')

trainer = ChatterBotCorpusTrainer(bot)

def check(pattern, string):
    if re.match(pattern, string):
        return True
    else:
        return False

trainer.train('chatterbot.corpus.english')
import os
os.system('cls' if os.name == 'nt' else 'clear')
d = input('>>>')
uf.print_blue(f"AI : {d}")
# ...existing code...
while True:
    b = ai.get_response(d)
    d = bot.get_response(b)
    b_str = str(b)
    d_str = str(d)
    if not check('die', d_str):
        uf.print_green(f"BOT: {b_str}")
    else:
        uf.print_red(" The robot sayed a bad word.")
    sleep(1)
    if not check('die', b_str):
        uf.print_blue(f"AI : {d_str}")

    sleep(1)
# ...existing code...


