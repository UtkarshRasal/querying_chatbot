
from src.services.OpenAIService import OpenAIService

openAI = OpenAIService()

class Message:

    def send_message(self, message, thread_id):
        response = openAI.interactBot(message=message, thread_id=thread_id)

        if not thread_id:
            pass