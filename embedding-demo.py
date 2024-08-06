import os
import re
import requests
import sys
from num2words import num2words
import os
import pandas as pd
import numpy as np
import tiktoken
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key = os.getenv("40dcb63620bb4875ad74e9878ad4c4cd"),  
  api_version = "2024-02-01",
  azure_endpoint = os.getenv("https://gjun-openai-user04.openai.azure.com/")
)

def generate_embeddings(text, model="text-embedding-ada-002"): # model = "deployment_name"
    return client.embeddings.create(input = [text], model=model).data[0].embedding

#df_bills['ada_v2'] = df_bills["text"].apply(lambda x : generate_embeddings (x, model = 'text-embedding-ada-002')) # model should be set to the deployment name you chose when you deployed the text-embedding-ada-002 (Version 2) model