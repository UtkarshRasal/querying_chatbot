
from fastapi import HTTPException, status
from src.services.OpenAIService import OpenAIService
# from src.services.EngineerQueryingService import EngineersQuery
from src.Utils.mongodb_connection import get_mongo_instance
# from src.Utils.helpers import amplifyQuery

openAI = OpenAIService()
# engineersQuery = EngineersQuery()

class Message:

    def __init__(self):
        self.client = get_mongo_instance()
        self.threads_model = self.client['threads']

    def send_message(self, message, thread_id, loggedInUser):
        response = openAI.interactBot(message=message, thread_id=thread_id)
        print(f" response")
        if response:
            if not thread_id:
                existing_thread = self.threads_model.find_one({ 'user_id': loggedInUser['id']})
                if existing_thread:
                    # update new thread and last message
                    self.threads_model.update_one(
                        {"_id": existing_thread["_id"]},
                        {"$push": {"threads": {"thread_id": response.get("thread_id"), "last_message": message}}},
                    )
                else:
                    # create a new initial thread
                    self.threads_model.insert_one({
                        "user_id": loggedInUser['id'],
                        "threads": [{
                            "thread_id": response.get("thread_id"),
                            "last_message": message
                        }]
                    })

            engineersList = []
            # amp_query = amplifyQuery(message, response.get("response", {}).get("keywords", [])) 
            # engineers = engineersQuery.get_engineers(amp_query, response.get("response", {}), mode=0)

            # engineerDetails = engineersQuery.get_engineer_details(engineers)

            return { "botResponse": response }

        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error in fetching OpenAI response")