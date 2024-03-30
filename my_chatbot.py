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
            'threshold': 0.65,
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
    "Do you like pizza?",
    "Yes, I enjoy a good pizza!",
    "Can you help me with something?",
    "Of course! What do you need help with?",
    "Goodbye",
    "Goodbye! Have a great day!"
]

def train_bot():
    trainer = ListTrainer(chatbot)
    trainer.train(training_data)

    corpus_trainer = ChatterBotCorpusTrainer(chatbot)
    corpus_trainer.train('chatterbot.corpus.english')

def run_chatbot():
    print("Welcome to GOGich ChatBot. Type 'exit' to end the conversation.")
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