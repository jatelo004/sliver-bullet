import os
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads variables

api_key = os.getenv("OPENAI_API_KEY")

print(api_key)  # prints the key value at runtime
import os
from dotenv import load_dotenv

load_dotenv()  # reads the .env file

api_key = os.getenv("OPENAI_API_KEY")
x_token = os.getenv("X_BEARER_TOKEN")
fb_token = os.getenv("FB_ACCESS_TOKEN")

print("OpenAI Key:", api_key)
print("X Token:", x_token)
print("FB Token:", fb_token)