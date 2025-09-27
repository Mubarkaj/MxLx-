from chatterbot import ChatBot
import os
import json
import fixer
import re
from chatterbot.trainers import ListTrainer

latest_ask = ""

pattern1 = re.compile(r".*replaceable1$")

bot = ChatBot("AI")
bot.storage.drop()
trainer = ListTrainer(bot)

os.system("cls")
print("HO IS USING U-BOT?")
while True:
    user = input(">>> ").lower()
    if user == "ayse":
        loc = "anne.json"
        break
    elif user == "samil":
        loc = "datf.json"
        break
    elif user == "yusa":
        loc = "yusa.json"
        break
    else:
        print("user not found.")
        continue

with open(loc, "r", encoding="utf-8") as dg:
    data = json.load(dg)


datas=[i.lower() for i in data]


trainer.train(
datas
)
os.system("cls")

# "a".capitalize
print(f"AI : Merhaba, {user.capitalize()}.")
while True:
    ask = input("Sen : ").lower()



    if ask == fixer.simple_fixer(ask,["ikan'da yoksa"],False) and user == "ayse":
        if latest_ask == "bugun ne pisireyim?":
            print("AI : Ikan'da yoksa kofte, dahada yoksa salata, hicbirr sey yoksa SATIN AL 💵!")
    elif ask in datas:
        ans = bot.get_response(ask)
        ans = str(ans)
        if user == "yusa":
            ans = "Enumerate iki tane cikti verir: num, item. ornek:" + pattern1.sub("\nmyList=['apple','orange']\nfor i, item in enumerate(myList)\n      print(f'{i}-{item}')\n\noutput:\n0-apple\n1-orange",ans)
        print(f"AI : {ans.capitalize()}")
        latest_ask=ask
    else:
        result = fixer.simple_fixer(ask, datas, False)
        if not result:
            print("AI : Anlamadim.")
            latest_ask=ask
        else:
            ans = bot.get_response(result)
            ans = str(ans)
            print(f"AI : {ans.capitalize()}")
            latest_ask=ask
    # elif not fixer.simple_fixer(ask,datas,False):
    #     ans = bot.get_response()
    #     ans = str(ans)
    #     print(f"AI : {ans.capitalize()}")
    # else:
    #     print("Anlamadim")





