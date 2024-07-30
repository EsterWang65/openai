import os  # 引入操作系統相關功能的模組  
import requests  # 引入處理 HTTP 請求的模組  
import json  # 引入處理 JSON 格式資料的模組  
from openai import AzureOpenAI  # 從 openai 模組引入 AzureOpenAI 類別  
from azure.identity import DefaultAzureCredential, get_bearer_token_provider  # 引入 Azure 身分驗證相關模組  
  
# 定義 Azure OpenAI 服務的端點 URL  
endpoint = "https://gjun-open-ai.openai.azure.com/"  
  
# 定義部署的模型名稱  
deployment = "GPT"  
  
# 定義 API 金鑰  
key = "8b6041cc25f54c05b5e7629715225837"  
  
# 建立 AzureOpenAI 客戶端  
client = AzureOpenAI(  
    azure_endpoint=endpoint,  # 設定 Azure 端點 URL  
    api_key=key,  # 設定 API 金鑰  
    api_version="2024-05-01-preview",  # 設定 API 版本  
)  
  
# 提示使用者輸入問題  
prompt = input("請輸入您的問題：")  
  
# 初始化訊息列表，存儲用戶和助手的對話  
messages = []  
  
# 當用戶的輸入不為空時，進行以下操作  
while prompt != "":  
    # 將用戶輸入的問題添加到訊息列表中  
    messages.append(  
        {  
            "role": "user",  # 設定角色為用戶  
            "content": prompt  # 設定內容為用戶的輸入  
        }  
    )  
      
    # 向 Azure OpenAI 服務請求生成回應  
    completion = client.chat.completions.create(  
        model=deployment,  # 設定使用的模型  
        messages=messages,  # 傳遞訊息列表  
        max_tokens=800,  # 設定生成回應的最大 token 數  
        temperature=0.7,  # 設定生成回應的隨機性  
        top_p=0.95,  # 設定使用 top-p 取樣  
        frequency_penalty=0,  # 設定頻率懲罰參數  
        presence_penalty=0,  # 設定出現懲罰參數  
        stop=None,  # 設定停止生成的標識符  
        stream=False  # 設定是否使用流式生成  
    )  
      
    # 將助手生成的回應添加到訊息列表中  
    messages.append(  
        {  
            "role": "assistant",  # 設定角色為助手  
            "content": completion.choices[0].message.content  # 設定內容為助手的回應  
        }  
    )  
      
    # 輸出助手的回應  
    print(completion.choices[0].message.content)  
      
    # 輸出完整的訊息列表，便於檢查  
    print(messages)  
      
    # 提示用戶再次輸入問題  
    prompt = input("請輸入您的問題：")  
