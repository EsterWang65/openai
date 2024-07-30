import os
import requests
import json
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = os.getenv("ENDPOINT_URL", "https://gjun-open-ai.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "GPT")
key = "8b6041cc25f54c05b5e7629715225837"

      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key = key,
    api_version="2024-05-01-preview",
)

messages = []

prompt = input("請輸入您的問題：")
while prompt != "":
    messages.append(
      {
        "role": "user",
        "content": prompt
        }  
    )
    completion = client.chat.completions.create(
        model=deployment,
        messages = messages,
        max_tokens=800,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )
    messages.append(
        {
        "role": "assistant",
        "content": completion.choices[0].message.content
        } 
    )
    print(completion.choices[0].message.content)
    print(messages)
    prompt = input("請輸入您的問題：")