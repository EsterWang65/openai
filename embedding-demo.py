from openai import AzureOpenAI
import numpy as np

client = AzureOpenAI(
  api_key = ("40dcb63620bb4875ad74e9878ad4c4cd"),  
  api_version = "2024-02-01",
  azure_endpoint = ("https://gjun-openai-user04.openai.azure.com/")
)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def generate_embeddings(text, model="text-embedding-ada-002"): # model = "deployment_name"
    return np.array(client.embeddings.create(input = [text], model=model).data[0].embedding)

vector1 = generate_embeddings("coffee")
vector2 = generate_embeddings("milk")
vector3 = generate_embeddings("latte")
cs = cosine_similarity(vector1 + vector2, vector3)
print(cs)