import json, bcrypt
from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256

pass_context = CryptContext(schemes =["bcrypt"],deprecated="auto")

def extract_dict_from_string(string):
    try:
        cleaned_string = string.replace('\n', '')
        extracted_dict = json.loads(cleaned_string)
        return extracted_dict
    except json.JSONDecodeError as e:
        # Log or handle JSON decoding error
        print(f"Error decoding JSON: {e}")
        return None

def hashBcrypt(password):
    return pbkdf2_sha256.hash(password)

def verifyBcrypt(password, hashed_password):
    print(password, hashed_password)
    return pbkdf2_sha256.verify(password, hashed_password)