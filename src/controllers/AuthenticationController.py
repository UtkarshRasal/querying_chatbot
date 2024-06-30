from fastapi import HTTPException, FastAPI, Depends
from src.Utils.mongodb_connection import get_mongo_instance
from src.Utils.helpers import hashBcrypt, verifyBcrypt
from src.Utils.tokens import ManageTokens
from src.Utils.validators import AuthTokenValidator

class Authentication:
    
    def __init__(self):
        self.client = get_mongo_instance()
        self.users_model = self.client['user']

    def register_user(self, username, password, confirm_password):
    
        try:
            # check if user already exists in the db
            user = self.users_model.find_one({ 'username': username })
            if user:
                return HTTPException(status_code=401, detail='User already exists')
            

            if password != confirm_password:
                return HTTPException(status_code=401, detail='passwords do not match')
            else:
                # encrypt password before storing in database
                _password = hashBcrypt(password)

                self.users_model.insert_one({ 'username': username, 'password': _password })


                return { 'success': True, 'message': 'user created successfully' }
        except Exception as e:
            return HTTPException(status_code=500, detail=f"{e}")
    
    def login_user(self, username, password):
        try:
            # check if the user exists or not
            user = self.users_model.find_one({ 'username': username })
            if not user:
                return HTTPException(status_code=400, detail='User not found!')
            
            
            hashed_password = user['password']  # encrypted password stored in db

            object_id = str(user['_id'])
            if verifyBcrypt(password, hashed_password):
                print(f"user - {user}")
                print(f"_id - {str(user['_id'])}")
                token_data: AuthTokenValidator = {
                    "username": user['username'],
                    "id": object_id
                }
                access_token = ManageTokens.create_access_token(data={ 'sub': token_data})

                return { 'success': True, 'message': 'Login Successful', 'user': { '_id': object_id, 'username': username, 'access_token': access_token } }
            raise HTTPException(status_code=401, detail='Login creadential invalid')

        except Exception as e:
            return HTTPException(status_code=500, detail=f"{e}")