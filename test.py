from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def image_to_normalized_vector(image_path):
    # 画像を開く
    img = Image.open(image_path)
    
    # 画像をRGB形式に変換（必要であれば）
    img = img.convert('RGB')
    
    # 画像データをNumPy配列に変換
    img_array = np.array(img)
    
    # RGB値を0-1の範囲に正規化
    normalized_array = img_array / 255.0
    
    return normalized_array, img.size

def normalized_vector_to_image(normalized_array, size):
    # 正規化された配列を元のスケールに戻す
    img_array = (normalized_array * 255).astype(np.uint8)
    
    # 配列を画像に変換
    img = Image.fromarray(img_array, 'RGB')
    
    # 元の画像のサイズにリサイズ
    img = img.resize(size)
    
    return img

def apply_color_transform(normalized_array, transform_matrix):
    # 画像の形状を取得
    original_shape = normalized_array.shape
    
    # 1次元ベクトルに変換
    flat_array = normalized_array.reshape(-1, 3)
    
    # 線形変換を適用
    transformed_flat_array = flat_array @ transform_matrix.T
    
    # 変換後の値が0-1の範囲に収まるようにクリッピング
    transformed_flat_array = np.clip(transformed_flat_array, 0, 1)
    
    # 元の形状に戻す
    transformed_array = transformed_flat_array.reshape(original_shape)
    
    return transformed_array

# 変換行列（例: RGBの順序を入れ替える）
transform_matrix = np.array([
    [0, 0, 1],  # 赤 -> 青
    [0, 1, 0],  # 緑 -> 緑（そのまま）
    [1, 0, 0]   # 青 -> 赤
])

# 使用例
image_path = '/Users/iori/file_folder/program/pokemonn/a/image/zenigame.png'
normalized_array, size = image_to_normalized_vector(image_path)
transformed_array = apply_color_transform(normalized_array, transform_matrix)
transformed_image = normalized_vector_to_image(transformed_array, size)

# 画像を表示
plt.imshow(transformed_image)
plt.axis('off')  # 軸を表示しない
plt.show()
