from PIL import Image
import numpy as np

def image_to_normalized_vector(image_path):
    # 画像を開く
    img = Image.open(image_path)
    
    # 画像をRGB形式に変換（必要であれば）
    img = img.convert('RGB')
    
    # 画像データをNumPy配列に変換
    img_array = np.array(img)
    
    # RGB値を0-1の範囲に正規化
    normalized_array = img_array / 255.0
    
    # 3次元配列（高さ、幅、RGB）を1次元ベクトルに変換
    normalized_vector = normalized_array.flatten()
    
    return normalized_vector

# 使用例
image_path = '/Users/iori/file_folder/program/pokemonn/a/image/hitokage.png'
normalized_vector = image_to_normalized_vector(image_path)
print(normalized_vector[:2])
