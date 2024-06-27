from openai import OpenAI
from config.defaults import Constants
from src.Utils.helpers import extract_dict_from_string

openAIClient = OpenAI(api_key=Constants.OPEN_AI_SECRET_KEY)

class OpenAIService:
    
    def __init__(self):
        self.client = openAIClient

    def append_to_thread(self, thread_id, message, role='user'):
        return self.client.beta.threads.messages.create(thread_id=thread_id,role=role, content=message)
        

    def run_thread(self, thread_id, assistant_id):

        run = self.client.beta.threads.runs.create_and_poll(thread_id=thread_id, assistant_id=assistant_id)

        if run is not None and run.status == "completed":
            messages = self.client.beta.threads.messages.list(thread_id=thread_id)
            return messages
        else:
            raise 'error in running thread'


    def interactBot(self, message: str, thread_id: str = None):
        _assistant = self.client.beta.assistants.retrieve("asst_gr55Ttqa0X6WaSOWlTJAItdg")

        if not thread_id:
            thread_id = self.client.beta.threads.create().id

        # append new message to thread
        thread_messages = self.append_to_thread(thread_id, message)
        # print(thread_messages)
        if not thread_messages:
            return {'error': 'Error in saving thread', 'thread_id': thread_id, 'thread_message': message }
        all_messages = self.run_thread(thread_id, _assistant.id) 
        
        if all_messages:
            all_messages = all_messages.to_dict()
            latest_response = all_messages['data'][0]
            response = latest_response['content'][0]['text']['value']
            response = extract_dict_from_string(response)

            if not response:
                return {"response": {"error": "Failed to parse response from OpenAI"}, "thread_id": thread_id} 
            response['id'] = latest_response['id']
            response['createdAt'] = latest_response['created_at']

            return {"response": response, "thread_id": thread_id}
        else:
            return {"response": {"error": "No response from the thread"}, "thread_id": thread_id}