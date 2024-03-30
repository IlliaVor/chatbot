from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response

chatbot = ChatBot(
    'GOGich',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.85,
            'response_selection_method': get_random_response
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            'response_selection_method': get_random_response,
            'threshold': 0.70,
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation',
            'response_selection_method': 'chatterbot.response_selection.get_random_response'
        },
        {
            'import_path': 'chatterbot.logic.TimeLogicAdapter',
            'response_selection_method': 'chatterbot.response_selection.get_random_response'
        },
    ],
    database_uri='sqlite:///database.sqlite3'
)

training_data = [
    "Hi there!",
    "Hello!",
    "How are you?",
    "I'm doing well, thank you.",
    "What's your name?",
    "My name is GOGich.",
    "Tell me a joke.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What's the weather like today?",
    "I'm sorry, I cannot provide weather information at the moment.",
    "What time is it?",
    "It's time for you to ask me another question!",
    "Who created you?",
    "I was created by an awesome developer!",
    "Can you help me with something?",
    "Of course! What do you need help with?",
    "What languages do you speak?",
    "I can communicate in English.",
    "Where do you live?",
    "I exist in the digital world, so I don't have a physical location.",
    "Tell me something interesting.",
    "Did you know that the world's oldest known recipe is for beer?",
    "What's your favorite color?",
    "I don't have preferences like humans do, but I like the color blue!",
    "Do you know any programming languages?",
    "I am written in Python, but I can understand and respond to conversations in natural language.",
    "Can you sing?",
    "I'm afraid I can't sing, but I can help you find song lyrics!",
    "What's the square root of 144?",
    "The square root of 144 is 12.",
    "Tell me a fun fact.",
    "Polar bears are left-handed.",
    "What's the capital of Japan?",
    "The capital of Japan is Tokyo.",
    "Can you tell me a bedtime story?",
    "Once upon a time, in a faraway land, there lived a wise old owl...",
    "What's your favorite animal?",
    "I don't have preferences like humans do, but I find all animals fascinating!"
    "Goodbye",
    "Goodbye! Have a great day!"
]

def train_bot():
    trainer = ListTrainer(chatbot)
    trainer.train(training_data)

    corpus_trainer = ChatterBotCorpusTrainer(chatbot)
    corpus_trainer.train('chatterbot.corpus.english')

def run_chatbot():
    print("Welcome to GOGich ChatBot!. 'exit' - to leave")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("GOGich: Goodbye!")
                break
            else:
                bot_response = chatbot.get_response(user_input)
                print("GOGich:", bot_response)
        except (KeyboardInterrupt, EOFError):
            print("\nGOGich: Goodbye!")
            break
        except Exception as e:
            print("GOGich: An error occurred:", str(e))

if __name__ == "__main__":
    train_bot()
    run_chatbot()