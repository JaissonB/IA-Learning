from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#Cria o chatbot
chatbot = ChatBot("DumbBot")
#Cria um treinador
trainer = ChatterBotCorpusTrainer(chatbot)

#Executa o treinamento
trainer.train('chatterbot.corpus.portuguese')

trainer.export_for_training('./data.json')

