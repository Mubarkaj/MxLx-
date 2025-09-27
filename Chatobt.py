from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('AI')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english')
    
while True:
    user = input("You: ")
    if user.lower() in ("quit", "exit"):
        break
    print("AI: ", bot.get_response(user))