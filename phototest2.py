import matplotlib.pyplot as plt
import matplotlib.image as img
import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')   # 如果是用 Colab 需要改變路徑
image = img.imread('/workspaces/openai/images/image_1.jpg')                       # 讀取圖片
plt.imshow(image)                                    # 在圖表中繪製圖片
plt.show()   
