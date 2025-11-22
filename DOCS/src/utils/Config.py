import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT")
    KEY = os.getenv("SUBSCR_KEY")
    AZURE_STG_CNT_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")