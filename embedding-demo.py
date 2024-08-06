from openai import AzureOpenAI
import numpy as np
import pandas as pd

client = AzureOpenAI(
  api_key = ("40dcb63620bb4875ad74e9878ad4c4cd"),  
  api_version = "2024-02-01",
  azure_endpoint = ("https://gjun-openai-user04.openai.azure.com/")
)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def generate_embeddings(text, model="text-embedding-ada-002"): # model = "deployment_name"
    return client.embeddings.create(input = [text], model=model).data[0].embedding

# vector1 = generate_embeddings("coffee")
# vector2 = generate_embeddings("milk")
# vector3 = generate_embeddings("latte")
# cs = cosine_similarity(vector1 + vector2, vector3)
# print(cs)

# df = pd.read_csv("words.csv")
# df["embedding"] = df["text"].apply(lambda x: generate_embeddings(x))
# print(df)
# df.to_csv("word_embeddings.csv")

df = pd.read_csv("word_embeddings.csv")
df["embedding"] = df["embedding"].apply(eval).apply(np.array)
search = input("Please enter a term: ")
search_vector = generate_embeddings(search)
df["similarities"] = df["embedding"].apply(lambda x: cosine_similarity(x, search_vector))
df_result = df.sort_values("similarities", ascending = False).head(10)
print(df_result)