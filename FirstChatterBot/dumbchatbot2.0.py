from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#Cria o chatbot
chatbot = ChatBot("DumbBot",
    logic_adapters = [
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ]
)
#Cria um treinador
trainer = ListTrainer(chatbot)

talk = ['Oi', 'Ola, tudo bem?',
        'Tudo bem?', 'Tudo otimo',
        'Voce gosta de programar?', 'Sim, eu programo em Python',
        'Voce e gay mano?', 'Todos somos, poucos sabem'
]
#Executa o treinamento
trainer.train(talk)

while True: 
    question = input("User: ")
    answer = chatbot.get_response(question)

    if float(answer.confidence) > .5:
        print('DumbBot: ', answer)
    else:
        print("DumbBot: I'm sorry! I don't have an answer for this question.")