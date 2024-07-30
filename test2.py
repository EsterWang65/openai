import os  
from openai import AzureOpenAI  
  
# Azure OpenAI 端點  
endpoint = "https://gjun-open-ai.openai.azure.com/"  
  
# 部署的模型名稱  
deployment = "GPT"  
  
# API 金鑰  
key = "8b6041cc25f54c05b5e7629715225837"  
  
# 初始化 AzureOpenAI 客戶端  
client = AzureOpenAI(  
    azure_endpoint=endpoint,  # 設定端點  
    api_key=key,              # 設定 API 金鑰  
    api_version="2024-02-15-preview",  # 設定 API 版本  
)  
  
# 提示使用者輸入系統訊息  
system_message = input("請輸入系統訊息：")  
  
# 初始化對話訊息列表，包含使用者輸入的系統訊息  
messages = [  
    {  
        "role": "system",  
        "content": system_message  
    }  
]  
  
def ask_question(prompt):  
    """  
    接收使用者的問題，並返回 AI 的回答。  
      
    參數:  
    prompt (str): 使用者的問題。  
      
    返回:  
    str: AI 的回答。  
    """  
  
    # 將使用者的問題加入訊息列表  
    messages.append(  
        {  
            "role": "user",  
            "content": prompt  
        }  
    )  
  
    # 呼叫 AzureOpenAI 的 chat.completions.create 方法，獲得 AI 回應  
    completion = client.chat.completions.create(  
        model=deployment,  # 使用的模型  
        messages=messages,  # 傳遞的訊息列表  
        max_tokens=800,     # 回應的最大 token 數  
        temperature=0.7,    # 溫度參數，控制回應的創造力  
        top_p=0.95,         # top_p 參數，控制隨機取樣  
        frequency_penalty=0,  # 控制對高頻詞的懲罰  
        presence_penalty=0,   # 控制對新話題的懲罰  
        stop=None,            # 設定停止序列  
        stream=False          # 是否進行流式傳輸  
    )  
  
    # 將 AI 的回應加入訊息列表  
    ai_response = completion.choices[0].message.content  
    messages.append(  
        {  
            "role": "assistant",  
            "content": ai_response  
        }  
    )  
  
    return ai_response  
  
# 提示使用者輸入問題  
prompt = input("輸入你的問題：")  
  
# 當使用者輸入的問題不為空時，進行迴圈  
while prompt != "":  
    response = ask_question(prompt)  
    print(response)  
    prompt = input("輸入你的問題：")  
