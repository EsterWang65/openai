import os  
import requests  
import json  
from openai import AzureOpenAI  
from azure.identity import DefaultAzureCredential, get_bearer_token_provider  
  
endpoint = "https://gjun-open-ai.openai.azure.com/"  
deployment = "Dalle3"  
key = "8b6041cc25f54c05b5e7629715225837"  
  
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=key,  
    api_version="2024-02-01",  
)  
  
result = client.images.generate(  
    model=deployment,  
    prompt="兩隻狗在玩泥巴",  
    n=1  
)  
  
image_url = json.loads(result.model_dump_json())['data'][0]['url']  
print(image_url)  
  
# 下載圖片並儲存到本地  
response = requests.get(image_url)  
if response.status_code == 200:  
    with open('downloaded_image.png', 'wb') as f:  
        f.write(response.content)  
    print("圖片已成功下載並儲存為 'downloaded_image.png'")  
else:  
    print("下載圖片失敗，狀態碼：", response.status_code)  
