class SmartChatBot:
    def __init__(self):
        self.context = []  # Stores conversation history for context
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
            "farewell": ["Goodbye!", "See you later!", "Take care!"],
            "how_are_you": ["I'm just a bot, but I'm doing great! How about you?"],
            "default": ["I'm sorry, I didn't quite understand that. Can you rephrase?"],
            "help": [
                "I'm here to assist you. You can ask me about the weather, general knowledge, or just chat with me!"
            ],
        }
        self.keywords = {
            "greeting": ["hello", "hi", "hey"],
            "farewell": ["bye", "goodbye", "exit", "see you"],
            "how_are_you": ["how are you", "how's it going"],
            "help": ["help", "assist", "support"],
        }

    def get_intent(self, user_input):
        """
        Determines the intent of the user's input by matching keywords.
        """
        user_input = user_input.lower()
        for intent, keywords in self.keywords.items():
            if any(keyword in user_input for keyword in keywords):
                return intent
        return "default"

    def get_response(self, intent):
        """
        Selects a response based on the identified intent.
        """
        if intent in self.responses:
            return self.responses[intent][0]  # Use the first response (can randomize later)
        return self.responses["default"][0]

    def save_context(self, user_input):
        """
        Saves the user's input to the context for later use.
        """
        self.context.append(user_input)

    def chatbot(self):
        """
        Main function to run the chatbot.
        """
        print("SmartChatBot: Hi! I'm your smart chatbot. Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ").strip()
            if "exit" in user_input.lower():
                print("SmartChatBot: Goodbye! Have a wonderful day!")
                break
            
            # Save user input to context
            self.save_context(user_input)

            # Determine intent and generate response
            intent = self.get_intent(user_input)
            response = self.get_response(intent)
            print(f"SmartChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    bot = SmartChatBot()
    bot.chatbot()
